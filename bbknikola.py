
# coding: utf-8

# <h1>BroBeurKids Nikola</h1>
# 
# This script deals with creating data for BroBeurKids/wcmckee Nikola site.
# 
# The directory to look at is brobeurkidsdotcom/posts 
# or folder
# 
# wcmckee.com /posts
# 
# /github folders are scanned with the input for folders.
# It's basically a search for notebook, then turn notebook into a blog posts.
# 
# Arrow is used to generate the date (YR/MONTH/DAY),
# and time(HR : MIN: SEC)
# 
# This is where ipynb files are kept. 
# 
# This script generates the .meta files needed. 
# 
# The meta file is called the same as the ipynb.  It also contains the slug and title, and date.
# The date is collected by looking at the save date of the ipynb.
# 
# 

# In[9]:

import os
import getpass
from walkdir import filtered_walk, dir_paths, all_paths, file_paths
import arrow
import nikola


# In[33]:

raw = arrow.utcnow()


# In[35]:

print raw


# In[45]:


def returntime():
    return raw.strftime('%H:%M:%S')


# In[47]:

returntime()


# In[36]:

yraw = raw.strftime("%Y")
mntaw = raw.strftime("%m")
dytaw = raw.strftime("%d")
#gmtz.strftime("%Y")


# In[37]:

fulda = yraw + '/' + mntaw + '/' + dytaw


# In[48]:

fultim = fulda + ' ' + returntime()


# In[49]:

#fultim


# In[9]:

#gtur = getpass.getuser()


# In[10]:

#lisbbkn = os.listdir('/home/' + gtur + '/brobeurkidsdotcom/posts')


# In[12]:

#lisbbkn


# In[14]:

#for lisb in lisbbkn:
#    if '.ipynb' in lisb:
#        print lisb  


# In[1]:

#Name of notebook you want to turn into a blog


# In[65]:

nbog = raw_input('Name of notebook to blog: ')


# In[66]:

#Search for blog through folders. 


# In[67]:

files = file_paths(filtered_walk('/home/wcmckee/github/', depth=100, included_files=[nbog + '.ipynb']))


# In[68]:

#print files


# In[69]:

opblog = ('/home/wcmckee/github/')


# In[74]:

podir = ('/home/wcmckee/github/wcmckee.com/posts/')


# In[75]:

podir


# In[70]:

for fie in files:
    #print fie
    print fie
    os.system('cp ' + fie + ' ' + podir)


# In[71]:

opeza = open(podir + nbog + '.meta', 'w')
opeza.write(nbog + '\n' + nbog + '\n' + fultim)
opeza.close()


# In[ ]:




# In[ ]:

os.chdir('/home/wcmckee/github/wcmckee.com/')
os.system('nikola build')

