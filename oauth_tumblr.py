 # -*- coding: utf-8 -*-

import urlparse
import oauth2 as oauth
import pytumblr
from til import factsChecker, sanitizeFacts

consumer_key = 'consumer key'
consumer_secret = 'consumer secret' 

request_token_url = 'http://www.tumblr.com/oauth/request_token'
access_token_url = 'http://www.tumblr.com/oauth/access_token'
authorize_url = 'http://www.tumblr.com/oauth/authorize'


def getTokens():
	consumer = oauth.Consumer(consumer_key, consumer_secret)
	client = oauth.Client(consumer)

	# Step 1: Get a request token. This is a temporary token that is used for 
	# having the user authorize an access token and to sign the request to obtain 
	# said access token.
	resp, content = client.request(request_token_url, "POST")
	if resp['status'] != '200':
	        raise Exception("Invalid response %s." % resp['status'])

	request_token = dict(urlparse.parse_qsl(content))

	print "Request Token:"
	print "    - oauth_token        = %s" % request_token['oauth_token']
	print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
	print 

	# Step 2: Redirect to the provider. Since this is a CLI script we do not 
	# redirect. In a web application you would redirect the user to the URL
	# below.

	print "Go to the following link in your browser:"
	print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
	print 

	# After the user has granted access to you, the consumer, the provider will
	# redirect you to whatever URL you have told them to redirect to. You can 
	# usually define this in the oauth_callback argument as well.
	accepted = 'n'
	while accepted.lower() == 'n':
	        accepted = raw_input('Have you authorized me? (y/n) ')
	        oauth_verifier = raw_input('What is the OAuth Verifier? ')

	# Step 3: Once the consumer has redirected the user back to the oauth_callback
	# URL you can request the access token the user has approved. You use the 
	# request token to sign this request. After this is done you throw away the
	# request token and use the access token returned. You should store this 
	# access token somewhere safe, like a database, for future use.
	token = oauth.Token(request_token['oauth_token'],
	    request_token['oauth_token_secret'])
	token.set_verifier(oauth_verifier)
	client = oauth.Client(consumer, token)

	resp, content = client.request(access_token_url, "POST")
	access_token = dict(urlparse.parse_qsl(content))

	oauth_token = access_token['oauth_token']
	oauth_secret = access_token['oauth_token_secret']

	return oauth_token, oauth_secret

def createClient():
	cred = getTokens()
	agent = pytumblr.TumblrRestClient(
	    consumer_key,
	    consumer_secret,
	    cred[0], #oauth_token
	    cred[1], #oauth_secret
	)
	return agent

def createPost():
	'''
	Create posts from facts fetched and sanitized to remove unwanted characters
	'''
	facts = sanitizeFacts()
	agent = createClient()
	blog = "tumblr blog name"
	for id, content in facts.iteritems():
		agent.create_text(blog, state="queue", body= content +"\n "+ id, tags=['facts', 'TIL', 'todayilearned'],)

def main():
	createPost()

if __name__ == '__main__':
	main()