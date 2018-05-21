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
    with.open("comment_replied_to.txt", "r") as file:
        comment_replied_to = file.read()
        comment_replied_to = comment_replied_to.split("\n")
        comment_replied_to = list(filter(None, comment_replied_to))

#open file of comments and filter empty lines
with.open("quotes.txt") as q:
    quotes = q.read()
    quotes = quotes.replace('\n','')
    quotes = quotes.split("/")
    quotes = list(filter(None, quotes))

#open file of names to respond to
with.open("top_players.txt") as t:
    players = t.read()
    players = players.split("\n")
    players = list(filter(None, players))
