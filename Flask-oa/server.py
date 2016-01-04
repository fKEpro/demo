import urllib, time, random, json

from hashlib import sha1
from flask import Flask, redirect, request, session, render_template

import helpers

#Twitter OAuth Variables
consumer_key = "YOUR TWITTER CONSUMER KEY"
consumer_secret = "YOUR TWITTER CONSUMER SECRET"

rootURL = "http://YOUR SERVER URL"

app = Flask(__name__)

@app.route('/clear')
def clear():
	session.clear()
	session['oauth_secret'] = ''
	session['oauth_token'] = ''
	session['user_id'] = ''
	return "Session wiped"

@app.errorhandler(404)
def fourOhFour(error):
    return render_template('fourohfour.html')

@app.route('/')
def home():

	if not 'oauth_token' in session:
		session.clear()
		session['oauth_secret'] = ''
		session['oauth_token'] = ''

	return render_template('index.html')

@app.route('/authenticate')
def authenticate():

	requestParams = {
		"oauth_callback" : rootURL + "/authorised",
		"oauth_consumer_key" : consumer_key,
		"oauth_nonce" : str(random.randint(1, 999999999)),
		"oauth_signature_method" : "HMAC-SHA1",
		"oauth_timestamp" : int(time.time()),
		"oauth_version" : "1.0"
	}

	theSig = helpers.sign_request(requestParams, "POST", "https://api.twitter.com/oauth/request_token", consumer_secret, session['oauth_secret'])

	requestParams["oauth_signature"] = theSig

	request = urllib2.Request("https://api.twitter.com/oauth/request_token", "")
	request.add_header("Authorization", helpers.create_oauth_headers(requestParams))

	try:
		httpResponse = urllib2.urlopen(request)
	except urllib.HTTPError as e:
		return e.read()

	responseData = helpers.getParameters(httpResponse.read())

	session['oauth_token'] = responseData['oauth_token']
	session['oauth_secret'] = responseData['oauth_token_secret']

	return redirect("https://api.twitter.com/oauth/authorize?oauth_token=" + session['oauth_token'])

@app.route('/authorised')
def authorised():

	if request.args.get('oauth_token', '') == session['oauth_token']:
		
		verifyRequestParams = {
			"oauth_consumer_key" : consumer_key,
			"oauth_nonce" : str(random.randint(1, 999999999)),
			"oauth_signature_method" : "HMAC-SHA1",
			"oauth_timestamp" : int(time.time()),
			"oauth_version" : "1.0",
			"oauth_token" : session['oauth_token']
		}

		print ("SECRET:\n" + session['oauth_secret'] + "\n")

		signVerification = helpers.sign_request(verifyRequestParams, "POST", "https://api.twitter.com/oauth/access_token", consumer_secret, session['oauth_secret'])

		verifyRequestParams["oauth_signature"] = signVerification

		verifyRequest = urllib2.Request("https://api.twitter.com/oauth/access_token", "oauth_verifier=" + request.args.get('oauth_verifier'))
		verifyRequest.add_header("Authorization", helpers.create_oauth_headers(verifyRequestParams))
		
		try:
			httpResponse = urllib2.urlopen(verifyRequest)
		except urllib.HTTPError as e:
			return e.read()

		responseData = helpers.getParameters(httpResponse.read())

		session['oauth_token'] = responseData["oauth_token"]
		session['oauth_secret'] = responseData["oauth_token_secret"]
		session['user_id'] = responseData['user_id']

	return redirect(rootURL)

@app.route('/get-tweets')
@app.route('/get-tweets/<count>')
def getTweets(count=0):

	if session['oauth_token'] == "" or session['oauth_secret'] == "":
		return redirect(rootURL)

	tweetRequestParams = {
		"oauth_consumer_key" : consumer_key,
		"oauth_nonce" : helpers.nonce(32),
		"oauth_signature_method" : "HMAC-SHA1",
		"oauth_timestamp" : int(time.time()),
		"oauth_version" : "1.0",
		"oauth_token" : session['oauth_token'],
		"user_id" : session['user_id'],
		"count" : str(count)
	}

	tweetRequest = helpers.sign_request(tweetRequestParams, "GET", "https://api.twitter.com/1.1/statuses/user_timeline.json", consumer_secret, session['oauth_secret'])

	tweetRequestParams["oauth_signature"] = tweetRequest

	makeRequest = urllib2.Request("https://api.twitter.com/1.1/statuses/user_timeline.json?count=" + tweetRequestParams['count'] + "&user_id=" + tweetRequestParams['user_id'])
	
	del tweetRequestParams['user_id'], tweetRequestParams['count']

	makeRequest.add_header("Authorization", helpers.create_oauth_headers(tweetRequestParams))

	try:
		 httpResponse = urllib2.urlopen(makeRequest)
	except urllib.HTTPError as e:
		return e.read()

	tweetResponse = json.loads(httpResponse.read())

	return render_template('tweets.html', data=tweetResponse)

if __name__ == '__main__':
	
	app.secret_key = 'R4nDOMCRypt0gr4ph1cK3yf0R5355i0N'
	app.run(host='0.0.0.0', debug=True)