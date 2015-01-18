
# coding: utf-8

# <h1>lcacoffee</h1>
# 
# script that displays coffees sold by hour at lca2015.
# Currently it opens a .json file and converts it into a python dict. 

# In[65]:

import json
import os
import csv


# In[66]:

opcvs = open('/home/wcmckee/Downloads/convertcsv.json', 'r')


# In[67]:

opzrd = opcvs.read()


# In[68]:

jdunp = json.loads(opzrd)


# In[69]:

valia = []


# In[70]:

jdunp.sort()


# In[71]:

jdunp.count(int)


# In[72]:

for jdr in jdunp[0]:
    print jdr


# In[72]:




# In[73]:

for dej in jdunp:
    print dej.values()
    valia.append(dej.values())


# In[74]:

dezrand = len(valia)


# In[75]:

azlis = []


# In[76]:

for vals in valia:    
    print vals
    azlis.append(vals)


# I need to filter the - - from the results. I really only need the values that have numbers. 
# 
# Take number in brackets away from number not in brackets. 
# The number in brackets is total amount of coffees sold. The number not in brackets is amount of volchers used. 
# The number that I get when i take away is the coffee sold without volchers. 
# 
# New dict that shows only the times that coffee were sold and the amount of coffgfges that were solf. Maybe that would works. 

# In[77]:

betra = []


# In[78]:

for azl in azlis:
    betra.append(azl)


# In[79]:

anoe = []
anez = []


# In[80]:

for betr in betra:
    betr.append(anoe)


# In[81]:

for deta in betr:
    #print deta
    if '- -' in deta:
        print deta
    else:
        anez.append(deta)


# In[82]:

fdic = []


# In[83]:

for resut in anez:
    print resut
    fdic.append(resut)


# In[84]:

fdic


# In[84]:




# In[84]:




# In[ ]:



