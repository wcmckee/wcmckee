
# coding: utf-8

# <h1>lcacoffee</h1>
# 
# script that displays coffees sold by hour at lca2015.
# Currently it opens a .json file and converts it into a python dict. 

# In[43]:

import json
import os
import csv


# In[44]:

opcvs = open('/home/wcmckee/Downloads/convertcsv.json', 'r')


# In[45]:

opzrd = opcvs.read()


# In[46]:

jdunp = json.loads(opzrd)


# In[47]:

valia = []


# In[48]:

jdunp.sort()


# In[49]:

jdunp.count(int)


# In[50]:

for jdr in jdunp[0]:
    print jdr


# In[50]:




# In[51]:

for dej in jdunp:
    print dej.values()
    valia.append(dej.values())


# In[52]:

dezrand = len(valia)


# In[53]:

azlis = []


# In[54]:

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

# In[55]:

betra = []


# In[56]:

for azl in azlis:
    betra.append(azl)


# In[57]:

anoe = []
anez = []


# In[58]:

for betr in betra:
    betr.append(anoe)


# In[59]:

for deta in betr:
    #print deta
    if '- -' in deta:
        print deta
    else:
        anez.append(deta)


# In[60]:

for resut in anez:
    print resut


# In[60]:




# In[104]:




# In[ ]:



