# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pyping
import nmap
import dominate
from dominate.tags import *
import paramiko
import base64

# <codecell>

nm = nmap.PortScanner()

# <codecell>

allscan = nm.scan('192.168.1.*')

# <codecell>

allhosts = nm.all_hosts()

# <codecell>

pinglis = []
nplis = []

# <codecell>

for hosts in allhosts:
    print(hosts)
    pinglis.append(pyping.ping(hosts))

# <codecell>

for pls in pinglis:
    print pls.output[0]
    nplis.append(pls.output[0])

# <codecell>

nplis

# <codecell>

nmapdoc = dominate.document(title='nmap scan')

# <codecell>

doc = dominate.document(title='nmap ping')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    #with div(id='header').add(ol()):
    #    for i in pinglis:
    #        li(a(i(), href='/%s.html' % i))

    with div():
        attr(cls='body')
        p(nplis)

print doc

# <codecell>

key = paramiko.RSAKey(data=base64.decodestring('AAA...'))

# <codecell>

key = paramiko.RSAKey(data=base64.decodestring('AAA...'))

# <codecell>

client = paramiko.SSHClient()

# <codecell>

clientkey = client.get_host_keys()

# <codecell>

clientkey

# <codecell>

client.connect('192.168.1.6', username='deb', password='deb')

# <rawcell>


