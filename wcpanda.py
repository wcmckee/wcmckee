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


# <codecell>

#pd.Series(bepb)

# <codecell>

print dev

# <codecell>

#dev = usb.core.find(idVendor='1d6b:0002')

# was it found?
#if dev is None:
#    raise ValueError('Device not found')

# <codecell>

os.listdir('/dev/bus/usb/001')

# <codecell>

os.listdir('/dev/input')

# <codecell>

runpan = os.system('python wcpanda.py')

# <codecell>

runpan

# <codecell>

runpan.denominator

# <codecell>

camjpg = os.listdir('/media/Storage/videos/')

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

df.values

# <codecell>

df.sort

# <codecell>

df.to_html

# <codecell>

df.merge

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


