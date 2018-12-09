from bs4 import BeautifulSoup
import requests
import praw
import config
import time
import random
from BS4Scrapper import *

#authenticate bot's account details using information kept in config.py
def authenticate():
    print("Logging on to RedDefine Bot...")
    reddit = praw.Reddit(username = config.username,
                         password = config.password,
                         client_id = config.client_id,
                         client_secret = config.client_secret,
                         user_agent = "RedDefine SERVICE bot providing information only when called for. v0.1")
    print("Logged in!\n")
    return reddit

#running the main bot
def run_bot(reddit, comment_id):

    print("Obtaining comments...\n")

    '''
    according to the guide created with the help of reddit community, https://www.reddit.com/r/Bottiquette/wiki/bottiquette,
    provides certain bot ettiquettes to follow. it is suggested not to make your bot monitor all the subreddits on reddit.
    I am therefore only going to allow certain subreddits that would be benefited by the presence of this bot.
    
    '''
    for comment in reddit.subreddit("testingground4bots").comments(limit=None):
                
        if "!reddefine " in comment.body and comment.id not in comment_id:
            word_list = str(comment.body).split()
            for n in range(len(word_list)):
                if word_list[n] == '!reddefine':
                    break
          
            word = ''
            
            for item in word_list[n+1:]:
                word += item
                if item != word_list[-1]:
                    word += ' '
            print(f'the word identified as "{word}" in {comment.id}')

            try:
                #replies back the correct syntax and example on how to use the bot if someone calls it without a word
                if word == '':
                    comment.reply('Please use the correct syntax to call me! \n Example : "!reddefine smh"\n\n***\n\n^(Bleep-bloop. I am a bot. |) [^(Github)](https://github.com/bhagirathbhard)')
                    print("Replied to an empty call comment" + comment.id)

                    with open("replied_to.txt","a") as f:
                        f.write(comment.id + "\n")
                
                #if the bot is called with the proper syntax it begins the wordlookup 
                elif word != '':
                    definition = word_lookup(word)
                    source = 'https://www.urbandictionary.com/define.php?term='+word
                    comment.reply(f'#{word.capitalize()}:\n\n**Definition**: {definition}\n\n[Source]({source})\n\n***\n\n^(Bleep-bloop. I am a bot. |) [^(Github)](https://github.com/bhagirathbhard)')
                    print("Replied to comment : Found the word " + comment.id)

                    with open("replied_to.txt", "a") as f:
                        f.write(comment.id + "\n")
                        
                else:
                    comment.reply('I can\'t find that word on Urban Dictionary.\n\n***\n\n^(Bleep-bloop. I am a bot. |) [^(Github)](https://github.com/bhagirathbhard)')
                    print("Replied to comment : Could not find that word " + comment.id)
                    with open("replied_to.txt", "a") as f:
                        f.write(comment.id + "\n")

            #exception call when something unexpected has happened.    
            except:
                comment.reply('I can\'t find that word on Urban Dictionary.\n\n***\n\n^(Bleep-bloop. I am a bot. |) [^(Github)](https://github.com/bhagirathbhard)')
                print("Exception Call " + comment.id)
                with open("replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")

'''
end of the main functionality of the bot, I am trying to introduce more services into this bot if one doesnt work.
hopefully if this works i can add wikipedia, youtube, etc.
'''

#gets the comment IDs of comments that have already been replied to. avoiding duplication and spam
def get_ids():
    with open("replied_to.txt", "r") as f:
        replied_to = f.read()
        replied_to = replied_to.split("\n")
    return replied_to

#main method
def main():
    reddit = authenticate()
    while True:
        try:
            comment_id = get_ids()
            run_bot(reddit, comment_id)
        except:
            print('Error. Sleeping for 5 seconds \n')
            time.sleep(5)

if __name__ == '__main__':
    main()