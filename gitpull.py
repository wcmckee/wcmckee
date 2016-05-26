
# coding: utf-8

# gitpull
# 
# script to perform a git pull on all repos in a folder 

# In[35]:

import os
import getpass
#import git


# In[29]:

myusr = getpass.getuser()


# In[30]:

myusr


# In[31]:

gitpa = (os.listdir('/home/' + myusr + '/git/'))


# In[32]:

gitpw = '/home/' + myusr + '/git/'


# In[33]:

gitpa


# In[25]:

for pig in (gitpa):
    #print (pig)
    #os.chdir(gitpa)
    os.system('git pull ' + gitpw + pig)


# In[27]:


#repo = git.Repo.clone_from(self._small_repo_url(), os.path.join(rw_dir, 'repo'), branch='master')

#heads = repo.heads
#master = heads.master       # lists can be accessed by name for convenience
#master.commit    


# In[ ]:



