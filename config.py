import os

#seperate place to store the Oauth information for the bot to use.

username = 'RedDefineBot'
password = os.environ['reddit_password']
client_secret = os.environ['clients']
client_id = os.environ['clientid']

#it is important to not upload this file on github / share it with anyone. If you want to post it, redact all the revealing information to better protect account details.
