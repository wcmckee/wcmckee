
# coding: utf-8

# ##### <h1>BroBeurKids Nikola</h1>
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
# Create preconfig files. A posts folder that one item is published.
# Depending on prepost folder deturms the post folder it's moved to. 
# Sequale and post certain times a day. 

# This script creates a blog post and saves it in posts folder along with the .meta file for it. 
# Config file for the script. Specify a list of blog names. 
# Reads a json file that contains: blog name (school name), author (input username), twitter config dir, domain name (school name - space and crap),
# 
# Do login/logout via blog post. 

# In[1]:

import os
import getpass
from walkdir import filtered_walk, dir_paths, all_paths, file_paths
import arrow
#import nikola
from TwitterFollowBot import TwitterBot


# In[62]:

raw = arrow.utcnow()


# In[64]:

def returntime():
    return raw.strftime('%H:%M:%S')


# In[65]:

yraw = raw.strftime("%Y")
mntaw = raw.strftime("%m")
dytaw = raw.strftime("%d")
#gmtz.strftime("%Y")


# In[66]:

fulda = yraw + '/' + mntaw + '/' + dytaw


# In[67]:

fultim = fulda + ' ' + returntime()


# In[68]:

#fultim


# In[69]:

#gtur = getpass.getuser()


# In[70]:

#lisbbkn = os.listdir('/home/' + gtur + '/brobeurkidsdotcom/posts')


# In[71]:

#lisbbkn


# In[72]:

#for lisb in lisbbkn:
#    if '.ipynb' in lisb:
#        print lisb  


# In[73]:

#Name of notebook you want to turn into a blog
#Could check the folder (walkdir) for files not 
#in the wcmckee.com posts folder.
#Tags. Modules used. 
#Look at the file and extract out modules imported,
#using these as tags.


# In[49]:

podir = input('blog dir: ')


# In[74]:

nbog = input('Name of file to blog: ')


# In[14]:

etnam = input('Extension of file to blog: ')


# In[15]:

tagmak = input('post tags: ')


# In[56]:

#Write the blog post
contenmak = input('content: ')


# In[16]:

#savewhere = input('dir to save post: ')


# In[17]:

my_list = tagmak.split(",")


# In[18]:

my_list


# In[19]:

hashtag = list()


# In[20]:

for myl in my_list:
    #print ('#' + myl.replace(' ', ''))
    hashtag.append(('#' + myl.replace(' ', '')))


# In[65]:

for has in hashtag:
    print (has)
    bro_bot.auto_follow(has, count=1)


# In[21]:

endstring = ''
for s in hashtag:
    endstring += s + ' '



# In[22]:

endstring


# In[ ]:




# In[43]:

#pear = input('path to search: ')


# In[ ]:

jsve = dict({'filename' : nbog + etnam, 'tags' : tagmak, 'date' : fulda, 'time' : returntime()})


# In[45]:

#Search for blog through folders. 


# In[46]:

#files = file_paths(filtered_walk(pear, depth=100, included_files=[nbog + etnam]))


# In[34]:

#print files


# In[35]:

#for fil in files:
#    print (fil)
#    jsve.update({'filefound' : fil})


# In[36]:

#jsve['filefound']


# In[47]:

#opblog = ('/home/wcmckee/github/')


# In[48]:

#podir = ('/home/wcmckee/github/wcmckee.com/posts/')


# In[63]:

bro_bot = TwitterBot('/home/wcmckee/wcmnot/wcmckee-notebook/config.txt')
#bro_ot = TwitterBot(podir + '/config.txt')


# In[50]:

jsve.update({'blogdir' : podir})


# In[51]:

postsdir = podir + ('/posts/' )


# In[52]:

#os.system('cp ' + jsve['filefound'] + ' ' + postsdir)


# In[53]:

#for fie in files:
    #print fie
    #print (fie)
    #print ('Copy ' + fie + ' to ' + postsdir)
    #os.system('cp ' + fie + ' ' + postsdir)


# In[54]:

oprst = open(podir + '/posts/' + nbog + etnam, 'w')


# In[57]:

oprst.write(contenmak)


# In[58]:

oprst.close()


# In[59]:

opeza = open(podir + '/posts/' + nbog + '.meta', 'w')
opeza.write(nbog + '\n' + nbog + '\n' + fultim + '\n' + tagmak)

opeza.close()


# In[60]:

os.chdir(podir)
os.system('nikola build')


# In[44]:

bro_bot.send_tweet(nbog + ' ' + endstring + ' http://brobeur.com/blog/output/posts/' + nbog + '.html')


# In[ ]:



