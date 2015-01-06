# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <h3>pygitx</h3>
# 
# Python script to download repos from github.
# It checked localfiles and skips downloading any repos that currently exsist. 
# Perform a git pull for each repo that exsists.
# 
# Look at the ipython notebook files (ipynb) inside each repo and generate a nikola site with it. 
# Write out .meta files for each notebook. 
# 
# title
# 
# url-friendly
# 
# year/month/day hr/min
# 
# tags: redditgetsdrawn, modules used?
# 
# cats: lang? doc, novel
# 
# 
# Site name repo name
# 

# <codecell>

from github import Github

# <codecell>

import os
import getpass
from git import *
import git
import datetime

# <codecell>

p = open('/home/wcmckee/ps.txt', 'r')

# <codecell>

#str(p.read())

# <codecell>

pred = str(p.read())

# <codecell>

pstrip = pred.strip('\n')

# <codecell>

g = Github('wcmckee', pstrip)

# <codecell>

grepo = g.search_users('wcmckee')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

# <codecell>

repoev = []

# <codecell>

for gre in grepo:
    print gre.repos_url
    print gre.get_public_events
    print gre.get_repo('wcmckee')
    repoev.append(gre.get_repo('wcmckee'))

# <codecell>

for rep in repoev:
    print rep

# <codecell>

for repoe in repoev:
    print repoe

# <codecell>

print gre.email

# <codecell>

grrep = gre.get_repos()

# <codecell>

replist =  list(grrep)

# <codecell>

repolisx = []
repocom = []
repocont = []

# <codecell>

ophom = ('/home/wcmckee/ipy/wcmckee-ipython/posts/')

# <codecell>

os.chdir('/home/wcmckee/ipy/wcmckee-ipython/posts')

# <codecell>

for repoz in replist:
    print repoz.name
    with open(str(repoz.name) + '.meta', "w") as f:
            repna = repoz.name.encode('ascii', 'ignore').decode('ascii')
            f.write(repoz.name + '\n' + repoz.name + '\n' + str(repoz.updated_at))
    #repolisx.append(repoz.name)
    #print repoz.size
    print repoz.updated_at
    #print repoz.get_contents
    print (repoz.get_commits())
    repocont.append(repoz.get_contents)
  #  repocom.append(repoz.get_commits)

# <codecell>


# <codecell>

for repoc in repocont:
    print repoc
    gre.get_repo()
    

# <codecell>

#for repz in repocom:
#    print repoz.ssh_url

# <codecell>

for repoit in repolisx:
    print repoit

# <codecell>

repolisx

# <codecell>

homlaz = ('/var/host/media/removable/USB Drive/')

# <codecell>

#opgitp = open('gitp.txt', 'r')

# <codecell>

#os.mkdir('wcmckee-git')

# <codecell>

gitdir = (homlaz + 'wcmckee-git')

# <codecell>

#_LOKDD

# <codecell>

#rpa

# <codecell>

os.chdir(gitdir)

# <codecell>

dirlis = os.listdir(gitdir)

# <codecell>

dirme = set(dirlis) - set(repolisx)

# <codecell>

dirout = set(repolisx) - set(dirlis)

# <codecell>

for dirz in dirout:
    print dirz

# <codecell>

dirme

# <codecell>

merglis = set(dirlis) & set(repolisx)

# <codecell>

pwd

# <codecell>

for repoit in repolisx:
    print repoit
    os.system('git clone https://github.com/wcmckee/' + repoit)
    #git.Git().clone('https://github.com/wcmckee/' + repoit)

