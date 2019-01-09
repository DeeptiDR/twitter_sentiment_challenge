import csv
import tweepy
from textblob import TextBlob

csvData=[['Tweets','sentimentAnalysis']]
with open('fileCSV.csv','w') as csvFile:
	writer=csv.writer(csvFile)
	writer.writerows(csvData)
  
#Authenticate
consumer_key='XXXXXX...' #Enter the consumer key from your twitter developer account
consumer_secret='XXXXX...' #Enter the consumer secret from your twitter developer account

access_token='XXXXX...' #Enter the access token from your twitter developer account
access_token_secret='XXXXX...' #Enter the access token secret from your twitter developer account

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

#Retrieve Tweets
public_tweets=api.search('Data Science') #you can use any keyword as per your wish. I chose 'Data Science'

for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text) #printing each tweet in terminal
    print(analysis.sentiment) 
    print("")

    row=[[analysis, analysis.sentiment]]

    with open('fileCSV.csv', 'a') as csvFile:
    	writer = csv.writer(csvFile)
    	writer.writerows(row)
      
csvFile.close()
