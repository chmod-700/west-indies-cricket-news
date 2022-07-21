from GoogleNews import GoogleNews
import tweepy
import config
import logging



logging.basicConfig(filename='bot_log.log',level=logging.INFO,format='%(asctime)s: %(levelname)s: %(message)s')

googlenews = GoogleNews()
googlenews.set_lang('en')
googlenews.search('west indies AND cricket') 
googlenews.set_period('1d')
raw_results = googlenews.results()
first_result = raw_results[0]



for key in first_result:
    if key == 'title':
        Title = first_result[key]
        #print('Title: ', first_result[key])
    elif key == 'link':
        article_link = first_result[key]
        #print('Link: ', first_result[key] )

hashtags = '#WI #cricket #westindies #rally #cwi #sport #windies' 
#print(Title,'\n',Link,'\n',hashtags)

tweet = Title+' '+'\n'+article_link+' '+'\n'+hashtags




def getClient():
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN, 
                       consumer_key=config.API_KEY, 
                       consumer_secret=config.API_KEY_SECRET, 
                       access_token=config.ACCESS_TOKEN, 
                       access_token_secret=config.ACCESS_TOKEN_SECRET)
    return client



client = getClient()

try:
    client.create_tweet(text=tweet)
    logging.info("Tweet has been updated successfully.")

except Exception as e:
    logging.error(e)
    

    
#References
#https://realpython.com/twitter-bot-python-tweepy/
#https://www.youtube.com/watch?v=EXhgOBllQVYs