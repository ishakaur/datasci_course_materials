import oauth2 as oauth
import urllib2 as urllib
import ujson as json

# See assignment1.html instructions or README for how to get these credentials

api_key = "NVQIk7jl0DOYwM6xJODUhZ181"
api_secret = "6l5WPdLRafZa0J8C17hWahZTS43hNcGtjuSGbh7xc32Vi8PeSm"
access_token_key = "538206224-ZZWWgYicgFwQHp8zZtfdnATPgPmlhFBgzLrYCOkN"
access_token_secret = "q6CYXfZ9XB7nS9pKV9InzlKT9zLAbpmySXGRow7IAO8K8"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  # url = "https://stream.twitter.com/1/statuses/sample.json"
  url = "https://api.twitter.com/1.1/search/tweets.json?q=$SPY"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    twresponse = json.loads(line.strip())
    print twresponse
    for status in twresponse[u'statuses']:
      print "{}: {}".format(status["user"]["screen_name"].encode('utf-8'), status["text"].encode('utf-8'))
      raw_input("")

if __name__ == '__main__':
  fetchsamples()
