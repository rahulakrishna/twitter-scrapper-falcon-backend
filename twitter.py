from bs4 import BeautifulSoup
from urllib.request import urlopen
import falcon
import json
from falcon_cors import CORS
import sentiment_mod as senty

cors = CORS(allow_origins_list=['http://localhost:3000'])

class TwitterResource(object):
	def on_get(self,req,resp,username):
		print(req)
		print(username)
		# username=raw_input()
		url='https://twitter.com/'+username
		# page=urllib2.urlopen(url).read()
		page = urlopen(url)
		soup = BeautifulSoup(page,"lxml")
		title=soup.title.string
		tweets=soup.find_all('p',class_='tweet-text')
		response=[]
		print(tweets)
		for tweet in tweets:
			# senty.sentiment(tweet.string)
			if tweet.string==None:
				print(tweet.get_text())
				sentiment = str(senty.sentiment(tweet.get_text()))
				print(sentiment)
				item = {
					'text':str(tweet.get_text()),
					'sentiment':sentiment
				}
				print(item)
				response.append(item.copy())
			else:
				print(tweet.string)
				sentiment = str(senty.sentiment(tweet.string))
				item = {'text':tweet.string,'sentiment':sentiment}
				print(item)
				response.append(item.copy())
		# Now we have to send the tweets back
		resp.status=falcon.HTTP_200
		# resp.body="Hello"
		print(response)
		resp.body=json.dumps(response)

app=falcon.API(middleware=[cors.middleware])

twitter=TwitterResource()

app.add_route('/twitter/{username}',twitter)