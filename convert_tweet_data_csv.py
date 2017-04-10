import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np


print '***This script may take some time depending on the number of tweets you have collected.***\n'

#Reading Tweets
print 'Reading in tweet data from file...'
tweets_data_path = 'nohup_test.out'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
    	if not str(line).startswith("{\"limit\":{\"track"):
        	tweet = json.loads(line)
        	tweets_data.append(tweet)
    except:
        continue

print '(number of tweets read in: ' + str(len(tweets_data)) + ')\n'

#Structuring Tweets
print 'Structuring tweet data...\n'
tweets = pd.DataFrame()

print 'Structuring text of tweets..\n'
tweets['text'] = [tweet.get('text','') for tweet in tweets_data]

print 'Structuring language of tweets..\n'
tweets['lang'] = [tweet.get('lang','') for tweet in tweets_data]

print 'Structuring creation date of tweets..\n'
tweets['created_at'] = [tweet.get('created_at','') for tweet in tweets_data]

print 'Structuring ID number of tweets..\n'
tweets['tweet_id'] = [tweet.get('id','') for tweet in tweets_data]

print 'Structuring location of tweets..\n'
tweets['tweet_location'] = [tweet['place']['country']if "place" in tweet and tweet['place'] else np.nan for tweet in tweets_data ]

print 'Structuring user ID number of tweets..\n'
tweets['user_id'] = [tweet.get('user', '').get('id', '') for tweet in tweets_data]

print 'Structuring user name of tweets..\n'
tweets['user_name'] = [tweet.get('user', '').get('name', '') for tweet in tweets_data]

print 'Structuring user screen name of tweets..\n'
tweets['user_screen_name'] = [tweet.get('user', '').get('screen_name', '') for tweet in tweets_data]

print 'Structuring user location of tweets..\n'
tweets['user_location'] = [tweet.get('user', '').get('location', '') for tweet in tweets_data]


print 'Exporting tweet data to CSV file...\n'
tweets.to_csv('tweets_export.csv', encoding='utf-8')



