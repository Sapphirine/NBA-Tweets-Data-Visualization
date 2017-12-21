# NBA-Tweets-Data-Visualization

Before we start, we need to install the following on the computer: 

- Python
- Tweepy 
- PySpark
- Pandas
- Neo4j
- NLTK
- Google Maps API for Python
- Word Cloud

Please refer to the official documents of these package for installation details. After installing above, we are ready to start. 

##Dataset building and data cleaning

We gather data from Twitter using Twitter Streaming API. Tweepy, a pre-built package for Python, handles auth in an easy way, providing convenience to users who wish to gather data from Twitter. To gather data, open python file “tweet_streaming.py”. We need to configure our credentials obtained from developer.twitter.com. We need to fill in the consumer token, consumer secret, access token, and access secret. Then we need to specify the path of the output file at the row “file”. In the function “on data”,  in the “try” block, we can modify the condition and operation that we want to apply to our data. If we leave it as default, the program will only pick up those tweets whose owner has specified their user location. Finally, we can modify the keyword list in the filter to decide which keywords in tweets to track. 

To clean data, use the file “location_clean.py”. First, put in the Google Maps API Access Key obtained from Google Maps into  gmaps = googlemaps.Client( key= ). Then, modify the value of iFile and oFile to change the desired file path of input and output. Please remember that the input file is the same output file of the previous applications. 

Finally, we can run the two applications in python. Type in the console python tweet_streaming.py to gather data from Twitter. The console will output the count of tweets that has been gathered. When you feel like that you are done gathering, simply hit Ctrl + C to exit the program. Then, clean the data by typing python location_clean.py. Wait for the program to naturally end, the output file will be the cleaned data in a JSON file called final_data.json. 

##Data Analysis

To get the sentiment analysis result, run sentimentclean.py and sparkclean.py in series in python. Configure the input path to be the path of final_data.json. The input of sparkclean.py should be the output of sentimentclean.py. Finally, the output should contain the sentiment score on average. 

##Data Visualization - Word Cloud

First, change the path in “wordrdd” to be the path of final_data.json from data cleaning. Also, change the path in the value of output to be the ones you desire. Change the path in image.open to change the shape that the output pictures will be in. Then, run the simplewordcloud.py. Add values to the function stopwords.add() to filter out the unwanted words that you do not want to include in the result. Wait for the program to normally complete. Then, we will have the corresponding pictures for each state and each team. 

##Data Visualization - Heatmap

AmChart is a powerful tool for data visualization. We use amChart for our heatmap to show heat distribution and sentiment distribution. To make it work, a user only need to refer several scripts in the script labels. For instance, ammap.js is a javascript file for a basic map. And usaLow.js is another file for initiating the US map. To apply any style, a javascript named light.js or dark.js is needed. After including these scripts and loading values such as the count of tweets or average sentiment of every state, you are ready to go.

##Data Visualization - Neo4j

Neo4j is a NoSQL graph-based database developed by Neo4j, Inc. Described by its developers as an ACID-compliant transactional database with native graph storage and processing, Neo4j is the most popular graph database according to DB-Engines ranking. It also provides and user-friendly web client. After we load the data analysis result CSV files to the Neo4j database. We can easily do query and visualize the relationship between each vertex through it. 

At first, we built a database in Neo4j Desktop and then we copy the three csv files to the "import" folder of the dataset. Then we start the database and open the web browser to access bolt://localhost:7867. Then we run every line of Neo4j.cypher in the browser clinet to load the vertices and edges from three csv files to the graph database.

We can try to do this query in Neo4J, "MATCH p=()-[r:Edge]->() Where toInt(r.cnt)>1000 and toFloat(r.avg)>0.3 return p" which showsw the (state, team) pair where the state have many fans of the related teams.  