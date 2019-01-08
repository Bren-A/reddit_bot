#!/usr/bin/env python3

# Postfinder
# This is my first bot. It is meant to update the user when there 
# are new posts that contain a specific keyword in it.
# Specifically used to find new posts about deals for a specific item in /r/frugalmalefashion

import praw # Imports necessary items to use reddit's api

# Import the reddit variable from other file
import os.path

from client import reddit

# Variable that sets the subreddit that the api will work in
sub = 'frugalmalefashion'

# Comment has to contain this phrase to activate bot
keyword = 'off'

for post in reddit.subreddit(sub).new(limit=10):
	if keyword in post.title.lower() :
		print(post.title)
		print('----------------')