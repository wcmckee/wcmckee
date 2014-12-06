# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# BroBeur Studios Blog
# 
# This is similar to the artcontrolme script but it deals with BroBeur Studios posts.
# It takes a folder of .meta and .wp/md/html and mashes it together as a json object. 
# It also outputs a html file with a random post, and all posts.

# <markdowncell>

# TODO
# 
# deal with images.
# need bigger hard drive on local dev system (currently pi running debian)
# 
# combine brobeur, artcontrolme, and freshfigure.me/art into one site. Do this by merging all posts and images. 
# 

# <codecell>

import dominate
from dominate.tags import *
import random
import os
import json

# <codecell>


# <codecell>

bropo = ('/home/wcmckee/brobeur-web/posts')

# <codecell>

os.chdir(bropo)

# <codecell>

wplis = []

# <codecell>

for fil in os.listdir(bropo):
    print fil
    wplis.append(fil)

# <codecell>

metlis = []

# <codecell>

for wp in wplis:
    if '.meta' in wp:
        metlis.append(wp)

# <codecell>

alldic = []

# <codecell>

for mea in metlis:
    file = open(mea, 'r')
    metaf = file.readlines()
    chzdir = ({'name': metaf[0].rstrip()})#, file.readline()}
    chzdir.update({'title': metaf[1].rstrip()})
    chzdir.update({'date': metaf[2].rstrip()})
    chzdir.update({'tags': metaf[3].rstrip()})
    print chzdir
    alldic.append(chzdir)

# <codecell>

alldic

# <codecell>

dicjsn = json.dumps(alldic)

# <codecell>

savdjsn = open('/home/wcmckee/visignsys/brobeur.json', 'w')
savdjsn.write(dicjsn)
savdjsn.close()

# <codecell>

for cha in chzdir:
    print cha

# <codecell>

chzdir

# <codecell>

for al in alldic:
    print al

# <codecell>

tiran = len(alldic)

# <codecell>

ranit = random.randint(0, tiran)

# <codecell>

ranit

# <codecell>

#from random import shuffle
#x = [[i] for i in alldic:
#    random.shuffle(x)

# <codecell>

from random import shuffle

# <codecell>

shuffle(alldic)

# <codecell>

alldic

# <codecell>

betjsn = json.dumps(alldic)

# <codecell>

betjsn

# <codecell>

randiz = alldic[ranit]

# <codecell>

randiz

# <codecell>

razdiz = randiz.values()

# <codecell>

razdiz

# <codecell>

randaz = randiz.values()

# <codecell>

for itez in randaz:
    print itez + '.wp'
    str2 = itez.replace("\n", "")
    tafilz = str2 + '.wp'

# <codecell>

tafilz

# <codecell>

bldat = open((tafilz), 'r')

# <codecell>

blogread = bldat.read()

# <codecell>

blogwra = blogread.upper()

# <codecell>

blogstr = str(blogwra)

# <codecell>

blogstr

# <codecell>

blogread

# <codecell>

ixran = os.urandom(128).encode('hex')

# <codecell>

randiz

# <codecell>

randiz.update({'text': blogread})

# <codecell>

randiz['title']

# <codecell>

lendiz = len(randiz)

# <codecell>

def bugsearch():
    for bugz in range(lendiz):
        return (randiz[bugz])

# <codecell>

for ranv in randiz.values():
    print ranv

# <codecell>

from bs4 import BeautifulSoup
soup = BeautifulSoup(blogread)

print(soup.prettify())

# <codecell>

soup.findAll('html')

# <codecell>

doc = dominate.document(title='BroBeur Blog Post')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(id='header').add(ol()):
        for i in alldic[1]:
            li(a(i.title(), href='/%s.html' % i))

    with div():
        attr(cls='body')
        p(razdiz)
        h1(randaz)
        p(blogread)

#print doc

# <codecell>

brobeurblogpz = ('/home/wcmckee/brobeur-blog-post')

# <codecell>

os.chdir(brobeurblogpz)

# <codecell>

wriind = open('index.html', 'w')

# <codecell>

jsnd = open('index.json', 'w')

jsnd.write(str(betjsn))

# <codecell>

jsnd.close()

# <codecell>

wriind.write(str(doc))

# <codecell>

wriind.close()

# <codecell>


# <codecell>


