# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <h1>Fairfield Login</h1>
# 
# This is a script that deals with managing a internet cafe.
# 
# I need to make it easy to create users, assign time to users, remove time, ban users, reset passwords, give time to a group of users (users who read, help garden etc.
# 
# Manages when computers are turned on and off.
# Computers turn on at 7:50am everymorning and perform a update, sync from origin.
# Allows Public login, allowed to login as users.
# At 2.25 computers reset and public is disabled. 
# 
# Give 45 mins to everybody. Add for bonus.
# 
# 
# All the ipynb files in a folder. 
# script opens ipynb filename striping the .ipynb add .meta instead. Opens the .meta and saves filename title, slug, time year-month-day-hour-min.
# 
# 

# <codecell>

import os

# <codecell>

os.getuid()

# <codecell>

os.getgroups()

# <codecell>

#os.system('rsync -azP /home/wcmckee/motion/ wcmckee@getsdrawn.com:/home/wcmckee/motion/')

# <codecell>

opfair = os.listdir('/home/wcmckee/ipy/wcmckee-ipython/posts')

# <codecell>

namfil = []

# <codecell>

opfair

# <markdowncell>

# If space in the filename then change to - for url-friendly.

# <codecell>

opsrip = []

# <codecell>

os.system('rm -rf /home/wcmckee/fairfieldcode/posts/*.meta')

# <codecell>

spliz = []

# <codecell>

saost = os.stat('/home/wcmckee/fairfieldcode/posts')

# <codecell>

saost.st_mtime

# <codecell>

saost.st_mtime

# <codecell>

saost.st_size

# <codecell>

saost.st_uid

# <codecell>

saost.st_atime

# <codecell>

saost.st_atime

# <codecell>

oswa = os.walk('/home/wcmckee')

# <codecell>

os.sysconf('SC_2_CHAR_TERM')

# <codecell>

os.sysconf_names

# <codecell>

os.listdir('/home/wcmckee/fairfieldcode/posts/')

for ipos in os.listdir('/home/wcmckee/fairfieldcode/posts/'):
    print ipos
    
    spliz.append([os.path.splitext(' ')[0] for x in ipos])

# <codecell>

spliz

# <codecell>

for opfa in opfair:
    #opfa.replace(" ", "")
    print opfa
    [os.path.splitext(x)[0] for x in a]
    opsrip.append(opfa.strip('.ipynb'))
    print opfa.strip('.ipynb')
   # if (' ') in opfa.strip('.ipynb'):
    #    print opfa.strip('.ipython')

# <codecell>

os.chdir('/home/wcmckee/fairfieldcode/posts/')

# <codecell>

import time

# <codecell>

endate = time.strftime("%d" + "-" + "%b" + "-" + "%Y" + "-")
          
entim = time.strftime("%H:%M")

# <codecell>

endate

# <codecell>

for opfilz in opsrip:
    print opfilz
    with open(str(opfilz) + '.meta', "w") as f:
            rstrin = opfilz.encode('ascii', 'ignore').decode('ascii')
            #print matdict
            #metadict = dict()
            #for lisz in lisrgc:
            #    metadict.update({'up': lisz.ups})
            #    metadict.update({'down': lisz.downs})
            #    metadict.update({'title': lisz.title})
            #    metadict.update({'created': lisz.created})
            f.write(rstrin.strip(' ') + '\n' + rstrin + '\n' + endate + entim)

# <codecell>

import nikola

# <codecell>

os.chdir('/home/wcmckee/fairfieldcode/')

# <codecell>

os.system('nikola build')

# <codecell>

os.system('rsync -azP /home/wcmckee/fairfieldcode wcmckee@wcmckee.com:/home/wcmckee/fairfieldcode/')

# <codecell>

opconf = open('/home/wcmckee/fairfieldcode/conf.py', 'r')

# <codecell>

opconf.read()

# <codecell>


# <codecell>


