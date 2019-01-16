import datetime
import math
import tweepy
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


now = datetime.date.today() # current year
next_year = datetime.date(now.year + 1 , 1,1) # first day of next year
current_year_beginning = datetime.date(now.year,1,1)
days_until_next_year = next_year - now
days_of_this_year = next_year - current_year_beginning 
day_of_the_year = days_of_this_year - days_until_next_year 
percent  =  math.ceil((day_of_the_year / days_of_this_year) * 100)
percent_of_10 = math.ceil(percent / 10)
full_bars =  percent_of_10
empty_bars = 10 - percent_of_10

progress_string = ( "▓" * full_bars + "░" * empty_bars + " " + str(percent) + "%" )

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()

api.update_status(progress_string)
