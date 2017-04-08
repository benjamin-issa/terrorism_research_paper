# -*- coding: utf-8 -*-

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "Your Access Token"
access_token_secret = "Your Access Token Secret"
consumer_key = "Your Consumer Key"
consumer_secret = "Your Consumer Secret"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filters Twitter Streams to capture data by words the words "terrorism" and "terrorist" in all supported languages.
    #I just punshed into Google Translate....
    stream.filter(track=['terrorist', 'terrorism', u"الإرهابي", u"الإرهاب", u"সন্ত্রাসবাদী", u"সন্ত্রাসবাদ", 'terorista', 'terorismus', 'terrorisme', 'Terrorismus', u"τρομοκράτης", u"τρομοκρατία", 'terrorista', 'terrorismo', u"تروریستی", u"تروریسم", 'terroristi', 'terrorismi', 'terorista','terorismo', 'terroriste', 'terrorisme', u"מְחַבֵּל", u"טֵרוֹר", u"आतंकवादी", u"आतंकवादी", u"आतंकवाद", 'terrorista', 'terrorizmus', 'teroris', 'terorisme', 'terrorista', 'terrorismo', u"テロリスト", u"テロ", u"테러리스트", u"테러", 'pengganas', 'keganasan', 'terrorisme', 'terrorisme', 'terrorysta', 'terroryzm', 'terrorista', 'terrorismo', 'terorist', 'terorism', u"Террорист", u"Терроризм", u"ผู้ก่อการร้าย", u"การก่อการร้าย", u"terörist", u"Terörizm", u"терорист", u"тероризм", u"دہشت گرد", u"دہشت گردی", u"Khủng bố", u"恐怖分子", u"恐怖主义", u"恐怖分子", u"恐怖主義" ])