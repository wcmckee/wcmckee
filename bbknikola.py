
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

# In[2]:

import os
import getpass
from walkdir import filtered_walk, dir_paths, all_paths, file_paths
import arrow
#import nikola


# In[3]:

raw = arrow.utcnow()


# In[5]:

def returntime():
    return raw.strftime('%H:%M:%S')


# In[6]:

returntime()


# In[7]:

yraw = raw.strftime("%Y")
mntaw = raw.strftime("%m")
dytaw = raw.strftime("%d")
#gmtz.strftime("%Y")


# In[8]:

fulda = yraw + '/' + mntaw + '/' + dytaw


# In[9]:

fultim = fulda + ' ' + returntime()


# In[10]:

#fultim


# In[11]:

#gtur = getpass.getuser()


# In[12]:

#lisbbkn = os.listdir('/home/' + gtur + '/brobeurkidsdotcom/posts')


# In[13]:

#lisbbkn


# In[14]:

#for lisb in lisbbkn:
#    if '.ipynb' in lisb:
#        print lisb  


# In[15]:

#Name of notebook you want to turn into a blog
#Could check the folder (walkdir) for files not 
#in the wcmckee.com posts folder.
#Tags. Modules used. 
#Look at the file and extract out modules imported,
#using these as tags.


# In[18]:

nbog = input('Name of file to blog: ')


# In[21]:

etnam = input('Extension of file to blog: ')


# In[22]:

tagmak = input('post tags: ')


# In[20]:

pear = input('path to search: ')


# In[ ]:




# In[66]:

#Search for blog through folders. 


# In[23]:

files = file_paths(filtered_walk(pear, depth=100, included_files=[nbog + etnam]))


# In[24]:

#print files


# In[69]:

opblog = ('/home/wcmckee/github/')


# In[74]:

#podir = ('/home/wcmckee/github/wcmckee.com/posts/')


# In[25]:

podir = input('blog dir: ')


# In[26]:

postsdir = podir + ('/posts/' )


# In[ ]:




# In[70]:

for fie in files:
    #print fie
    os.system('cp ' + fie + ' ' + podir)


# In[71]:

opeza = open(podir + nbog + '.meta', 'w')
opeza.write(nbog + '\n' + nbog + '\n' + fultim + '\n' + tagmak)
opeza.close()


# In[ ]:




# In[ ]:

os.chdir(podir)
os.system('nikola build')

