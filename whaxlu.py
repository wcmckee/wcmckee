# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# visitor sign system
# 
# This is a python script used to sign in and signout, keeping track of hours and creating a more automative system.
# 
# Make sign in and out faster, easier to keep track of.
# 
# Never forget. 
# 
# Auto roll check. 
# 
# Two random hex codes for security and correct checking. 
# 
# Creates xls file with data: 
# input (or auto) name, reason, auto day/month/year hr/min - of signin

# <codecell>

import os
import time
import xlutils
import xlwt
import dominate

# <codecell>

mname = ('William Mckee')
ename = ('will@artcontrol.me')
signin = ('ESW')

# <codecell>

time.strftime("%a, %d %b %Y %H:%M: +0000", time.gmtime())

# <codecell>

wb = xlwt.Workbook()
ws = wb.add_sheet('visitor sign database')

# <codecell>

exran = os.urandom(128).encode('hex')

# <codecell>

ixran = os.urandom(128).encode('hex')

# <codecell>

rawdets = ['In Date', 'In Time', 'In Code', 'Name', 'Reason', 'Out Date', 'Out Time']

# <codecell>

numroll = []

# <codecell>

for det in range(6):
    print det
    numroll.append(det)
    #ws.write(0, det, )

# <codecell>

numroll

# <codecell>

for rad in rawdets:
    print rad
    #print len(rad)
    print rad.upper()
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

getname = raw_input('Name: ')
getreason = raw_input('Reason: ')

# <codecell>

ws.write(1, 2, exran)

# <codecell>

ws.write(1, 3, getname)

# <codecell>

ws.write(1, 4, getreason)

# <codecell>

wb.save('/home/wcmckee/whai/' + xlvs)

# <codecell>

wsdict = {getname: exran}

# <codecell>

wsdict

# <codecell>

wsdict.update({time.strftime("%d" + "-" + "%b" + "-" + "%Y"): time.strftime("%H:%M")})

# <codecell>

wsdict.update({getreason: ixran})

# <codecell>

wsdict

# <codecell>

wsdict.keys()

# <codecell>

import dominate
from dominate.tags import *

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

print doc

# <codecell>


# <codecell>


