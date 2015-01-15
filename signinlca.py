# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# signinlca
# 
# script to signin for volunteers at lca2015

# <codecell>

import os
import time
import json
import getpass

# <codecell>

def returndate():
    return time.strftime(("%d" + "-" + "%b" + "-" + "%Y"))

def returntime():
    return time.strftime("%H:%M:%S")

# <codecell>

firnam = raw_input('first name: ')
lasnam = raw_input('last name: ')
tshir = raw_input('tshirt size: ')
cofvol = raw_input('coffee volc: ')
comen = raw_input('comments: ')

# <codecell>

betdict = dict()

# <codecell>

betdict.update({'first-name' : firnam})
betdict.update({'last-name' : lasnam})
betdict.update({'signin-date' : returndate()})
betdict.update({'signin-hrmin' : returntime()})
betdict.update({'tshirt-size' : tshir})
betdict.update({'coffees' : int(cofvol)})
betdict.update({'comments:' : comen})

# <codecell>

betdict

# <codecell>

convj = json.dumps(betdict)

# <codecell>

convj

# <codecell>

puser = getpass.getuser()

# <codecell>


# <codecell>

signpath = ('/home/' + puser + '/signinlca')

# <codecell>

if os.path.isdir(signpath) == True:
    print 'Path is there'
else:
    print 'Path not there'
    os.mkdir(signpath)

# <codecell>

os.chdir(signpath)

# <codecell>

opday = open(str(firnam + lasnam) + '.json', 'a')

# <codecell>

opday.write(convj)

# <codecell>


