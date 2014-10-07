# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Python script to download repos from github.
# It checked localfiles and skips downloading any repos that currently exsist. 
# Perform a git pull for each repo that exsists

# <codecell>

from github import Github

# <codecell>

import os
import getpass
from git import *
import git

# <codecell>

g = Github('wcmckee', 'cam123now!')

# <codecell>

grepo = g.search_users('wcmckee')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

# <codecell>

for gre in grepo:
    print gre.repos_url

# <codecell>

print gre.email

# <codecell>

grrep = gre.get_repos()

# <codecell>

replist =  list(grrep)

# <codecell>

repolisx = []

# <codecell>

for repoz in replist:
    print repoz.name
    repolisx.append(repoz.name)

# <codecell>

for repoit in repolisx:
    print repoit

# <codecell>

repolisx

# <codecell>

homlaz = ('/home/wcmckee/')

# <codecell>

os.chdir(homlaz)

# <codecell>

opgitp = open('gitp.txt', 'r')

# <codecell>

rpa = str(opgitp.read())

# <codecell>

rpa

# <codecell>

dirlis = os.listdir(homlaz)

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

merglis   

# <codecell>

for repoit in repolisx:
    print repoit
    git.Git().clone('https://github.com/wcmckee/' + repoit)

# <codecell>

wcmrepo = git.repository('/home/wcmckee/wcmkee')

# <codecell>

help('git')

# <codecell>


# <codecell>

import git

# <codecell>

from git import *
repo = Repo("/Users/mtrier/Development/git-python")

# <codecell>

git.Repository.clone('https://github.com/wcmckee/BeOk')

# <codecell>

git.repository.Repository.clone()

# <codecell>

(git.objects)

# <codecell>


