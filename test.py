# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Testing the chromebook 

# <codecell>

import os

# <codecell>

lisfir = ('/home/wcmckee/index.xcf')

# <codecell>

lisfir

# <codecell>

def lisfire(localfile, remotehost, remotefile):
    return os.system('scp "%s" "%s:%s"' % (localfile, remotehost, remotefile) )

def refzem(remotehost, remotefolder):
    return os.system('scp "%s":"%s" ls -R' % (remotehost, remotefolder))

# <codecell>

lisfire('/home/wcmckee/Documents/getsdrawn-line.png', 'wcmckee@getsdrawn.com', '/home/wcmckee/getsdrawn-line.png')

# <codecell>

checkred = refzem('wcmckee', 'wcmckee.com')

# <rawcell>


# <codecell>

checkred.real

# <codecell>

chrez = checkred.conjugate

# <codecell>

checkred.imag

# <codecell>

chrez()

# <codecell>


# <codecell>


