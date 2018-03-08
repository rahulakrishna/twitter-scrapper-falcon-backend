from bs4 import BeautifulSoup
import urllib2
import falcon
import json

class TwitterResource(object):
	def on_get(self,req,resp,username):
		print(req)
		print(username)
		# username=raw_input()
		url='https://twitter.com/'+username
		page=urllib2.urlopen(url).read()
		soup = BeautifulSoup(page,"lxml")
		title=soup.title.string
		tweets=soup.find_all('p',class_='tweet-text')
		response=[]
		print(tweets)
		for tweet in tweets:
			if tweet.string==None:
				print(tweet.get_text())
				response.append(tweet.get_text())
			else:
				print(tweet.string)
				response.append(tweet.string)
		# Now we have to send the tweets back
		resp.status=falcon.HTTP_200
		# resp.body="Hello"
		resp.body=json.dumps({"tweets":response})

app=falcon.API()

twitter=TwitterResource()

app.add_route('/twitter/{username}',twitter)