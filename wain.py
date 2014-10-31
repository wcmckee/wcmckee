# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

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
#from sqlalchemy import Column, ForeignKey, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
#from sqlalchemy import create_engine

# <codecell>

lasnam = raw_input('Last Name: ')
firnam = raw_input('First Name: ')
dopz = raw_input('dob: ')
mname = ('William Mckee')
ename = raw_input('Email: ')
signin = raw_input('Reason: ')

# <codecell>

rawdets = raw_input('Enter keys: ')

# <codecell>

numroll = []

# <codecell>

for det in range(6):
    #print det
    numroll.append(det)
    #ws.write(0, det, )

# <codecell>

#for rad in rawdets:
 #   print rad
    #print len(rad)
#    print rad.upper()
    #range(20)

# <codecell>

#ws.write(0, 0, 'In Date')
#ws.write(0, 1, 'In Time')
#ws.write(0, 2, 'In Code')
#ws.write(0, 3, 'Name')
#ws.write(0, 4, 'Reason')
#ws.write(0, 5, 'Out Date')
#ws.write(0, 6, 'Out Time')
#ws.write(0, 7, 'Out Code')

# <codecell>

#strftime is %d (day), 

#ws.write(1, 0, time.strftime("%d" + "-" + "%b" + "-" + "%Y"))

#ws.write(1, 1, time.strftime("%H:%M"))

# <codecell>

#getname = raw_input('Name: ')
#getreason = raw_input('Reason: ')

# <codecell>

#ws.write(1, 2, exran)

# <codecell>

#ws.write(1, 3, mname)

# <codecell>

#ws.write(1, 4, signin)

# <codecell>

#wb.save('/home/wcmckee/whai/' + xlvs)
#wb.save('/home/wcmckee/whai/index.xls')

# <codecell>

usecom = raw_input('Comments: ')

# <codecell>

#wsdict = {mname: 'test'}

# <codecell>

betdict = {'firstname': firnam}

# <codecell>

dayr = time.strftime("%d" + "-" + "%b" + "-" + "%Y")
hrmn = time.strftime("%H:%M:%S")

# <codecell>

betdict.update({'lastname': lasnam})
betdict.update({'reason': signin})
betdict.update({'signin comment': usecom})
betdict.update({'signin date': dayr})
betdict.update({'signin hrmin': hrmn})

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
        for i in betdict.values():
            li(a(i))

    with div():
        attr(cls='body')
        p('last updated: ' + time.strftime("%H:%M"))
        p('Visitor Sign Sheet is open source')
        a('http://github.com/wcmckee/wcmckee')

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

savpos = open('/home/wcmckee/visignsys/posts/' + ixtwe + '.html', 'a')
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

savpos = open('/home/wcmckee/visignsys/index.json', 'w')
savpos.write(str(betjsn))
savpos.close()

# <codecell>

print 'sign in complete'

# <codecell>


# <codecell>


