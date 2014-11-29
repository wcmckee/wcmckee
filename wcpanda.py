# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import pandas as pd
import math
import usb
import os
import re
import subprocess
import email
import smtplib

# <markdowncell>

# This is a python script that performs a lsusb and ping systems, emailing off the results.
# 
# TODO
# 
# Alert if any changes to devices or ping. 
# Generate email that contains - lsusb - ping - recent music played - video snapshots
# 
# Altenative logins to password - something kids can remember and use.
# 
# Sign in/Sing Out script 
# generate reports of end of week/month
# 

# <codecell>

randn = np.random.randn

# <codecell>

randn()

# <codecell>

math.sin(randn())

# <codecell>

a = np.arange(randn())

# <codecell>

a

# <codecell>

a = np.arange(15).reshape(3,5)

# <codecell>

a

# <codecell>

opind = open('/home/wcmckee/visignsys/index.meta')

# <codecell>

doubme = opind.read()

# <codecell>

(doubme)

# <codecell>

for dou in doubme:
    print dou

# <codecell>

dev = usb.core.find()

# <codecell>

import serial

# <codecell>

serial.time

# <codecell>

busses = usb.busses()

# <codecell>

for bus in busses:
    print bus

# <codecell>

for bus in busses:
  devices = bus.devices
  for dev in devices:
    print repr(dev)
    print "Device:", dev.filename
    print "  idVendor: %d (0x%04x)" % (dev.idVendor, dev.idVendor)
    print "  idProduct: %d (0x%04x)" % (dev.idProduct, dev.idProduct)
    print "Manufacturer:", dev.iManufacturer
    print "Serial:", dev.iSerialNumber
    print "Product:", dev.iProduct

# <codecell>

dev

# <codecell>

dev.idProduct

# <codecell>

dev.idVendor

# <codecell>

dev.iManufacturer

# <codecell>

dev.iSerialNumber

# <codecell>

repr(dev)

# <codecell>

device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
df = subprocess.check_output("lsusb", shell=True)
devices = []
for i in df.split('\n'):
    if i:
        info = device_re.match(i)
        if info:
            dinfo = info.groupdict()
            dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
            devices.append(dinfo)
print devices

# <codecell>

ledec = len(devices)

# <codecell>

for devz in devices[0]:
    #print devz
    print devices[0][devz]

# <codecell>

#tesz = pd.DataFrame('test')

# <codecell>

namdev = ({})

# <codecell>

for devi in devices:
    print devi['tag']
    namdev.update({devi['tag']:devi['id']})

# <codecell>

namdev

# <codecell>

devices[0]

# <codecell>

susb = pd.Series(namdev)

# <codecell>

usbdf = pd.DataFrame(susb)

# <codecell>

usbdf

# <codecell>

#for dev in df.values:
#    for bepb in dev:
        #print bepb
#        print bepb['device']
        #s.append(bepb['tag'])
#        print bepb['tag']
#        print bepb['id']

# <codecell>

str(devices)

# <codecell>

usbhtml = usbdf.to_html()
ps = open('/etc/motion/ps', 'r')
passW = ps.readline()

# <codecell>

fromz = 'brobeurstudios@gmail.com'  
toz = 'will@artcontrol.me'  
msg = str(devices)

# Credentials (if needed)  
username = 'brobeurstudios@gmail.com'
password = passW   
# The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)  
server.sendmail(fromz, toz, msg)  

# <codecell>

#dev = usb.core.find(idVendor='1d6b:0002')

# was it found?
#if dev is None:
#    raise ValueError('Device not found')

# <codecell>

usbus = os.listdir('/home/wcmckee')

# <codecell>

chelis = []

# <codecell>

for usbz in usbus:
    #chelis.append(os.listdir(usbz))
    print usbz

# <codecell>


# <codecell>


# <codecell>

os.listdir('/dev/input')

# <codecell>

#runpan = os.system('python wcpanda.py')

# <codecell>

#runpan

# <codecell>

#runpan.denominator

# <codecell>

camjpg = os.listdir('/home/wcmckee/')

# <codecell>

for cjp in camjpg:
    print cjp
    

# <codecell>

jpser = pd.Series(camjpg)

# <codecell>

jpser

# <codecell>

df = pd.DataFrame(jpser)

# <codecell>

df

# <codecell>

lslit = []

# <codecell>

for fgvsl in df.values:
    print fgvsl
    #str(os.listdir(fgvsl))

# <codecell>

df.sort

# <codecell>

df.to_html()

# <codecell>

df.merge

# <codecell>


# <codecell>

df.tail()

# <codecell>

savmo = open('/home/wcmckee/motsav/index.html', 'w')
savmo.write(str(df.to_html()))

# <codecell>

savmo.close()

# <codecell>

opmo = open('/home/wcmckee/motsav/index.html', 'r')

# <codecell>

opmo.read()

# <codecell>


# <codecell>


# <codecell>


