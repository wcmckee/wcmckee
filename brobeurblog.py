# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# BroBeur Studios Blog
# 
# This is similar to the artcontrolme script but it deals with BroBeur Studios posts

# <codecell>

import random

# <codecell>

import os

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
    chzdir = {metaf[2]: metaf[1]}#, file.readline()}
    print chzdir
    alldic.append(chzdir)

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

randiz = alldic[ranit]

# <codecell>

randiz

# <codecell>

razdiz = randiz.keys()

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

from bs4 import BeautifulSoup
soup = BeautifulSoup(blogread)

print(soup.prettify())

# <codecell>

soup.findAll('html')

# <codecell>

import dominate
from dominate.tags import *

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

print doc

# <codecell>

brobeurblogpz = ('/home/wcmckee/brobeur-blog-post')

# <codecell>

os.chdir(brobeurblogpz)

# <codecell>

wriind = open('index.html', 'w')

# <codecell>

wriind.write(str(doc))

# <codecell>

wriind.close()

# <codecell>


