
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

# In[45]:

import os
import getpass
from walkdir import filtered_walk, dir_paths, all_paths, file_paths
import arrow
#import nikola
#from TwitterFollowBot import TwitterBot


# In[46]:

raw = arrow.utcnow()


# In[47]:

def returntime():
    return raw.strftime('%H:%M:%S')


# In[48]:

yraw = raw.strftime("%Y")
mntaw = raw.strftime("%m")
dytaw = raw.strftime("%d")
#gmtz.strftime("%Y")


# In[49]:

fulda = yraw + '/' + mntaw + '/' + dytaw


# In[50]:

fultim = fulda + ' ' + returntime()


# In[51]:

#fultim


# In[52]:

#gtur = getpass.getuser()


# In[53]:

#lisbbkn = os.listdir('/home/' + gtur + '/brobeurkidsdotcom/posts')


# In[54]:

#lisbbkn


# In[55]:

#for lisb in lisbbkn:
#    if '.ipynb' in lisb:
#        print lisb  


# In[56]:

#Name of notebook you want to turn into a blog
#Could check the folder (walkdir) for files not 
#in the wcmckee.com posts folder.
#Tags. Modules used. 
#Look at the file and extract out modules imported,
#using these as tags.


# In[57]:

podir = input('blog dir: ')


# In[32]:

nbog = input('Name of file to blog: ')


# In[33]:

etnam = input('Extension of file to blog: ')


# In[34]:

tagmak = input('post tags: ')


# In[89]:

#pear = input('path to search: ')


# In[38]:

jsve = dict()


# In[39]:

#Write the blog post
#Ask to write content or publish 
writecont = input('Write content? y/N ')
if 'y' in writecont:
    contenmak = input('content: ')

else:
    pear = input('path to search: ')
    files = file_paths(filtered_walk(pear, depth=100, included_files=[nbog + etnam]))
    for fil in files:
        print (fil)
        jsve.update({'filefound' : fil})


# In[ ]:

#add extra tags in 


# In[132]:

lastbit = contenmak[:50]


# In[133]:

contenmak[-50:]


# In[135]:

sampb = lastbit + '... ' + contenmak[-50:]


# In[136]:

sampb


# In[ ]:




# In[80]:

#savewhere = input('dir to save post: ')


# In[81]:

my_list = tagmak.split(",")


# In[82]:

my_list


# In[83]:

hashtag = list()


# In[84]:

for myl in my_list:
    #print ('#' + myl.replace(' ', ''))
    hashtag.append(('#' + myl.replace(' ', '')))


# In[85]:

#bro_bot = TwitterBot('/home/wcmckee/wcmnot/wcmckee-notebook/config.txt')
#bro_ot = TwitterBot(podir + '/config.txt')


# In[86]:

#for has in hashtag:
#    print (has)
#    bro_bot.auto_follow(has, count=1)


# In[87]:

endstring = ''
for s in hashtag:
    endstring += s + ' '



# In[88]:

endstring


# In[ ]:




# In[90]:

jsve = dict({'filename' : nbog + etnam, 'tags' : tagmak, 'date' : fulda, 'time' : returntime()})


# In[91]:

#Search for blog through folders. 


# In[92]:

#files = file_paths(filtered_walk(pear, depth=100, included_files=[nbog + etnam]))


# In[93]:

#print files


# In[94]:

#for fil in files:
#    print (fil)
#    jsve.update({'filefound' : fil})


# In[95]:

#jsve['filefound']


# In[96]:

#opblog = ('/home/wcmckee/github/')


# In[97]:

#podir = ('/home/wcmckee/github/wcmckee.com/posts/')


# In[98]:

jsve.update({'blogdir' : podir})


# In[41]:

postsdir = podir + ('/posts/' )


# In[42]:

#os.system('cp ' + jsve['filefound'] + ' ' + postsdir)


# In[43]:

#for fie in files:
    #print fie
    #print (fie)
    #print ('Copy ' + fie + ' to ' + postsdir)
    #os.system('cp ' + fie + ' ' + postsdir)


# In[ ]:




# In[44]:

if 'y' in writecont:
    oprst = open(podir + '/posts/' + nbog + etnam, 'w')
    oprst.write(contenmak)
    oprst.close()
else:
    os.system('cp ' + jsve['filefound'] + ' ' + postsdir)


# In[105]:

opeza = open(podir + '/posts/' + nbog + '.meta', 'w')
opeza.write(nbog + '\n' + nbog + '\n' + fultim + '\n' + tagmak)

opeza.close()


# In[106]:

#print (podir + '/posts/' + nbog + '.meta')


# In[107]:

#os.chdir(podir)
#os.system('nikola build')


# In[108]:

#os.system('rsync -azP ' + postsdir + ' ' + 'wcmckee@brobeur.com:/home/wcmckee/bb/blog/posts')


# In[110]:

#bro_bot.search_tweets(ndstring)


# In[111]:

#bro_bot.send_tweet(nbog + ' ' + endstring + ' http://brobeur.com/blog/output/posts/' + nbog + '.html')


# In[ ]:



