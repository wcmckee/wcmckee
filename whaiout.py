# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <h3>WhaiOut</h3>
# 
# This is the signout script that opens the login file and fills in signout info.
# 
# Opens up list of signin data. This is date of sign in, time, name, and reason.
# This is .meta. This script appends sign out data. This is signout date, signout time, and comments.
# 
# 8 urandom 128 keys are generated. Used these in saving the achieve, as .html, and .meta files.
# Why not save as yr-month-day-hr-min.meta /html
# 
# Turn it into a Nikola blog. Three blog posts. login (whaxlu.py), logout (whaiout.py), and the result of both of them. Perhaps it
# 
# creates date and time mark and asks for comment

# <markdowncell>

# This needs rewriten to remove xl stuff opening. keep it to json and dict. 

# <codecell>

#import xlrd
import os
import time
#from xlutils.copy import copy
#from xlrd import *
import dominate
import json
from dominate.tags import *
from time import strftime, gmtime

# <codecell>

#wrkbook = xlrd.open_workbook('/home/wcmckee/whai/index.xls')

# <codecell>

jsopn = open('/home/wcmckee/visignsys/index.json', 'r')
jsrdv = jsopn.read()

# <codecell>

jsrdv

# <codecell>

#print wrkbook.sheet_names()

#worksheet = wrkbook.sheet_by_name('visitor sign database')
#swlis = []
#num_rows = worksheet.nrows - 1
#curr_row = -1
#while curr_row < num_rows:
#    curr_row += 1
#    row = worksheet.row(curr_row)
    #print row
#    swlis.append(row)

# <codecell>

#valis = []

# <codecell>

#for swl in swlis[1]:
#    print swl.value
#    valis.append(swl.value)

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

snoutm = {'out-date': endate}
snoutm.update({'out-time': entim})
snoutm.update({'out-comment': inpcom})

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

wha = open('/home/wcmckee/visignsys/index.json', 'a')

#w = copy(open_workbook('/home/wcmckee/whai/index.xls'))
#w.get_sheet(0).write(1,5, time.strftime("%d" + "-" + "%b" + "-" + "%Y"))
#w.get_sheet(0).write(1,6, time.strftime("%H:%M"))
#w.get_sheet(0).write(1,7, tiran)

#w.save('/home/wcmckee/whai/index.xls')

# <codecell>

indsav = ('/home/wcmckee/whai/index.html')

# <codecell>

opind = open(indsav, 'w')

# <codecell>

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

yearz = strftime("%y", gmtime())
monthz = strftime("%m", gmtime())
dayz = strftime("%d", gmtime())

hurz = strftime("%H", gmtime())
minz = strftime("%M", gmtime())

# <codecell>

dform = (yearz + monthz + dayz +hurz + minz)

# <codecell>

optrd = open('/home/wcmckee/visignsys/posts/' + dform + '.meta', 'w')
optrd.write(oplsav)
optrd.close()

# <codecell>

jsnrd = open('/home/wcmckee/visignsys/posts/' + dform + '.json', 'w')
jsnrd.write(oplsav)
jsnrd.close()

# <codecell>

savpos = open('/home/wcmckee/visignsys/index.json', 'r')
signindi = savpos.read()

# <codecell>

jsnaccept = signindi.replace("'", "\"")
snoutm = json.loads(jsnaccept)

# <codecell>

snct = dict(d.items() + snoutm.items())

# <codecell>

savpos.close()

# <codecell>

os.chdir('/home/wcmckee/visignsys/posts')

# <codecell>

lismet = os.listdir('/home/wcmckee/visignsys/posts')

# <codecell>

lismet

# <codecell>

opjsnz = []

# <codecell>

for beca in lismet:
    if '.json' in beca:
        print beca
        opjsnz.append(beca)

# <codecell>

optjz = []
optjsz = []

# <codecell>

apgpls = []

# <codecell>

#for opjw in opjsnz:
#    print opjw
#    optjsz.append(objw)
    

# <codecell>

#for filop in opjsnz:
    #print filop
#    opt = open(opj, 'r')
#    thedict = str(opt.read())
#    thedict
#    opt.close()

# <codecell>

#opt = open(opj, 'r')

# <codecell>

#thedict = opt.read()

# <codecell>

#thedict

# <codecell>

#convgpj = json.loads(thedict)

# <codecell>

#convgpj.values()

# <codecell>


# <codecell>


