#!/usr/bin/python
import praw
import warnings


warnings.filterwarnings("ignore")


user_agent = ("PyEng Bot 0.1")

r = praw.Reddit(user_agent = user_agent)
username = raw_input("What is your reddit username?: ")
user = r.get_redditor(username)
print "Din karma er: ", user.link_karma + user.comment_karma
uSubReddit = raw_input("What subreddit would you like to browse?: ")

subreddit = r.get_subreddit(uSubReddit)

def run():
    for submission in subreddit.get_hot(limit = 5):
        print "Title: ", submission.title
        print "Text: ", submission.selftext
        print "Score: ", submission.score, "\n"
        print "---------------------------------"
        print "Get ready for the next -----------------------\n"

    
    
def changeSub():
    newSubReddit = raw_input("What subreddit would you like to browse now?: ")
    subreddit = r.get_subreddit(newSubReddit)
    for submission in subreddit.get_hot(limit = 5):
        print "Title: ", submission.title
        print "Text: ", submission.selftext
        print "Score: ", submission.score
        print "---------------------------------\n"
        print "THIS IS THE NEXT POST!!!!\n"
        print "---------------------------------\n"
        
run()
print "use command changeSub() to change subreddit"
