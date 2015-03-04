
# coding: utf-8

# wcm spint. script to log into public wifi with a script

# In[1]:

import splinter


# In[2]:

spb = splinter.Browser()


# In[3]:

spb.visit('http://10.4.0.11/upload/custom/TE%20TAKERE/Te%20Takere%20Disclaimer.html')


# In[ ]:

but = spb.find_by_name('Login')


# In[ ]:

but.click()


# In[ ]:



