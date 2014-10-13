# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# This is the signout script that opens the xl file and fill in signout info.
# 
# Opens up list of signin data. This is date of sign in, time, name, and reason.
# This is .meta. This script appends sign out data. This is signout date, signout time, and comments.
# 
# 8 urandom 128 keys are generated. Used these in saving the achieve, as .html, and .meta files.
# 
# creates date and time mark and asks for comment

# <codecell>

import xlrd
import os
import time
from xlutils.copy import copy
from xlrd import *
import dominate
import json

# <codecell>

wrkbook = xlrd.open_workbook('/home/wcmckee/whai/index.xls')

# <codecell>

print wrkbook.sheet_names()

worksheet = wrkbook.sheet_by_name('visitor sign database')
swlis = []
num_rows = worksheet.nrows - 1
curr_row = -1
while curr_row < num_rows:
    curr_row += 1
    row = worksheet.row(curr_row)
    print row
    swlis.append(row)

# <codecell>

valis = []

# <codecell>

for swl in swlis[1]:
    print swl.value
    valis.append(swl.value)

# <codecell>

valis

# <codecell>

tiran = os.urandom(128).encode('hex')
reran = os.urandom(128).encode('hex')
comran = os.urandom(128).encode('hex')

# <codecell>

inpcom = raw_input('comment: ')

# <codecell>

endate = time.strftime("%d" + "-" + "%b" + "-" + "%Y")
          
entim = time.strftime("%H:%M")

# <codecell>

snoutm = {'signout date': endate}
snoutm.update({'signout time': entim})
snoutm.update({'signout comment': inpcom})

# <codecell>

snoutm

# <codecell>

signoutdic = {endate: tiran}
timoutdic = {entim: reran}

# <codecell>

signoutdic.update({entim:reran})

# <codecell>

signoutdic.update({inpcom: comran})

# <codecell>

signkeys = signoutdic.keys()

# <codecell>


w = copy(open_workbook('/home/wcmckee/whai/index.xls'))
w.get_sheet(0).write(1,5, time.strftime("%d" + "-" + "%b" + "-" + "%Y"))
w.get_sheet(0).write(1,6, time.strftime("%H:%M"))
w.get_sheet(0).write(1,7, tiran)

w.save('/home/wcmckee/whai/index.xls')

# <codecell>

indsav = ('/home/wcmckee/whai/index.html')

# <codecell>

opind = open(indsav, 'w')

# <codecell>

import dominate
from dominate.tags import *

doc = dominate.document(title=wrkbook.sheet_names())

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(id='header').add(ol()):
        for i in valis:
            li(a(i))

    with div():
        attr(cls='body')
        p('visitor sign database is open source. Visit https://github.com/wcmckee/wcmckee ')

#print doc

# <codecell>

opind.write(str(doc))

# <codecell>

opind.close()

# <codecell>

liop = open('/home/wcmckee/visignsys/index.meta', 'a+')
liop.write(str(signkeys))
liop.close()

# <codecell>


# <codecell>

oplis = open('/home/wcmckee/visignsys/index.meta', 'r')
oplsav = oplis.read()
oplis.close()

# <codecell>

trsor = tiran[0:12]

# <codecell>

trsor

# <codecell>

optrd = open('/home/wcmckee/visignsys/posts/' + trsor + '.meta', 'w')
optrd.write(oplsav)
optrd.close()

# <codecell>

oplsav

# <codecell>

jsnrd = open('/home/wcmckee/visignsys/posts/' + trsor + '.json', 'w')
jsnrd.write(oplsav)
jsnrd.close()

