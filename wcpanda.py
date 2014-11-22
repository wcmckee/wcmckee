# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import pandas as pd
import math
import usb

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

dev = usb.core.find(idVendor='1d6b:0002')

# was it found?
if dev is None:
    raise ValueError('Device not found')

# <codecell>

import arudino

# <codecell>


