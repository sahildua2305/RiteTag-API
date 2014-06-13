# Using RiteTag API(https://ritetag.com/rest-api)

import requests
from requests_oauthlib import OAuth1
import json

# Obtain your app details along with secret token from http://ritetag.com/developer/signup
ck = '' # consumer_key
cs = '' # consumer_secret
tk = '' # token
ts = '' # token_secret

# Taking input from command line while execution
query = raw_input()

# Authorizing with the given details using OAuth1 module
auth = OAuth1(ck, cs, tk, ts)
url = "http://ritetag.com/api/v2/ai/twitter/"+query
response = requests.get(url, auth=auth)

result = response.content
print result
