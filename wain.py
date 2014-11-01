# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Visitor Sign System
# 
# This script was created as an altenative to a printed spreadsheet that you use a physical pen to write - date, name, reason, time in, time out. 
# There is a comment book that this could be used to replace also. 
# Currently people write comments in pen on lined refil. Comments 
# The script is basic. It saves the time, date, name, reason, and added in comments as an html page and json object. Archieve of past logins are saved.
# It is split into two scripts. The first wain or whaxlu is used for the login. 
# The second script is whaiout which is the logout script. It takes the output of wain or whaxlu and appends logout data - time, date, and comment.

# <markdowncell>

# TODO
# 
# html page of page 100 logins/logouts - append all json as one html
# 
# graph of weekly/day hours and how they chage.
# 
# work out time between login and logout.
# 
# question that you comment on that includes the sketch daily reddit gets drawn. 
# 
# fake name encriputiom for kids
# 
# records time when child eats/drinks

# <codecell>

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <h2>visitor sign system</h2>
# 
# This is a python script used to sign in and signout, keeping track of hours and creating a more automative system.
# 
# Make sign in and out faster, easier to keep track of.
# 
# Never forget. 
# 
# Auto roll check. 
# 
# Two random hex codes for security and correct checking. Made use of tthese by using one as file name when saving.
# 
# Creates xls file with data, also uses sqlalchemy for databases, web server, html page: 
# input (or auto) name, reason, auto day/month/year hr/min - of signin.
# 
# when launched asked if you want to signin or signout. 
# 
# how i want this to run for william:
# 
# william arrives into whai. On his phone he runs the signin script. On signing out for the day the script is run onto final part, signout. asks for comment first then records time, and date. 
# 
# comment system. leave comment for staff, parent, tag staff, area, story, parent, child.
# 
# signout - enter code of session you want to signout. 
# 
# Screw the excel file, im just dealing with index page. i am saving achieve in posts folder under urandom 13 character code. 

# <codecell>

import os
import time
import dominate
import sys
from dominate.tags import *
import json

lasnam = raw_input('Last Name: ')
firnam = raw_input('First Name: ')
dopz = raw_input('dob: ')
mname = ('William Mckee')
ename = raw_input('Email: ')
signin = raw_input('Reason: ')

numroll = []

# <codecell>

for det in range(6):
    #print det
    numroll.append(det)

usecom = raw_input('Comments: ')



betdict = {'first': firnam}

# <codecell>

dayr = time.strftime("%d" + "-" + "%b" + "-" + "%Y")
hrmn = time.strftime("%H:%M:%S")

# <codecell>

betdict.update({'lastname': lasnam})
betdict.update({'reason': signin})
betdict.update({'signin-comment': usecom})
betdict.update({'signin-date': dayr})
betdict.update({'signin-hrmin': hrmn})

# <codecell>

betjsn = json.dumps(betdict)

# <codecell>

betjsn


doc = dominate.document(title='Visitor Sign Sheet')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(id='header').add(ol()):
        h1('Visitor Sign Sheet')
        for i in betdict.values():
            li(a(i))

    with div():
        attr(cls='body')
        p('last updated: ' + time.strftime("%H:%M"))
        p('Visitor Sign Sheet is open source')
        a('http://github.com/wcmckee/wcmckee', href='https://github.com/wcmckee/wcmckee')

#print doc

# <codecell>

savindex = open('/home/wcmckee/visignsys/index.html', 'w')

# <codecell>

savindex.write(str(doc))
savindex.close()

# <codecell>
ixran = os.urandom(16)
ixtwe = ixran[0:16]

# <codecell>

savpos = open('/home/wcmckee/visignsys/posts/' + ixtwe + '.html', 'w')
savpos.write(str(doc))
savpos.close()

# <codecell>

savpos = open('/home/wcmckee/visignsys/posts/' + ixtwe + '.json', 'w')
savpos.write(str(betjsn))
savpos.close()

# <codecell>

#savpos = open('/home/wcmckee/visignsys/index.meta', 'w')
#savpos.write(str(wsdict.keys()))
#savpos.close()

# <codecell>

savpos = open('/home/wcmckee/visignsys/index.json', 'a')
savpos.write(str(betjsn))
savpos.close()

print ('sign in complete')

# <codecell>


