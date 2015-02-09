
# coding: utf-8

# <h1>BroBeurKids Nikola</h1>
# 
# This script deals with creating data for BroBeurKids Nikola site.
# 
# The directory to look at is brobeurkidsdotcom/posts 
# 
# This is where ipynb files are kept. 
# 
# This script generates the .meta files needed. 
# 
# The meta file is called the same as the ipynb.  It also contains the slug and title, and date.
# The date is collected by looking at the save date of the ipynb.
# 
# 

# In[8]:

import os
import getpass


# In[9]:

gtur = getpass.getuser()


# In[10]:

lisbbkn = os.listdir('/home/' + gtur + '/brobeurkidsdotcom/posts')


# In[12]:

lisbbkn


# In[14]:

for lisb in lisbbkn:
    if '.ipynb' in lisb:
        print lisb  


# In[ ]:



