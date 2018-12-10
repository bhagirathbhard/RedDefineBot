# RedDefineBot

**RedDefineBot is a Service bot for Reddit that defines words from Urban Dictionary only when called for. v0.1**

RedDefineBot follows etiquettes defined by the reddit community on [/r/botettiqutte](https://www.reddit.com/r/Bottiquette/wiki/bottiquette)

**RedDefineBot is not an auto replying, spamming bot. It only works when it is called for and is a service bot that can be invoked only in welcoming subreddits of the community.**
_______

### Before running any bots

**Use descriptive useragents**. Include a username by which admins can identify you. Tell what your bot is doing and why. Convince the admins that you aren't wasting their bandwidth. Inadequate useragents may cause your bot to get logged out in the middle of your session, and the program will crash. Abusive useragents can get your bot shadowbanned.

[Reddit API rules](https://github.com/reddit/reddit/wiki/API)

________

### config.py

To standardize and simplify authentication, all bots rely on `config.py`.

________ 

### reddefinebot.py

This is the main file submitted in cs50.io project folder. It works alongside other files such as  `replied_to.txt`, `words.txt`, `BS4Scrapper.py`.

Currently, it can only operate in the **/r/testingground4bots** subreddit to stay in a sandboxed environment and not offend anybody.
The main method when invoked goes through the comment stream on the subreddit and if it finds the call it is looking for, that in this bot’s scenario is, `“!reddefine word”` then it uses the `BS4Scrapper.py` script to do a word lookup for it on **Urban Dictionary.**
