# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <h1>GetsDrawn DotCom</h1>

# <markdowncell>

# This is a python script to generate the website GetsDrawn. It takes data from RedditGetsDrawn and makes something awesome.
# 
# The script has envolved and been rewritten several times. 

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

# <codecell>

gtsdrndir = ('/home/wcmckee/getsdrawndotcom')

# <codecell>

os.chdir(gtsdrndir)

# <codecell>

r = praw.Reddit(user_agent='getsdrawndotcom')

# <codecell>

getnewr = r.get_subreddit('redditgetsdrawn')

# <codecell>

rdnew = getnewr.get_new()

# <codecell>

lisrgc = []

# <codecell>

for uz in rdnew:
    print uz
    lisrgc.append(uz)

# <codecell>

for lizq in lisrgc:
    print lizq

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

gtdrndic

# <codecell>


