import requests
import requests.auth
import praw
import time
import datetime
from praw.models import MoreComments
from keys import *

#requests used to connect with Reddit API

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    password = PASSWORD,
    user_agent="Comment Extraction by r/krishasher",
    username = "krishasher",
)

#This requests gives the access token which is used in the header below under 'Authorization'
#The above code can be deleted once the acess token is found
sr = reddit.subreddit('funny')

#dictionary is used to store top 5 submissions for the last 26 weeks
dict_time = {}
for i in range(26):
    dict_time[i] = []

#The for loop below looks through each submission and adds it to the dictionary
#depending on the week from today's date it was created.  The nested for loop
#takes the six top comments of the submission  
for submission in reddit.subreddit("funny").top(time_filter="all", limit = None):
    for comment in submission.comments[0:6]:
        if isinstance(comment, MoreComments):
            continue
        print(comment.body)

    t = (time.time() - submission.created_utc)//604800
    if (t < 26):
        dict_time[t].append(submission)

#This finds all the users in the subreddit and adds them to the dictionary
#if they are less than three months old
users = {}
for comment in sr.comments(limit=1000):
     auth = comment.author
     if not auth in users and time.time()-auth.created_utc<54432000:
         users[auth] = auth.created_utc

print(dict_time[0])





for i in range(26):
    print(i , dict_time[i])
    
