'''#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
import os

form = cgi.FieldStorage() 
print("Content-type: text/html\r\n\r\n")

if form.getvalue('sk'):
   word = form.getvalue('sk')

inp=word


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json


#Twitter consumer key, consumer secret, access token, access secret

ckey="Rxla0uihgEQV6fo0jSYTCLTdy"
csecret="0axu4srnQTxcBFKuLQUSCjBPxDao1C9MfmxpJBCvFBsaL5mkFq"
atoken="2917106385-jWo9vsBBmvMRhwfb634BIqhOtyz2KrNr1njiAS1"
asecret="sNg5YqwcvR79YnJKNcbttSKcPm9672bJ3gNMWrrY8b4Ad"
# set up stream listener
class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
		# collect all desired data fields 
        if 'text' in all_data:
          tweet         = all_data["text"]
          created_at    = all_data["created_at"]
          retweeted     = all_data["retweeted"]
          username      = all_data["user"]["screen_name"]
          #user_tz       = all_data["user"]["time_zone"]
          user_location = all_data["user"]["location"]
          #user_coordinates   = all_data["coordinates"]
          
          print((username,tweet,user_location))
          
          return True
        else:
          return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

# create stream and filter on a searchterm
twitterStream = Stream(auth, listener())
twitterStream.filter(track=word,languages = ["en"], stall_warnings = True)

# x axis values
x = [i for i in range (len(sent))]
 
# y axis values
y =sent
 
# plotting strip plot with seaborn
ax = plt.plot(x, y);
 
# giving labels to x-axis and y-axis
#ax.set(xlabel ='length', ylabel ='sentiments')
 
# giving title to the plot
plt.title('Sentiment-o-metre');

# function to show plot
plt.show()
 
# function to show plot
#plt.show()

#f=open('python.json','r')'''

'''a=f.read()
f.close()

from nltk.tokenize import word_tokenize
import operator 
import json
from collections import Counter
from nltk.corpus import stopwords
import string
 
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
stop.append("http")
stop.append("https")
print "YO"

from nltk import bigrams 
print "YO"
ca = Counter()
#print stop
l=a.split('\n')
#print l
#c=1
fi=open('tweets.txt','w')
fi.close()
#print "YO"
for t in l:
	try:
		tweet=json.loads(t)
		ttweet=tweet["text"]
		#print ttweet
		x=word_tokenize(ttweet)
		#print x
		ll=[]
		#print x
		for words in x:
			if words not in stop:
				ll.append(words)
		#print "X   =     "+str(x)
		#terms_bigram = bigrams(ll)
		#print ', '.join(' '.join((a, b)) for a, b in terms_bigram)
		#print "\nLL  =     "+str(ll)
		str1 = ' '.join(ll).encode('utf-8').strip()
		fi=open('tweets.txt','a')
		fi.write(str(str1)+"\n")	
		fi.close()	
		#print str1
		#print c
		#c=c+1
		ca.update(ll)
	except Exception as e:
		print str(e)

print(ca.most_common(5))'''




#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
import os
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

form = cgi.FieldStorage() 
print("Content-type: text/html\r\n\r\n")

if form.getvalue('sk'):
   word = form.getvalue('sk')

f=open('tweets.txt','w')
f.close



#Twitter consumer key, consumer secret, access token, access secret
ckey="Rxla0uihgEQV6fo0jSYTCLTdy"
csecret="0axu4srnQTxcBFKuLQUSCjBPxDao1C9MfmxpJBCvFBsaL5mkFq"
atoken="2917106385-jWo9vsBBmvMRhwfb634BIqhOtyz2KrNr1njiAS1"
asecret="sNg5YqwcvR79YnJKNcbttSKcPm9672bJ3gNMWrrY8b4Ad"

#info lists
tweettext=[]
tweetuser=[]
tweetlocn=[]
tweetretw=[]
#sentiment analysis 
sent=[]

# set up stream listener
class listener(StreamListener):

    def __init__(self, time_limit=60):
        self.start_time = time.time()
        self.limit = time_limit
        super(listener, self).__init__()

    def on_data(self, data):
	if (time.time() - self.start_time) < self.limit:
	    all_data = json.loads(data)
            if 'text' in all_data:
		  tweet         = all_data["text"]
		  #created_at    = all_data["created_at"]
		  retweeted     = all_data["retweeted"]
		  username      = all_data["user"]["screen_name"]
		  #user_tz       = all_data["user"]["time_zone"]
		  user_location = all_data["user"]["location"]
		  #user_coordinates   = all_data["coordinates"]
          
          	  #print((username,tweet,user_location))
		  tweettext.append(tweet)
		  tweetuser.append(username)
		  tweetretw.append(retweeted)
		  tweetlocn.append(user_location)
          
          	  return True
       	    else:
          	  return True
        else:
            
            return False

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

# create stream and filter on a searchterm
twitterStream = Stream(auth, listener(time_limit=10))
twitterStream.filter(track=[word],languages = ["en"], stall_warnings = True)

from nltk.tokenize import word_tokenize
import operator 
import json
from collections import Counter
from nltk.corpus import stopwords
import string
 
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
stop.append("http")
stop.append("https")

for t in tweettext:
		x=word_tokenize(t)
		ll=[]
		for words in x:
			if words not in stop:
				ll.append(words)
		str1 = ' '.join(ll).encode('utf-8').strip()
		fi=open('tweets.txt','a')
		fi.write(str(str1)+"\n")	
		fi.close()	


from pyspark import SparkConf, SparkContext
from textblob import TextBlob
from operator import add
import sys
## Constants
APP_NAME = " Big Data "

##OTHER FUNCTIONS/CLASSES
def main(sc,filename):
   textRDD = sc.textFile(filename)
   with open("/root/Desktop/proj/tweets.txt","r") as fp:
      for i, line in enumerate(fp):
         if "\xe2" in line:
	    sp=TextBlob(repr(line)).sentiment.polarity
#	    print str(sp)+"************************"

	    sent.append(sp)


if __name__ == "__main__":
   # Configure Spark
   conf = SparkConf().setAppName(APP_NAME)
   conf = conf.setMaster("local[*]")
   sc   = SparkContext(conf=conf)
   filename = "/root/Desktop/proj/tweets.txt"
   # Execute Main functionality
   main(sc, filename)


s1 = ' '.join(str(tweetlocn).split(','))
s2 = ' '.join(str(tweetretw).split(','))
s3 = ' '.join(str(tweetuser).split(','))
#s4 = ' '.join(str(sent).split(','))
#print tweettext


#file for business analytics
f=open('/root/Desktop/proj/ba.txt','w')
str((s1,s2,s3))+"\n"
f.write(s1)
f.write(s2)
f.write(s3)
#f.write(s4)
f.close()

print s1+"\n"+s2+"\n"+s3+"\n***************************"
slen=len(sent)
#print sent
#print slen


#df = pd.read_csv('/root/Desktop/proj/tweets.txt')
slen=len(sent)

# x axis values
x = [i for i in range (len(sent))]
 
# y axis values
y =sent
 
# plotting strip plot with seaborn
ax = plt.plot(x, y);
 
# giving labels to x-axis and y-axis
#ax.set(xlabel ='length', ylabel ='sentiments')
 
# giving title to the plot
plt.title('Sentiment-o-metre');

# function to show plot
plt.show()
 
# function to show plot
#plt.show()
#sns.tsplot(x='slen' , y='sent' , fit_reg=False , data=sent)
