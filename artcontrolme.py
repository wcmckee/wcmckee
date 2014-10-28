# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# **artcontrolme**
# 
# 
# Python script to deal with exported artcontrolme static files. The files are located at https://github.com/artcontrol/artcontrolme. '.wp' files that contain HTML of posts. '.meta' files contain name, permalink, date, cat, tags, id.
# 

# <markdowncell>

# **TODO**
# 
# sort dict of permalink and time published.
# render index.html that shows recent 10 works

# <codecell>

import requests
from bs4 import BeautifulSoup
import os
import json

# <codecell>

#artcpost = ('/home/wcmckee/artcontrolme/posts')

# <codecell>

postsdir = (u'/home/wcmckee/artcontrolme/posts')

# <codecell>

os.chdir(postsdir)

# <codecell>

alfilz = []

# <codecell>

for filz in os.listdir(postsdir):
    print filz
    alfilz.append(filz)

# <codecell>

alfilz

# <codecell>

for bleh in alfilz:
    if '.wp' in bleh:
        print bleh
    

# <codecell>

#file = open('alcemy-landscape.wp', 'r')

#print file.read()

# <codecell>

lisblog = []
metablog = []
dictblog = {}
finlis = []

# <codecell>

teop = open('test.txt', 'w')

# <codecell>

#f=open('filename')
#lines=f.readlines()
#print lines[26]
#print lines[30]

# <codecell>

for bleh in alfilz:
    if '.meta' in bleh:
        #print bleh
        
        #filez = open('alcemy-landscape.wp', "r")
        #filez.read
        #filez.close()
        file = open(bleh, 'r')
        metaf = file.readlines()

        #print file.read()
        #metablog.append(file.readline())
        #metablog.append(file.readline())
        #metablog.append(file.readline())
        #print metaf[2]
        #adrdir = {metaf[0]: metaf[2]}
        #chzdir = ({'test': 'test'})
        #chzdir.update({metaf[2]: metaf[1]})
        chzdir = {metaf[2].rstrip(): metaf[1].rstrip()}#, file.readline()}
        
        #print chzdir
        finlis.append(chzdir)
        teop.write(file.read())

# <codecell>

chzdir

# <codecell>

chzdir.items()

# <codecell>

tuplis = []

# <codecell>

derplis = []

# <codecell>

import collections

# <codecell>

dez = collections.OrderedDict()

# <codecell>

metaf

# <codecell>

cherdict = {'test':'test'}

# <codecell>

jslis = []

# <codecell>

for bleh in alfilz:
    if '.meta' in bleh:
        #print bleh
        
        #filez = open('alcemy-landscape.wp', "r")
        #filez.read
        #filez.close()
        file = open(bleh, 'r')
        metaf = file.readlines()

        #print file.read()
        #metablog.append(file.readline())
        #metablog.append(file.readline())
        #metablog.append(file.readline())
        #print metaf[2]
        #adrdir = {metaf[0]: metaf[2]}
        chzdir = ({'name': metaf[0].rstrip()})#, file.readline()}
        cherdict.update({metaf[2].rstrip(): metaf[1].rstrip()})
        cherdict.update({metaf[1]: metaf[3].rstrip()})
        chzdir.update({'title': metaf[1].rstrip()})
        chzdir.update({'date': metaf[2].rstrip()})
        chzdir.update({'tags': metaf[3].rstrip()})
        print chzdir
        finlis.append(chzdir)
        cherjson = json.dumps(chzdir)
        jslis.append(cherjson)
        teop.write(file.read())

# <codecell>

jslis

# <codecell>

cherjson = json.dumps(chzdir)

# <codecell>

cherjson

# <codecell>

savus = open('/home/wcmckee/visignsys/artcontrol.json', 'w')
savus.write(str(jslis))
savus.close()

# <codecell>

chzdir.items()

# <codecell>

chval = chzdir.values()

# <codecell>

itm = len(chval)

# <codecell>

itm

# <codecell>

for chre in range(itm):
    print chval[chre]

# <codecell>

for chz in chzdir:
    print chz

# <codecell>

for fin in finlis:
    #print sorted(fin.keys())
    for fez in fin.keys():
        #sorted(fez)
        print (fez)
        derplis.append(fez)
    tuplis.append(fin.keys())
    

# <codecell>

sordep = sorted(derplis)

# <markdowncell>

# I want to add the correct permalink to the sorted list of publish dates.
# 
# Take two dict. 
# dict1 is original sort time : permalink
# dict2 is sorted time : NEED TO ADD CORRECT PERMALINK HERE
# 
# look at the time in first dict from dict2 and add permalink as its value.
# 
# if numba ('2011-07etc') in timlist:
#  get its value (permalink). write this as value for dict2.
# 
# Need to add html content, tags, and cats once this is sorted. should be easy since accessing it with var[num of line]

# <codecell>

sordep

# <codecell>

metablog

# <codecell>

for neta in metablog:
    print neta

# <codecell>

for bleh in alfilz:
    if '.wp' in bleh:
        #print bleh
        
        #filez = open('alcemy-landscape.wp', "r")
        #filez.read
        #filez.close()
        file = open(bleh, 'r')

        #print file.read()
        lisblog.append(file.read())
        teop.write(file.read())

# <codecell>

len(lisblog)

# <codecell>

filez = open('alcemy-landscape.wp', "r")
filez.read()
filez.close()

# <codecell>

import dominate
from dominate.tags import *

doc = dominate.document(title='artcontrolme')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')
    h1('artcontrolme')
    h3('The Art Of WCMCKEE')

with doc:
    with div(id='header').add(ol()):
        for chre in range(itm):
            p(chval[chre])

    #with div():
     #   attr(cls='body')
      #  p('Lorem ipsum..')

print doc

# <codecell>


# <codecell>


# <codecell>


