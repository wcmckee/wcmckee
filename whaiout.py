# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# This is the signout script that opens the xl file and fill in signout info.
# 
# creates date and time mark and asks for comment

# <codecell>

import xlrd
import os
import time
from xlutils.copy import copy
from xlrd import *
import dominate

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

# <codecell>


w = copy(open_workbook('/home/wcmckee/whai/index.xls'))
w.get_sheet(0).write(1,5, time.strftime("%d" + "-" + "%b" + "-" + "%Y"))
w.get_sheet(0).write(1,6, time.strftime("%H:%M"))
w.get_sheet(0).write(1,7, tiran)

w.save('/home/wcmckee/whai/index.xls')

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

print doc

# <codecell>

indsav = ('/home/wcmckee/whai/index.html')

# <codecell>

opind = open(indsav, 'w')

# <codecell>

opind.write(str(doc))

# <codecell>

opind.close()

# <codecell>

cat /home/wcmckee/whai/index.html

# <codecell>

lily allen live

