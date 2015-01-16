
# coding: utf-8

# <h1>lcacoffee</h1>
# 
# script that displays coffees sold by hour at lca2015.
# Currently it opens a .json file and converts it into a python dict. 

# In[97]:

import json
import os
import csv


# In[98]:

opcvs = open('/home/wcmckee/Downloads/convertcsv.json', 'r')


# In[99]:

opzrd = opcvs.read()


# In[100]:

jdunp = json.loads(opzrd)


# In[101]:

valia = []


# In[102]:

jdunp


# In[102]:




# In[103]:

for dej in jdunp:
    print dej.values()
    valia.append(dej.values())


# In[109]:

len(valia)


# In[108]:

for vals in valia:        
    print vals


# In[104]:




# In[104]:




# In[ ]:



