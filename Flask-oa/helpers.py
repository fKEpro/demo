import urllib, collections, hmac, binascii, time, random, string

from hashlib import sha1

def getParameters(paramString):

	paramString = paramString.split("&")

	pDict = {}

	for parameter in paramString:
		parameter = parameter.split("=")

		pDict[parameter[0]] = parameter[1]

	return pDict

def sign_request(parameters, method, baseURL, consumer_secret, oauth_secret):

	baseURL = urllib.quote(baseURL, '')

	p = collections.OrderedDict(sorted(parameters.items(), key=lambda t: t[0]))

	requestString = method + "&" + baseURL + "&"
	parameterString = ""

	for idx, key in enumerate(p.keys()):
		paramString = key + "=" + urllib.quote(str(p[key]), '')
		if idx < len(p.keys()) - 1:
			paramString += "&"

		parameterString += paramString

	result = requestString + urllib.quote(parameterString, '')

	signingKey = consumer_secret + "&" + oauth_secret

	hashed = hmac.new(signingKey, result, sha1)
	signature = binascii.b2a_base64(hashed.digest())[:-1]

	return signature

def create_oauth_headers(oauthParams):
	
	oauthp = collections.OrderedDict(sorted(oauthParams.items(), key=lambda t: t[0]))

	headerString = "OAuth "

	for idx, key in enumerate(oauthp):
		hString = key + "=\"" + urllib.quote(str(oauthp[key]), '') + "\""
		if idx < len(oauthp.keys()) - 1:
			hString += ", "

		headerString += hString

	return headerString

def nonce(size=32, chars="abcdef" + string.digits):
	uonce = ''.join(random.choice(chars) for x in range(size)) 
	return uonce