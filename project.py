import requests
import requests.auth
import praw
import time
from praw.models import MoreComments
from keys import *
import json
from datetime import datetime, tzinfo

output = {}

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    password = PASSWORD,
    user_agent="Comment Extraction by r/krishasher",
    username = "krishasher",
)

#user input
subred = str(input("What is the subreddit name without '/r' \n"))
while subred[0]=="r" and subred[1]=="/":
    print("Do not include /r in the string")

sr = reddit.subreddit(subred)
output['subreddit'] = sr.title

#dictionary is used to store top 5 submissions for the last 26 weeks
dict_time = {}
for i in range(26):
    dict_time[f'Week {i+1}'] = []

#The for loop below looks through each submission and adds it to the dictionary
#depending on the week from today's date it was created.  The nested for loop
#takes the six top comments of the submission  
sub_comment = []
for submission in reddit.subreddit(subred).top(time_filter="all", limit = 100):
    sub_comment = []
    unix = submission.created_utc
    t = int((time.time() - unix)//604800)
    sub_time = str(datetime.fromtimestamp(unix))

    if (t < 26):
        new_dict = {'submission': submission.title,
                    'up-votes': submission.score}
        for comment in submission.comments[:6]:
            if isinstance(comment, MoreComments):
                continue
            sub_comment.append(comment.body)
        new_dict['created'] = sub_time
        new_dict['comments'] = sub_comment
        dict_time[f'Week {t+1}'].append(new_dict)

output['subreddit_info'] = dict_time

print("Done looking through subreddit posts")
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
    print("New json file is created using ouput dictionary")
    
