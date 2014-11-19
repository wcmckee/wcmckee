# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import pandas as pd
from pandas import *
import os
import qgrid
randn = np.random.randn

# <rawcell>

# What I want to do is open up the data from visignsys into pandas, display the data in rows and collums. 
# Dates with comments along side. The best way to do this is save dicts to files and open them with pandas, creating r n c. 

# <codecell>

readjson = open('/home/wcmckee/visignsys/index.meta', 'r')

# <codecell>

checkj = readjson.read()

# <codecell>

s = Series(checkj)

# <codecell>

s

# <codecell>

finmea = os.listdir('/home/wcmckee/visignsys/posts')

# <codecell>

finmea

# <codecell>

medalis = []

# <codecell>

for finm in finmea:
    if '.meta' in finm:
        medalis.append(finm)

# <codecell>

altxt = []

# <codecell>

for rmad in medalis:
    #print rmad
    with open('/home/wcmckee/visignsys/posts/' + rmad, 'r') as f:
            read_data = f.read()
            altxt.append(read_data)

# <codecell>

checkem = []

# <codecell>

for alt in altxt:
    print alt
    checkem.append(Series(alt))

# <codecell>

for chem in checkem:
    print chem

# <codecell>

s = Series(altxt)

# <codecell>

s.all

# <codecell>

s[0]

# <codecell>

ndf = {}

# <codecell>

df = DataFrame(s)

# <codecell>

df

# <codecell>

qgrid.show_grid

# <codecell>

medajsn = []

# <codecell>

for finm in finmea:
    if '.json' in finm:
        medajsn.append(finm)

# <codecell>

medajsn

# <codecell>

remz = []

# <codecell>

for mjsn in medajsn:
    #print rmad
    with open('/home/wcmckee/visignsys/posts/' + mjsn, 'r') as f:
            read_data = f.read()
            remz.append(read_data)

# <codecell>

remz

# <codecell>

import os
import time
import xlutils
import xlwt
import xlrd
import dominate
import sys
from dominate.tags import *
import json
#from sqlalchemy import Column, ForeignKey, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
#from sqlalchemy import create_engine

# <codecell>

lasnam = ('Mckee')
firnam = ('William')
dopz = ('04/12/1988')
mname = ('William Mckee')
ename = ('will@artcontrol.me')
signin = ('ESW')

wb = xlwt.Workbook()
ws = wb.add_sheet('visitor sign database')

# <codecell>

rangen = []

# <codecell>

for genz in range(8):
    #print os.urandom(128).encode('hex')
    rangen.append(os.urandom(128).encode('hex'))

# <codecell>

exran = os.urandom(128).encode('hex')

# <codecell>

ixran = os.urandom(128).encode('hex')

# <codecell>

rawdets = ['In-Date', 'In-Time', 'In-Code', 'Name', 'Reason', 'Out-Date', 'Out-Time']

# <codecell>

numroll = []
    #ws.write(0, det, )

# <codecell>

#for rad in rawdets:
 #   print rad
    #print len(rad)
#    print rad.upper()
    #range(20)

# <codecell>

ws.write(0, 0, 'In Date')
ws.write(0, 1, 'In Time')
ws.write(0, 2, 'In Code')
ws.write(0, 3, 'Name')
ws.write(0, 4, 'Reason')
ws.write(0, 5, 'Out Date')
ws.write(0, 6, 'Out Time')
ws.write(0, 7, 'Out Code')

# <codecell>

#strftime is %d (day), 

ws.write(1, 0, time.strftime("%d" + "-" + "%b" + "-" + "%Y"))

ws.write(1, 1, time.strftime("%H:%M"))

# <codecell>

#getname = raw_input('Name: ')
#getreason = raw_input('Reason: ')

# <codecell>

ws.write(1, 2, exran)

# <codecell>

ws.write(1, 3, mname)

# <codecell>

ws.write(1, 4, signin)

# <codecell>

#wb.save('/home/wcmckee/whai/' + xlvs)
wb.save('/home/wcmckee/whai/index.xls')

# <codecell>

usecom = raw_input('Comments: ')

# <codecell>

wsdict = {mname: rangen[0]}

# <codecell>

betdict = {'firstname': firnam}

# <codecell>

dayr = time.strftime("%d" + "-" + "%m" + "-" + "%Y")
hrmn = time.strftime("%H:%M:%S")

# <codecell>

betdict.update({'lastname': lasnam})
betdict.update({'reason': signin})
betdict.update({'signin-comment': usecom})
betdict.update({'signin-date': dayr})
betdict.update({'signin-hrmin': hrmn})

# <codecell>
s = Series(betdict)
betjsn = json.dumps(betdict)

# <codecell>

betjsn

# <codecell>

wsdict.update({time.strftime("%d" + "-" + "%m" + "-" + "%Y"): rangen[1]})

# <codecell>

wsdict.update({ time.strftime("%H:%M"): rangen[2]})

# <codecell>

wsdict.update({signin: rangen[3]})

# <codecell>

wsdict.update({usecom: rangen[4]})

# <codecell>


# <codecell>

doc = dominate.document(title='visitor sign sheet')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(id='header').add(ol()):
        for i in wsdict.keys():
            li(a(i))

    with div():
        attr(cls='body')
        p('last updated: ' + time.strftime("%H:%M"))

#print doc

# <codecell>

savindex = open('/home/wcmckee/visignsys/index.html', 'w')

# <codecell>

savindex.write(str(doc))
savindex.close()

# <codecell>

ixtwe = ixran[0:12]

# <codecell>

savpos = open('/home/wcmckee/visignsys/posts/' + ixtwe + '.html', 'w')
savpos.write(str(doc))
savpos.close()

# <codecell>

savpos = open('/home/wcmckee/visignsys/posts/' + ixtwe + '.meta', 'w')
savpos.write(str(wsdict))
savpos.close()

# <codecell>

savpos = open('/home/wcmckee/visignsys/index.meta', 'w')
savpos.write(str(wsdict.keys()))
savpos.close()

# <codecell>

savpos = open('/home/wcmckee/visignsys/index.json', 'w')
savpos.write(str(betjsn))
savpos.close()

# <codecell>

print 'helli'

# <codecell>


# <codecell>

s

# <codecell>

mydef = DataFrame(s)

# <codecell>

mydef

# <codecell>

urdef = mydef.copy()

# <codecell>

urdef.to_html()

# <codecell>

urdef.append(mydef)

# <codecell>

urdef

# <codecell>

pdran = pd.date_range(start='1-1-2000', end='12/31/2012', freq='B')

# <codecell>

ser = Series(pdran)

# <codecell>

ser

# <codecell>

for i in range(10):
    randn()

# <codecell>

ilisz = []

# <codecell>

contnum = 

# <codecell>

if contnum = 10:
    ilisz.append(randn())
    contnum = contnum + 1

# <codecell>

while contnum = (-10):
    ilitz.append(randn())
    contnum = contnum + 1

# <codecell>

#!/usr/bin/python

count = 0
while (count < 9):
   ilisz.append(randn())
   print 'The count is:', count
   count = count + 1
    

print "Good bye!"

# <codecell>

ilisz

# <codecell>

ser.append(ilisz)

# <codecell>

ser.index

# <codecell>

ser.

