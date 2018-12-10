
# RedDefineBot

<div align="center">

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/bhagirathbhard/RedDefineBot/)
[![HitCount](http://hits.dwyl.io/bhagirathbhard/RedDefineBot.svg)](http://hits.dwyl.io/bhagirathbhard/RedDefineBot)
.. image:: https://img.shields.io/pypi/pyversions/sticker.svg
    :target: https://pypi.python.org/pypi/sticker
</div>


**RedDefineBot is a Service bot for Reddit that defines words from Urban Dictionary only when called for. v0.1**

RedDefineBot follows etiquettes defined by the reddit community on [/r/Bottiquette](https://www.reddit.com/r/Bottiquette/wiki/bottiquette)

You can call `RedDefineBot` using the following syntax :
>
>         !reddefine cs50
>

The output would be like this :

>**CS50:**

>**Definition**: This is your first CS lecture. This is your big Harvard class. This is the legend himself, David Malan. This is what your hyped up friends told you about. This is your first pset. This is your first line of code. This is you turning in your first pset. This is your second pset. This is you thinking it's not that bad. This is your friends submitting study cards, thinking that it's pretty cool. This is you pulling an all-nighter on pset 3, after add/drop is over. This is you regretting that you took CS50. This is you wondering what the heck bmp means and how you'll ever implement a hashtable. This is you trying to get help at office hours, but you can't because there's too many other confused students. This is you coming in solidarity with your sleepy fellow students. This is you watching the lectures from laptop, because you stopped going to lecture physically. This is you getting decent at CS. This is you taking your midterm. This is you crying about your midterm. This is you finishing a few more psets. This is you finishing the last psets, and hugging the other people at office hours. This is you doing your final project. This is you at the CS50 fair. This is you walking out of Northwest, feeling like a CS god. This is you wondering if you want to actually do CS. This is you postponing that decision as you pop a bottle of champagne, because it's the end of your CS semester. This is you finishing up the rest of your finals.

>This is CS50.

>[Source](https://www.urbandictionary.com/define.php?term=cs50)

>^(Bleep-bloop. I am a bot. |) [^(Github)](https://github.com/bhagirathbhard)

***

**RedDefineBot is not an auto replying, spamming bot. It only works when it is called for and is a service bot that can be invoked only in welcoming subreddits of the community.**
_______

# Before running any bots

**Use descriptive useragents**. Include a username by which admins can identify you. Tell what your bot is doing and why. Convince the admins that you aren't wasting their bandwidth. Inadequate useragents may cause your bot to get logged out in the middle of your session, and the program will crash. Abusive useragents can get your bot shadowbanned.

[Reddit API rules](https://github.com/reddit/reddit/wiki/API)

________

# Config.py

To standardize and simplify authentication, all bots rely on `config.py`.

________ 

# RedDefineBot.py

This is the main file submitted in cs50.io project folder. It works alongside other files such as  `replied_to.txt`, `words.txt`, `BS4Scrapper.py`.

Currently, it can only operate in the **/r/testingground4bots** subreddit to stay in a sandboxed environment and not offend anybody.
The main method when invoked goes through the comment stream on the subreddit and if it finds the call it is looking for, that in this bot’s scenario is, `“!reddefine word”` then it uses the `BS4Scrapper.py` script to do a word lookup for it on **Urban Dictionary.**

________ 

# BS4Scrapper.py

This script uses Beautiful Soup 4 library in python to scrap relevant information off an HTML page online using LXML.
I am using this to effectively get out the definition of a word off Urban Dictionary.



