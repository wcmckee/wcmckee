# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Reddit Gets Drawn Snatch Script
# 
# test

# <codecell>

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# RedditGetsDrawn Snatch
# 
# This is a Python script that takes data from reddit and posts it to another subreddit. It also creates a html file with the images embed into. The images are the most recent 25 on r/redditgetsdrawn.
# 

# <markdowncell>

# TODO
# 
# submit art to users via website
# 
# fix image sizes (need to scale down to 550px)
# 
# Save to server rather than imgur
# 
# Archieve, snapshots of rgd
# 
# more artcontrol
# 
# itwillbemine comments to html - currently being saved in contact 
# 
# work on css, div up page, title, side, body, fo
# update twitter with ONE IMAGE and announce that the list has been updated.
# 
# write blog post and submits to artcontroldrawsyou/blog 
# 
# gets sticked post on reddit
# 
# delete about/contact page and have on all same page. can still have link to blog. 
# about 
# contact etc... along the top.
# other sections
# 
# post images to blog for archieve - save body to wcmckee.com/blog - md format?
# 
# nikola install - build site.
# 
# cronjob to update site ever ?? hours? 4?
# 
# photos section: latest 25 photos submitted to redditgetsdrawn.
# art section: latest 25 art submitted to redditgetsdrawn. 

# <codecell>

import os
import random
import requests
from bs4 import BeautifulSoup
import re
import json
import time
import praw
import dominate
from dominate.tags import *
from time import gmtime, strftime

# <codecell>

os.chdir('/home/wcmckee/artcontroldrawsyou')

# <codecell>

r = praw.Reddit(user_agent='rgdsnatch')

# <codecell>

#r.login('artcontrol', 'taylor123vag!')

# <codecell>

rd = r.get_subreddit('redditgetsdrawn')

# <codecell>

subz = rd.get_hot().next()
istit = (subz.title)
istxt = (subz.selftext_html)
istick = (subz.stickied)

# <codecell>

istit

# <codecell>

istxt

# <codecell>

rdnewz = rd.get_new()

# <codecell>

rdnew = []

# <codecell>

rdnew

# <codecell>

reddraw = praw.Reddit(user_agent='rgdsnatch')

# <codecell>

getrddraw = reddraw.get_subreddit('redditgetsdrawn')

# <codecell>

subz = getrddraw.get_new()

# <codecell>

rdnew = []

# <codecell>

rdnewz = getrddraw.get_new()

# <codecell>

rdnew = []

# <codecell>

rdnew

# <codecell>

for uz in rdnewz:
    #print uz
    rdnew.append(uz)

# <codecell>

datelis = []
refdic = {}

# <codecell>

for rdz in rdnew:
    print rdz.name
    print rdz.title
    print rdz.url
    print rdz.author
    print rdz.secure_media
    print rdz.num_comments
    datelis.append(rdz.title)
    datelis.append(rdz.url)
    datelis.append(rdz.author)

# <codecell>

import dominate
from dominate.tags import *

doc = dominate.document(title='RedditGetsDrawn Recent Reference')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')
    
    with div():
        attr(cls='header')
        h1('RedditGetsDrawn Recent Reference')
        p('updated ', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))

    
    

with doc:
    with div(id='body').add(ol()):
        for rdz in rdnew:
            h1(rdz.title)
            a(rdz.url)
            if '.jpg' or '.png' in rdz.url:
                print rdz.url
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
        p('RGDRecentReference is open source')
        a('http://github.com/wcmckee/wcmckee')

print doc

# <codecell>

rgdir = ('/home/wcmckee/rgdrecentReference/')

# <codecell>

os.chdir(rgdir)

# <codecell>

mkindex = open('index.html', 'w')
mkindex.write(str(doc))
mkindex.close()

# <codecell>

print str(doc)

# <codecell>

print strftime("%a, %d %b %Y %H:%M:%S +0000")

# <codecell>

strftime("%d" + "/" + "%M" + "/" + "%Y")

# <codecell>

time.localtime()

# <codecell>

time.asctime()

# <codecell>

#os.chdir('/home/wcmckee/brobeur-blog-post/')

# <codecell>

#brobeind = open('índex.html', 'r')

# <codecell>

#brotest = open('índex.html', 'r')
#brotest.read()

