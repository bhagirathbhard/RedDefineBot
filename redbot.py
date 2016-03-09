import praw
import time

r = praw.Reddit(user_agent = "an account that replies thank you, prime minister of India")
r.login()
words_to_match= ['thanks modi']
cache = []

def run_bot():
	subreddit = r.get_subreddit("india")
	comments = subreddit.get_comments(limit=50)
	for comment in comments:
		comment_text = comment.body.lower()
		isMatch = any(string in comment_text for string in words_to_match)
		if comment.id not in cache and isMatch:
			comment.reply("you are welcome saar.")
			cache.append(comment.id)

while True:
	run_bot()
	time.sleep(10)
