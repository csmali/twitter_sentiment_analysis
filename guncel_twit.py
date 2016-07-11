#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twitter import *
import time, openpyxl
import sys

sys.getdefaultencoding()

consumer_key = "38UIavSHtBqzzwomWjwMB5IdM"
consumer_secret = "qG7jj53kRT3JTTHbcpfdhv5Al38thFiJx5LbjQVKBIyBVnQx3M"
access_token = "4777500987-Ro2k28V2JWrZux8OwkDbB2FmSnY8BNXhHZutSnC"
access_token_secret = "1dwBATrUKxoHSYcp0AxAE0SV8S3BdxITWr6h0PRE5WYtT"

t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
sayac = 1
id = 0
while 1:
	try:
		search = t.search.tweets(q='#EURO2016',since_id = id, count=100, lang='tr')
		tweets = search['statuses']
		print '-'
		sayac = 0
		for tweet in tweets:
			try :
				twit = tweet['text'].encode('utf-8')
				name = tweet['user']['screen_name']
				twit = twit.replace('\n',' ')
				#twit = tweet['text']
				if twit[0:3] != 'RT ':
					file = open('guncel_tweets.txt','a')
					file.write(twit + '\n')
					file.close()
					print twit
					sayac = sayac + 1
					time.sleep(1)
				if id < tweet['id']:
					id = tweet['id']
			except Exception as a:
				pass
		if sayac == 0:
			time.sleep(30)
		else:
			print id
	except Exception as b:
		print b
		time.sleep(60)