# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <h1>Reddit Gets Drawn Snatch Script</h1>
# 
# Creates the website redditgetsdrawnrecentreference. It contains the 25 most recent posts on r/redditgetsdrawn. title, image url, and username
# 
# TODO:
# Contains artwork replies to each thread
# 
# This is a Python script that takes data from reddit and posts it to another subreddit. It also creates a html file with the images embed into. The images are the most recent 25 on r/redditgetsdrawn.
# 
# The script returns the comments from the most recent 25 posts along with the comments of comments.
# 
# Pandas is used to append everything into a series and DataFrame. 
# The pandas allows youto easily append these together. 
# 
# get all artwork and append into reference image -> 
# artwork. 
# 
# Generate sites again.
# 

# <markdowncell>

# RedditGetsDrawn Snatch
#  
# This is a Python script that takes data from reddit and posts it to another subreddit. It also creates a html file with the images embed into. The images are the most recent 25 on r/redditgetsdrawn.
#  
# 
# <markdowncell>
# 
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
# 
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
# 
# cleanup code 
# 
# import pandas into it and removed things i dont need like dominate

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
#import nose
#import unittest
import numpy as np
import pandas as pd
from pandas import *

# <codecell>

chdira = ('/home/wcmckee/artcontroldrawsyou')
os.chdir(chdira)

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

rdnewz = rd.get_new()

rdnew = []

# <codecell>

reddraw = praw.Reddit(user_agent='rgdsnatch')

# <codecell>

getrddraw = reddraw.get_subreddit('redditgetsdrawn')

# <codecell>

decict = dict()

# <codecell>

subz = getrddraw.get_new()

# <codecell>

#class TestRedditFunction(unittest.TestCase):
    
#    def setUp(self):
#        self.seq = reddraw.get_subreddit('redditgetsdrawn')
        
#    def testredit(self):
#        drawnew('redditgetsdrawn') 

# <codecell>

def drawnew(subred):
    getrdraw = reddraw.get_subreddit(subred)
    return getrdraw

def apred(deciz):
    
    return (deciz)

# <codecell>

apred('omg')

# <codecell>

rdrws = drawnew('redditgetsdrawn')

# <codecell>

rtohr = rdrws.get_controversial_from_all()

# <codecell>

for imgz in rtohr:
    #print imgz.selftext
    print imgz.num_comments

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
rgdef = dict()
comdefz = []

# <codecell>

for rdz in rdnew:
    print rdz.name
    print rdz.title
    print rdz.url
    print rdz.author
    print rdz.secure_media
    print rdz.num_comments
    print rdz.comments
    comdefz.append(rdz.comments)
    datelis.append(rdz.title)
    datelis.append(rdz.url)
    datelis.append(rdz.author)
    comdict = {'comtxt':rdz.comments}
    rgdef.update({rdz.author: rdz.url})
    pandic = DataFrame(rdz.json_dict)
    decict.update({'url':rdz.url})
    decict.update({'title':rdz.title})
    decict.update({'ups': rdz.ups})
    decict.update({'downs': rdz.downs})

# <codecell>

decict

# <codecell>

pandic

# <codecell>

comdict

# <codecell>

comply = []

# <codecell>

fddict = dict()

# <codecell>

fdz.body

# <codecell>

for comaq in comdefz:
    for fdz in comaq:
        print fdz
        print fdz.author
        print fdz.created_utc
        print fdz.replies
        fddict.update({'combody': fdz.body})
        fddict.update({'comauthor': fdz.author})
        fddict.update({'comup': fdz.ups})
        fddict.update({'comdown': fdz.downs})
        
        comply.append(fdz.replies)
        decict.update({'created':fdz.created_utc})
        decict.update({'author': fdz.author})
        decict.update({'body':fdz.body})
        decict.update({'replies':fdz.replies})

# <codecell>

decict

# <codecell>

fddict

# <codecell>

qwedict = decict.items() + fddict.items()

# <codecell>

alldixz = dict()

# <codecell>

for qwpz in qwedict:
    print qwpz
    alldixz.update({qwpz: 'test'})

# <codecell>

alldixz

# <codecell>

qwedict

# <codecell>

for coaz in comply:
    print coaz
    for coa in coaz:
        print coa.body
        print coa.author

# <codecell>

serz = Series(fddict)

# <codecell>

fddict

# <codecell>

fddict.keys()

# <codecell>

def extractlinks(html):
    soup = BeautifulSoup(html)
    anchors = soup.findAll('a')
    links = []
    for a in anchors:
        links.append(a['href'])
    return links

# <codecell>

cydict = fddict.values()

# <codecell>

for itz in cydict:
    print itz   

# <codecell>

chedict = {'blah': 'testing'}

# <codecell>

#fixurl = BeautifulSoup(fddict.values())

# <codecell>

for coma in comdefz:
    #print coma
    #chedict.update({'first': coma})
    for co in coma:
        print co
        chedict.update({co.author: co.body})

# <codecell>

getsdrdir = ('/home/wcmckee/getsdrawndotcom/')

# <codecell>

os.listdir(getsdrdir)

# <codecell>

chedict

# <codecell>

#jsdum = json.loads(chedict)

# <codecell>

rcoms = chedict.keys()
rvals = chedict.values()
imcom = []

# <codecell>

for rvs in rvals:
    print rvs
    if '.jpg' or '.png' in rvs:
        imcom.append(rvs)
        

# <codecell>

imcom

# <codecell>

#fuldoc = doc.render()

# <codecell>


# <codecell>

doc = dominate.document(title='Dominate your HTML')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(id='header').add(ol()):
        for imz in imcom:
            #print imz
            p(imz)

    #with div():
     #   attr(cls='body')
     #   p('Lorem ipsum..')

#print doc

# <codecell>

for docin in doc.head.children:
    print docin

# <codecell>

for pain in docin.parent.children:
    print pain

# <codecell>

doc.body.parent.children

# <codecell>


# <codecell>

#soup = BeautifulSoup(doc)

#print(soup.prettify())

# <codecell>

#extractlinks()

# <codecell>

#for imc in imcom:
#    print imc

# <codecell>

#doc.body

# <codecell>


# <codecell>

#doc.render()

# <codecell>

#for dicaz in doc.children:
#    print dicaz

# <codecell>


# <codecell>

#for imz in imcom:
    
#    print imz

# <codecell>

#for rez in rcoms:
#    print rez
    

# <codecell>


# <codecell>

#for rgt in rgdef.values():
#    if '.jpg' in rgt:
#        print rgt

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

#print doc

# <codecell>

rgdir = ('/home/wcmckee/rgdrecentReference/')

# <codecell>

doc.render()

# <codecell>

os.chdir(rgdir)

# <codecell>

mkindex = open('index.html', 'w')
mkindex.write(str(doc))
mkindex.close()

# <codecell>

#print str(doc)

# <codecell>

print strftime("%a, %d %b %Y %H:%M:%S +0000")

# <codecell>

savedate = strftime("%d" + "-" + "%m" + "-" + "%Y" + "-" + "%H")

# <codecell>

def timeret():
    return strftime("%d" + "-" + "%m" + "-" + "%Y" + "-" + "%H")

def givmd():
    return str(savedate + '.md')

def givdic():
    return rgdir.replace('/', '-')

# <codecell>

givdic()

# <rawcell>

# timeret()

# <codecell>

givmd()

# <codecell>

savedate

# <codecell>

deepone = str(savedate + '.md')

# <codecell>

deepone

# <codecell>

#os.chdir('/home/wcmckee/brobeur-blog-post/')

# <codecell>

#brobeind = open('índex.html', 'r')

# <codecell>

#brotest = open('índex.html', 'r')
#brotest.read()

# <codecell>

redposts = ('/home/wcmckee/rgdrecentReference/posts/pandas')

# <codecell>

os.chdir(redposts)

# <codecell>

time.asctime()

# <codecell>

savinx = open(str(deepone), 'w')

# <codecell>

savinx.write(str(rgdef))

# <codecell>

savinx.close()

# <codecell>

deepone

# <codecell>

decict

# <codecell>

decict.update({'datehour': givmd()})

# <codecell>

depan = Series(decict)

# <codecell>

fepan = Series(fddict)

# <codecell>

mepan = (fepan)+(depan)

# <codecell>

depan

# <codecell>

feram = pd.DataFrame(fepan)

# <codecell>

fepan

# <codecell>

feram

# <codecell>

mepan

# <codecell>

defed = DataFrame(depan)

# <codecell>

#defed.append(fepan)

# <codecell>

depan

# <codecell>

fepan

# <codecell>

mergz = depan.append(fepan)

# <codecell>

mergz

# <codecell>


# <codecell>

defed

# <codecell>

defhtml = defed.to_html()

# <codecell>

wrhtm = open('index.html', 'w')
wrhtm.write(defhtml)
wrhtm.close()

# <codecell>


# <codecell>


# <codecell>


