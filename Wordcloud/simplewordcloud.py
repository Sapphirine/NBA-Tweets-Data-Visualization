import findspark
findspark.init()

import pyspark
from os import path
from PIL import Image
import numpy as np
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

conf = SparkConf().setAppName("Spark Count")
sc = SparkContext(conf=conf).getOrCreate()
spark = SparkSession.builder.appName('wordcloud').getOrCreate()

states = [
      u'Alaska', u'Alabama', u'Arkansas', u'American Samoa', u'Arizona', u'California', u'Colorado', 
      u'Connecticut', u'District of Columbia', u'Delaware', u'Florida', u'Georgia', u'Guam', u'Hawaii', 
      u'Iowa', u'Idaho', u'Illinois', u'Indiana', u'Kansas', u'Kentucky', u'Louisiana', u'Massachusetts', 
      u'Maryland', u'Maine', u'Michigan', u'Minnesota', u'Missouri', u'Mississippi', u'Montana', 
      u'North Carolina', u' North Dakota', u'Nebraska', u'New Hampshire', u'New Jersey', u'New Mexico', 
      u'Nevada', u'New York', u'Ohio', u'Oklahoma', u'Oregon', u'Pennsylvania', u'Puerto Rico', 
      u'Rhode Island', u'South Carolina', u'South Dakota', u'Tennessee', u'Texas', u'Utah', u'Virginia', 
      u'Virgin Islands', u'Vermont', u'Washington', u'Wisconsin', u'West Virginia', u'Wyoming'
]

wordsrdd = spark.read.json("finaldata.json").rdd.filter(lambda x: x[0] is None)
wordsteamrdd = wordsrdd.map(lambda x: (x.team, x.text)).reduceByKey(lambda x, y: x + ' ' + y)
wordsstaterdd = wordsrdd.map(lambda x: (x.state, x.text)).reduceByKey(lambda x, y: x + ' ' + y)

stopwords = set(STOPWORDS)
stopwords.add("https")
stopwords.add("co")
stopwords.add("t")
stopwords.add("on")
stopwords.add("RT")
stopwords.add("World_Wide_Wob")

otext = ''

for data in wordsteamrdd.collect():
	otext += data[1]
	text = data[1]
	mask = np.array(Image.open('nba.jpg'))
	wc = WordCloud(background_color="white", max_words=2000, mask=mask, stopwords=stopwords, max_font_size=80, random_state=42)
	wc.generate(text)
	output = 'team/' + data[0] + '.png'
	wc.to_file(output)
	image_colors = ImageColorGenerator(mask)

mask = np.array(Image.open('nba.jpg'))
wc = WordCloud(background_color="white", max_words=2000, mask=mask, stopwords=stopwords, max_font_size=80, random_state=42)
wc.generate(otext)
output = 'Overall.png'
wc.to_file(output)

otext = ''

for data in wordsstaterdd.collect():
	if data[0] not in states:
		otext += ' '
		otext += data[1]
		continue
	text = data[1]
	mask = np.array(Image.open('nba.jpg'))
	wc = WordCloud(background_color="white", max_words=2000, mask=mask, stopwords=stopwords, max_font_size=80, random_state=42)
	wc.generate(text)
	output = 'state/' + data[0] + '.png'
	wc.to_file(output)
	image_colors = ImageColorGenerator(mask)

mask = np.array(Image.open('nba.jpg'))
wc = WordCloud(background_color="white", max_words=2000, mask=mask, stopwords=stopwords, max_font_size=80, random_state=42)
wc.generate(otext)
output = 'state/Overseas.png'
wc.to_file(output)

print('done')

sc.stop()