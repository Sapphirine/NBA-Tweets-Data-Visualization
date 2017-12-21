from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
import json
with open('/Users/matthew/Desktop/clean1.json','r') as data_file:    
    dat=json.load(data_file)
print(type(dat))
    
ofile = open('finaldata1.json','a')
sid = SentimentIntensityAnalyzer()
for data in dat:
    paragraph=data['text']
    sentences = sent_tokenizer.tokenize(paragraph)
    sentsum = 0
    sentnum = 0
    for sentence in sentences:
        print(sentence)
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]), end='')
        print(ss['compound'])
        sentsum += ss['compound']
        sentnum += 1
    data['sentiment'] = sentsum/sentnum
    print(data['sentiment'])
    json.dump(data, ofile)
    ofile.write(',')
    ofile.write('\n')
        #test=TextBlob(sentence)
        #print()
        #print(test.sentiment.polarity)
        #print()