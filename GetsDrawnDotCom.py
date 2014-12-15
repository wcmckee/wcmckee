
# coding: utf-8

# <h1>GetsDrawn DotCom</h1>

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




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

# In[70]:

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


# In[71]:

gtsdrndir = ('/home/wcmckee/getsdrawndotcom')


# In[72]:

os.chdir(gtsdrndir)


# In[73]:

r = praw.Reddit(user_agent='getsdrawndotcom')


# In[74]:

#getmin = r.get_redditor('itwillbemine')


# In[75]:

#mincom = getmin.get_comments()


# In[76]:

#engine = pyttsx.init()

#engine.say('The quick brown fox jumped over the lazy dog.')
#engine.runAndWait()


# In[77]:

#shtweet = []


# In[78]:

#for mi in mincom:
#    print mi
#    shtweet.append(mi)


# In[79]:

bodycom = []
bodyicv = dict()


# In[80]:

#beginz = pyttsx.init()


# In[81]:

#for shtz in shtweet:
#    print shtz.downs
#    print shtz.ups
#    print shtz.body
#    print shtz.replies
    #beginz.say(shtz.author)
    #beginz.say(shtz.body)
    #beginz.runAndWait()
    
#    bodycom.append(shtz.body)
    #bodyic


# In[82]:

#bodycom 


# In[83]:

getnewr = r.get_subreddit('redditgetsdrawn')


# In[84]:

rdnew = getnewr.get_new()


# In[85]:

lisrgc = []


# In[86]:

for uz in rdnew:
    #print uz
    lisrgc.append(uz)


# In[87]:

gtdrndic = dict()


# In[88]:

for lisr in lisrgc:
    #print lisr.url
    #print lisr.title
    #print lisr.author
    #print lisr.comments
    gtdrndic.update({'title': lisr.title})
    print lisr.json_dict
    


# In[89]:

opsinz = open('/home/wcmckee/visignsys/index.meta', 'r')
panz = opsinz.read()


# In[90]:

#panz()


# In[91]:

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


# In[92]:

gtdrndic


# In[93]:

doc.render()


# In[94]:

indfil = ('/home/wcmckee/getsdrawndotcom/index.html')


# In[95]:

mkind = open(indfil, 'w')
mkind.write(str(doc))
mkind.close()


# In[96]:

#os.system('scp -r /home/wcmckee/getsdrawndotcom/ wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom')


# In[97]:

os.system('scp -r /home/wcmckee/getsdrawndotcom/index.html wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/index.html')


# In[ ]:

os.system('scp -r /home/wcmckee/getsdrawndotcom/style.css wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/style.css')


# In[ ]:



