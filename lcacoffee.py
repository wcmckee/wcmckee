
# coding: utf-8

# <h1>lcacoffee</h1>
# 
# script that displays coffees sold by hour at lca2015.
# Currently it opens a .json file and converts it into a python dict. 

# In[19]:

import json
import os
import csv


# In[20]:

opcvs = open('/home/wcmckee/Downloads/convertcsv.json', 'r')


# In[21]:

opzrd = opcvs.read()


# In[22]:

jdunp = json.loads(opzrd)


# In[23]:

valia = []


# In[24]:

jdunp.sort()


# In[25]:

jdunp.count(int)


# In[26]:

for jdr in jdunp[0]:
    print jdr


# In[26]:




# In[27]:

for dej in jdunp:
    print dej.values()
    valia.append(dej.values())


# In[10]:

dezrand = len(valia)


# In[11]:

azlis = []


# In[12]:

for vals in valia:    
    print vals[0:20]
    azlis.append(vals)


# I need to filter the - - from the results. I really only need the values that have numbers. 
# 
# Take number in brackets away from number not in brackets. 
# The number in brackets is total amount of coffees sold. The number not in brackets is amount of volchers used. 
# The number that I get when i take away is the coffee sold without volchers. 
# 
# New dict that shows only the times that coffee were sold and the amount of coffgfges that were solf. Maybe that would works. 

# In[13]:

betra = []


# In[14]:

for azl in azlis:
    betra.append(azl)


# In[34]:

anoe = []
anez = []


# In[30]:

for betr in betra:
    betr.append(anoe)


# In[39]:

for deta in betr:
    #print deta
    if '- -' in deta:
        print deta
    else:
        anez.append(anez)


# In[40]:

for resut in anez:
    print resut


# In[ ]:




# In[104]:




# In[ ]:



