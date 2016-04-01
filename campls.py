
# coding: utf-8

# perform ls on directory looking for most recent rst file change. 
# Gets wordcount, most recent word, date and time of this change. 
# 
# Record the wordcount in a json object, compare to older json objects and 
# punish or rewards depending on changes. 
# 
# Tweets during the day of changes. 

# In[50]:

import os
import glob
import getpass


# In[52]:

theusr = getpass.getuser()


# In[53]:

newest = max(glob.iglob('/home/' + theusr + '/git/writersdenhamilton/posts/*.rst'),
                       key=os.path.getctime)


# In[54]:

filename = os.path.basename(newest)


# In[56]:

opnew = open(newest, 'r')


# In[57]:

newrd = opnew.read()


# In[58]:

opnew.close()


# In[59]:

nerdrep = newrd.replace('\n', ' ')


# In[60]:

nerdsplit = nerdrep.split()


# In[61]:

latword = nerdsplit[-1]


# In[62]:

wctoday = len(nerdsplit)


# In[63]:

print('Writing: ' + filename + ' recent word: ' + latword + '  wc: ' + str(wctoday))

