# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import pandas as pd
from pandas import *
import os

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

for alt in altxt:
    print alt

# <codecell>

s = Series(altxt)

# <codecell>

s.all

# <codecell>


