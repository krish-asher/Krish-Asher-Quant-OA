import requests
import requests.auth
import praw
import time
import datetime
from praw.models import MoreComments
from keys import *
import json

output = {}

#requests used to connect with Reddit API

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    password = PASSWORD,
    user_agent="Comment Extraction by r/krishasher",
    username = "krishasher",
)

#user input
subred = str(input("What is the subreddit name\n"))
while subred[0]=="r" and subred[1]=="/":
    print("Do not include /r in the string")

#This requests gives the access token which is used in the header below under 'Authorization'
#The above code can be deleted once the acess token is found
sr = reddit.subreddit(subred)

#dictionary is used to store top 5 submissions for the last 26 weeks
dict_time = {}
for i in range(26):
    dict_time[i] = []

#The for loop below looks through each submission and adds it to the dictionary
#depending on the week from today's date it was created.  The nested for loop
#takes the six top comments of the submission  
sub_comment = []
for submission in reddit.subreddit(subred).top(time_filter="all", limit = None):
    new_dict = {'submission': submission.title,
                'up-votes': submission.score}
    t = (time.time() - submission.created_utc)//604800
    if (t < 26):
        for comment in submission.comments[0:6]:
            if isinstance(comment, MoreComments):
                continue
            sub_comment.append(comment.body)
        new_dict['comments'] = sub_comment
        dict_time[t].append(new_dict)

output['subreddit_info'] = dict_time

print("Done")
#This finds all the users in the subreddit and adds them to the dictionary
#if they are less than three months old
users = {}
for comment in sr.comments(limit=50):
    auth = comment.author
    if auth:
        auth_d = auth.created_utc
        if not auth in users and time.time()-auth_d<54432000:
            users[str(auth)] = auth_d
output['subreddit_users'] = users

output['subbreddit_user_count'] = len(users)

json_object = json.dumps(output, indent=4)

#Putting into json file
with open('./reddit-subreddit-scraper/output.json', 'w') as f:
    f.write(json_object)
    print("New json file is created from data.json file")
    
