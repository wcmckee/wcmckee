
# coding: utf-8

# <h3>artcontrol gallery</h3>
# 
# Create gallery for artcontrol artwork. 
# 
# Uses Year / Month / Day format.
# 
# Create blog post for each day there is a post.
# 
# It will need to list the files for that day and create a markdown file in posts that contains the artwork. Name of art then followed by each pience of artwork -line, bw, color. 
# 
# write a message about each piece of artwork. 
# 
# 

# In[ ]:




# In[1]:

import os
import arrow


# In[2]:

raw = arrow.now()


# In[3]:

yraw = raw.strftime("%Y")
mntaw = raw.strftime("%m")
dytaw = raw.strftime("%d")


# In[4]:

fulda = yraw + '/' + mntaw + '/' + dytaw


# In[5]:

fultim = fulda + ' ' + raw.strftime('%H:%M:%S')


# In[ ]:




# In[6]:

arnow = arrow.now()


# In[7]:

curyr = arnow.strftime('%Y')


# In[8]:

curmon = arnow.strftime('%m')


# In[9]:

curday = arnow.strftime('%d')


# In[10]:

galerdir = ('/home/wcmckee/github/artcontrolme/galleries/')


# In[11]:

galdir = os.listdir('/home/wcmckee/github/artcontrolme/galleries/')


# In[12]:

galdir


# In[52]:

mondir = os.listdir(galerdir + curyr)


# In[53]:

daydir = os.listdir(galerdir + curyr + '/' + curmon )


# In[54]:

daydir


# In[55]:

galdir


# In[56]:

mondir


# In[57]:

daydir


# In[ ]:




# In[58]:

if curyr in galdir:
    pass
else:
    os.mkdir(galerdir + curyr)


# In[59]:

if curmon in mondir:
    pass
else:
    os.mkdir(galerdir + curyr + '/' + curmon)


# In[60]:

fulldaypath = (galerdir + curyr + '/' + curmon + '/' + curday)


# In[61]:

if curday in daydir:
    pass
else:
    os.mkdir(galerdir + curyr + '/' + curmon + '/' + curday)


# In[62]:

galdir


# In[63]:

mondir


# In[64]:

daydir


# In[65]:

str(arnow.date())


# In[66]:

nameofblogpost = input('Post name: ')


# check to see if that blog post name already excist, if so error and ask for something more unique! 
# 
# input art piece writers. Shows the art then asks for input, appending the input below the artwork. Give a name for the art that is appended above. 

# In[ ]:




# In[67]:

daypost = open('/home/wcmckee/github/artcontrolme/posts/' + nameofblogpost + '.md', 'w')


# In[68]:

daymetapost = open('/home/wcmckee/github/artcontrolme/posts/' + nameofblogpost + '.meta', 'w')


# In[69]:

daymetapost.write('.. title: ' + nameofblogpost + ' \n' + '.. slug: ' + nameofblogpost + ' \n' + '.. date: ' + fultim + ' \n' + '.. author: wcmckee')


# In[70]:

daymetapost.close()


# In[ ]:




# In[ ]:




# In[71]:

todayart = os.listdir(fulldaypath)


# In[72]:

titlewor = list()


# In[73]:

titlewor


# ![themilkcollective-line](/galleries/2015/10/themilkcollective-line.png)

# In[74]:

galpath = ('/galleries/' + curyr + '/' + curmon + '/' + curday + '/')


# In[75]:

galpath


# In[76]:

todayart.sort()


# In[77]:

todayart


# In[78]:

for toar in todayart:
    daypost.write(('!' + '[' + toar.strip('.png') + '](' + galpath + toar + ')\n'))


# In[79]:

daypost.close()


# In[ ]:




# In[ ]:



