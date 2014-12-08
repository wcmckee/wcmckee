# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <h1>GetsDrawn DotCom</h1>

# <markdowncell>

# This is a python script to generate the website GetsDrawn. It takes data from /r/RedditGetsDrawn and makes something awesome.
# 
# The script has envolved and been rewritten several times. 
# 
# The first script for rgdsnatch was written after I got banned from posting my artwork on /r/RedditGetsDrawn. The plan was to create a new site that displayed stuff from /r/RedditGetsDrawn. 
# 
# Currently it only displays the most recent 25 items on redditgetsdrawn.
# 
# This is moving forward from rgdsnatch.py because I am stuck on it.  
# 
# TODO
# 
# Fix the links that don't link to png/jpeg and link to webaddress. 
# Needs to get the images that are at that web address and embed them.
# 
# Display artwork submitted under the images. 
# 
# Upload artwork to user. Sends them a message on redditgetsdrawn with links. 
# 
# More pandas

# <codecell>

import os 
import requests
from bs4 import BeautifulSoup
import re
import json
import time
import praw
import dominate
from dominate.tags import * 
from time import gmtime, strftime
#import nose
#import unittest
import numpy as np
import pandas as pd
from pandas import *
#import pyttsx

# <codecell>

gtsdrndir = ('/home/wcmckee/getsdrawndotcom')

# <codecell>

os.chdir(gtsdrndir)

# <codecell>

r = praw.Reddit(user_agent='getsdrawndotcom')

# <codecell>

getmin = r.get_redditor('itwillbemine')

# <codecell>

mincom = getmin.get_comments()

# <codecell>

#engine = pyttsx.init()

#engine.say('The quick brown fox jumped over the lazy dog.')
#engine.runAndWait()

# <codecell>

shtweet = []

# <codecell>

for mi in mincom:
    print mi
    shtweet.append(mi)

# <codecell>

bodycom = []
bodyicv = dict()

# <codecell>

#beginz = pyttsx.init()

# <codecell>

for shtz in shtweet:
    print shtz.downs
    print shtz.ups
    print shtz.body
    print shtz.replies
    #beginz.say(shtz.author)
    #beginz.say(shtz.body)
    #beginz.runAndWait()
    
    bodycom.append(shtz.body)
    #bodyic

# <codecell>

bodycom 

# <codecell>

getnewr = r.get_subreddit('redditgetsdrawn')

# <codecell>

rdnew = getnewr.get_new()

# <codecell>

lisrgc = []

# <codecell>

for uz in rdnew:
    #print uz
    lisrgc.append(uz)

# <codecell>

gtdrndic = dict()

# <codecell>

for lisr in lisrgc:
    print lisr.url
    print lisr.title
    print lisr.author
    print lisr.comments
    gtdrndic.update({'title': lisr.title})

# <codecell>

opsinz = open('/home/wcmckee/visignsys/index.meta', 'r')
panz = opsinz.read()

# <codecell>

#panz()

# <codecell>

doc = dominate.document(title='GetsDrawn')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')
    
    with div():
        attr(cls='header')
        h1('GetsDrawn')
        p(img('imgs/getsdrawn-bw.png', src='imgs/getsdrawn-bw.png'))
        p('Updated ', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        p(panz)
        p(bodycom)
    
    

with doc:
    with div(id='body').add(ol()):
        for rdz in lisrgc:
            h1(rdz.title)
            #a(rdz.url)
            if '.jpg' or '.png' in rdz.url:
                #print rdz.url
                p(img(rdz.url, src='%s' % rdz.url))
                
            #print rdz.url
            #if '.jpg' in rdz.url:
            #    img(rdz.urlz)
            #else:
            #    a(rdz.urlz)
            p(str(rdz.author))
            
            #li(img(i.lower(), src='%s' % i))

    with div():
        attr(cls='body')
        p('GetsDrawn is open source')
        a('http://github.com/wcmckee/wcmckee')

#print doc

# <codecell>

gtdrndic

# <codecell>

doc.render()

# <codecell>

indfil = ('/home/wcmckee/getsdrawndotcom/index.html')

# <codecell>

mkind = open(indfil, 'w')
mkind.write(str(doc))
mkind.close()

# <codecell>

#os.system('scp -r /home/wcmckee/getsdrawndotcom/ wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom')

# <codecell>

os.system('scp -r /home/wcmckee/getsdrawndotcom/index.html wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/index.html')

# <codecell>

os.system('scp -r /home/wcmckee/getsdrawndotcom/style.css wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/style.css')

# <codecell>


