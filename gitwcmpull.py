
# coding: utf-8

# gitwcmpull
# 
# Dealing with git repos

# In[2]:

#import git
import os


# In[ ]:




# In[6]:

lismed = os.listdir('/media/removable/USB Drive/wcmckee-git')


# In[7]:

#os.chdir('/media/removable/USB Drive/wcmckee-git/' + lism)


# In[9]:

#os.system('git pull')


# In[ ]:

for lism in lismed:
    print lism
    os.chdir('/media/removable/USB Drive/wcmckee-git/' + lism)
    os.system('git pull')


# In[ ]:



