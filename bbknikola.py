
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

# In[29]:

import os
import getpass
from walkdir import filtered_walk, dir_paths, all_paths, file_paths
import arrow
#import nikola


# In[30]:

raw = arrow.utcnow()


# In[31]:

def returntime():
    return raw.strftime('%H:%M:%S')


# In[32]:

returntime()


# In[33]:

yraw = raw.strftime("%Y")
mntaw = raw.strftime("%m")
dytaw = raw.strftime("%d")
#gmtz.strftime("%Y")


# In[34]:

fulda = yraw + '/' + mntaw + '/' + dytaw


# In[35]:

fultim = fulda + ' ' + returntime()


# In[36]:

#fultim


# In[37]:

#gtur = getpass.getuser()


# In[38]:

#lisbbkn = os.listdir('/home/' + gtur + '/brobeurkidsdotcom/posts')


# In[39]:

#lisbbkn


# In[40]:

#for lisb in lisbbkn:
#    if '.ipynb' in lisb:
#        print lisb  


# In[41]:

#Name of notebook you want to turn into a blog
#Could check the folder (walkdir) for files not 
#in the wcmckee.com posts folder.
#Tags. Modules used. 
#Look at the file and extract out modules imported,
#using these as tags.


# In[42]:

nbog = input('Name of file to blog: ')


# In[43]:

etnam = input('Extension of file to blog: ')


# In[44]:

tagmak = input('post tags: ')


# In[45]:

pear = input('path to search: ')


# In[ ]:




# In[18]:

#Search for blog through folders. 


# In[46]:

files = file_paths(filtered_walk(pear, depth=100, included_files=[nbog + etnam]))


# In[47]:

#print files


# In[48]:

opblog = ('/home/wcmckee/github/')


# In[49]:

#podir = ('/home/wcmckee/github/wcmckee.com/posts/')


# In[50]:

podir = input('blog dir: ')


# In[55]:

postsdir = podir + ('/posts/' )


# In[ ]:




# In[56]:

for fie in files:
    #print fie
    print (fie)
    print ('Copy ' + fie ' to ' + postsdir)
    os.system('cp ' + fie + ' ' + postsdir)


# In[57]:

opeza = open(podir + nbog + '.meta', 'w')
opeza.write(nbog + '\n' + nbog + '\n' + fultim + '\n' + tagmak)
opeza.close()


# In[ ]:




# In[58]:

os.chdir(podir)
os.system('nikola build')


# In[ ]:



