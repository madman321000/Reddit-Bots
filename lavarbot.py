import praw
import pdb
import re
import os
import random

#create instance
reddit = praw.Reddit('Lavar')

#check if there already is a file
if not os.path.isfile("comment_replied_to.txt"):
    comment_replied_to=[]

#otherwise open the file
else:
    #read into a list and filter all the empty comments
    with open("comment_replied_to.txt", "r") as file:
        comment_replied_to = file.read()
        comment_replied_to = comment_replied_to.split("\n")
        comment_replied_to = list(filter(None, comment_replied_to))

#open file of comments and filter empty lines
with open("quotes.txt", "r") as q:
    quotes = q.read()
    quotes = quotes.replace('\n','')
    quotes = quotes.split("/")
    quotes = list(filter(None, quotes))

#open file of names to respond to
with open("top_players.txt", "r") as t:
    players = t.read()
    players = players.split("\n")
    players = list(filter(None, players))

#open subreddit and get stream of comments
subreddit = reddit.subreddit('nba')
comments = subreddit.stream.comments()
for comment in comments:
    #if comment is not already replied to
    if comment.id not in comment_replied_to:
        #search without case sensitivity
        try:
            text = str(comment.body)
            text = text.split()
            for word in text:
                if word in players:
                    comment.reply(random.choice(quotes))
                    comment_replied_to.append(comment.id)
                    # Write list into file
                    with open("comment_replied_to.txt", "w") as w:
                        for comment_id in comment_replied_to:
                            w.write(comment_id + "\n")
                    break
        except UnicodeEncodeError:
            continue
    else:
        break
