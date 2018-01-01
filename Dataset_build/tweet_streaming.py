import tweepy
import json
import time
import re

consumer_token = '0'
consumer_secret = '0'
access_token = '0'
access_token_secret = '0'

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

file = open('teams1.json', 'a')
tweets = []

class TweetStreamListener(tweepy.StreamListener):
    def __init__(self):
        self.file = tweets
    def on_data(self, data):
        tw_obj = json.loads(data)
        str = tw_obj["text"]
        try:
            if tw_obj["user"]["location"] is not None:
                json.dump(tw_obj, file)
                file.write(',')
                file.write('\n')
                print(tw_obj["user"]["location"])
        except:
            pass
    def on_error(self, status_code):
        if status_code == 420:
            return False

tweetStreamListener = TweetStreamListener()
tweetStream = tweepy.Stream(auth = api.auth, listener=tweetStreamListener)
tweetStream.filter(track = ["dennis schröder", "marco belinelli", "ersan ilyasova", "mike muscala", "kent bazemore", "atlanta hawks",
                            "kemba walker", "nicolas batum", "michael kidd-gilchrist", "marvin williams", "	dwight howard", "charlotte hornets",
                            "goran dragic", "dion waiters", "josh richardson", "james johnson", "kelly olynyk", "miami heat",
                            "elfrid payton", "evan fournier", "jonathon simmons", "aaron gordon", "nikola vucevic", "orlando magic",
                            "tim frazier", "bradley beal", "kelly oubre jr.", "otto porter", "marcin gortat", "washington wizards",
                            "kris dunn", "justin holiday", "denzel valentine", "lauri markkanen", "robin lopez", "chicago bulls",
                            "jose calderon", "j.r. smith", "lebron james", "jae crowder", "kevin love", "cleveland cavaliers",
                            "reggie jackson", "avery bradley", "stanley johnson", "tobias harris", "andre drummond", "detroit pistons",
                            "kyrie irving", "jaylen brown", "jayson tatum", "marcus morris", "al horford", "boston celtics",
                            "spencer dinwiddie", "allen crabbe", "demarre carroll", "rondae hollis-jefferson", "timofey mozgov", "brooklyn nets",
                            "jarrett jack", "damyean dotson", "courtney lee", "kristaps porzingis", "enes kanter", "new york knicks",
                            "dennis smith", "yogi ferrell", "wesley matthews", "harrison barnes", "dirk nowitzki", "dallas mavericks",
                            "chris paul", "james harden", "trevor ariza", "ryan anderson", "clint capela", "houston rockets",
                            "mario chalmers", "james ennis iii", "dillon brooks", "jarell martin", "marc gasol", "memphis grizzlies",
                            "steph curry", "klay thompson", "kevin durant", "draymond green", "zaza pachulia", "golden state warriors",
                            "austin rivers", "lou williams", "wesley johnson", "danilo gallinari", "deandre jordan", "los angeles clippers",
                            "lonzo ball", "kentavious caldwell-pope", "brandon ingram", "larry nance jr.", "brook lopez", "los angeles lakers",
                            "jamal murray", "gary harris", "wilson chandler", "kenneth faried", "nikola jokic", "denver nuggets",
                            "jeff teague", "jimmy butler", "andrew wiggins", "taj gibson", "karl-anthony towns", "minnesota timberwolves",
                            "russell westbrook", "andre roberson", "paul george", "carmelo anthony", "steven adams", "oklahoma city thunder",
                            "darren collison", "victor oladipo", "bojan bogdanovic", "thaddeus young", "myles turner", "indiana pacers",
                            "eric bledsoe", "tony snell", "khris middleton", "giannis antetokounmpo", "john henson", "milwaukee bucks",
                            "jerryd bayless", "j.j. redick", "ben simmons", "robert covington", "joel embiid", "philadelphia 76ers",
                            "kyle lowry", "demar derozan", "c.j. miles", "serge ibaka", "jonas valanciunas", "toronto raptors",
                            "rajon rondo", "jrue holiday", "e'twaun moore", "anthony davis", "demarcus cousins", "new orleans pelicans",
                            "tony parker", "danny green", "kyle anderson", "lamarcus aldridge", "pau gasol", "san antonio spurs",
                            "tyler ulis", "troy daniels", "t.j. warren", "marquese chriss", "tyson chandler", "phoenix suns",
                            "george hill", "garrett temple", "bogdan bogdanovic", "zach randolph", "willie cauley-stein", "sacramento kings",
                            "damian lillard", "c.j. mccollum", "al-farouq aminu", "noah vonleh", "jusuf nurkic", "portland trail blazers",
                            "ricky rubio", "donovan mitchell", "joe ingles", "derrick favors", "rudy gobert", "utah jazz"])
