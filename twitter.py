import tweepy
import time

ACCESS_TOKEN = '780358704642203649-iFeBFnFmE3vTupPvNQRRwfkfkPIg6WO'
ACCESS_SECRET = 'E4S0og7F6bJlUPYAlrF5tBhkT8bxAXyYSVyTubvM5TCvF'
CONSUMER_KEY = 'Vw3ihnDj0rD3sh2OvsSwPWtwc'
CONSUMER_SECRET = 'Oq13MepTwM4D5Lls9727OF0rYsXaZ9mEu5bBVAmPzYNtlycjAD'
SEARCH=input("Aisa Cup 2018")
FROM=input("2018-09-27")
TO=input("2018-09-28")
INPUT_FILE_PATH= './'+SEARCH+'.txt'

num=int(input("50"))
auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
i=0;

f = open(INPUT_FILE_PATH, 'w', encoding='utf-8')

for res in tweepy.Cursor(api.search, q=SEARCH, rpp=100, count=20, result_type="recent", since = FROM,until =TO, include_entities=True, lang="en").items(num):
	i+=1
	f.write(res.user.screen_name)
	f.write(' ')
	f.write('[')
	f.write(res.created_at.strftime("%d/%b/%Y:%H:%M:%S %Z"))
	f.write(']')	
	f.write(" ")
	f.write('"')
	f.write(res.text.replace('\n',''))
	f.write('"')
	f.write(" ")
	f.write(str(res.user.followers_count))
	f.write(" ")
	f.write(str(res.retweet_count))
	f.write('\n')
f.close
print("Tweets retrieved ",i)