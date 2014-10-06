# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# visitor sign system
# 
# This is a python script used to sign in and signout, keeping track of hours and creating a more automative system.
# 
# Make sign in and out fast 
# 
# Never forget. 
# 
# Auto roll check. 

# <codecell>

import tweepy
import os
import time
import xlutils
import xlwt

# <codecell>

conke = 'DfrJQ56s4Hhr8MhTg92xw'
consec = 'XCVXYLtK9mJ9a4aKpT0wXpmYexFvSFLxbdm1aZFPjFQ'
ackey = '26423770-Z8AmtM2JCVFFJ708lddF72rO2qa9gjlT1hFuYJAQ1'
acsec = '3lI7Bw262NOvKkqE7iw4vx1JORIasjMjAB4rkAE'

# <codecell>

auth = tweepy.OAuthHandler(conke, consec)
auth.set_access_token(ackey, acsec)

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

rawdets = ['In Date', 'In Time', 'Name', 'Reason', 'Out Date', 'Out Time']

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
ws.write(0, 2, 'Name')
ws.write(0, 3, 'Reason')
ws.write(0, 4, 'Out Date')
ws.write(0, 5, 'Out Time')

# <codecell>

#strftime is %d (day), 

ws.write(1, 0, time.strftime("%d" + "-" + "%b" + "-" + "%Y"))

ws.write(1, 1, time.strftime("%H:%M"))

# <codecell>

getname = raw_input('Name: ')
getreason = raw_input('Reason: ')

# <codecell>

ws.write(1, 2, getname)

# <codecell>

ws.write(1, 3, getreason)

# <codecell>

wb.save('/home/wcmckee/whai/' + xlvs)

# <codecell>


