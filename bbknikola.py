
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
# 
# Title should accept spaces - slug should be edited to remove space and replace with -

# In[1]:

import os
import getpass
from walkdir import filtered_walk, dir_paths, all_paths, file_paths
import arrow
#import nikola
#from TwitterFollowBot import TwitterBot


# In[2]:

raw = arrow.utcnow()


# In[3]:

def returntime():
    return raw.strftime('%H:%M:%S')


# In[4]:

yraw = raw.strftime("%Y")
mntaw = raw.strftime("%m")
dytaw = raw.strftime("%d")
#gmtz.strftime("%Y")


# In[5]:

fulda = yraw + '/' + mntaw + '/' + dytaw


# In[6]:

fultim = fulda + ' ' + returntime()


# In[7]:

#fultim


# In[8]:

#gtur = getpass.getuser()


# In[9]:

#lisbbkn = os.listdir('/home/' + gtur + '/brobeurkidsdotcom/posts')


# In[10]:

#lisbbkn


# In[11]:

#for lisb in lisbbkn:
#    if '.ipynb' in lisb:
#        print lisb  


# In[12]:

#Name of notebook you want to turn into a blog
#Could check the folder (walkdir) for files not 
#in the wcmckee.com posts folder.
#Tags. Modules used. 
#Look at the file and extract out modules imported,
#using these as tags.


# In[13]:

podir = input('blog dir: ')


# In[14]:

nbog = input('Name of file to blog: ')


# In[15]:

etnam = input('Extension of file to blog: ')


# In[16]:

tagmak = input('post tags: ')


# In[17]:

#pear = input('path to search: ')


# In[18]:

jsve = dict()


# In[19]:

nbog + etnam


# In[21]:

#Write the blog post
#Ask to write content or publish 
writecont = input('Write content? y/N ')
if 'y' in writecont:
    contenmak = input('content: ')

else:
    #search or manually locate fil.
    pear = input('path to search: y/N')
    if 'y' in pear:
        files = file_paths(filtered_walk(pear, depth=100, included_files=[nbog + etnam]))
        for fil in files:
            print (fil)
            jsve.update({'filefound' : fil})
    else:
        patlim = input('path of file: ')
        jsve.update({'filefound' : patlim + nbog + etnam})


# In[22]:

#fil


# In[23]:

#add extra tags in 


# In[24]:

jsve


# In[25]:

#lastbit = contenmak[:50]


# In[26]:

#contenmak[-50:]


# In[27]:

#sampb = lastbit + '... ' + contenmak[-50:]


# In[28]:

#sampb


# In[ ]:




# In[29]:

#savewhere = input('dir to save post: ')


# In[30]:

my_list = tagmak.split(",")


# In[31]:

my_list


# In[32]:

hashtag = list()


# In[33]:

for myl in my_list:
    #print ('#' + myl.replace(' ', ''))
    hashtag.append(('#' + myl.replace(' ', '')))


# In[34]:

#bro_bot = TwitterBot('/home/wcmckee/wcmnot/wcmckee-notebook/config.txt')
#bro_ot = TwitterBot(podir + '/config.txt')


# In[35]:

#for has in hashtag:
#    print (has)
#    bro_bot.auto_follow(has, count=1)


# In[36]:

endstring = ''
for s in hashtag:
    endstring += s + ' '



# In[37]:

endstring


# In[ ]:




# In[38]:

jsve.update({'filename' : nbog + etnam, 'tags' : tagmak, 'date' : fulda, 'time' : returntime()})


# In[39]:

#jsve.update({})


# In[40]:

jsve


# In[41]:

#Search for blog through folders. 


# In[42]:

#files = file_paths(filtered_walk(pear, depth=100, included_files=[nbog + etnam]))


# In[43]:

#print files


# In[44]:

#for fil in files:
#    print (fil)
#    jsve.update({'filefound' : fil})


# In[45]:

#jsve['filefound']


# In[46]:

#opblog = ('/home/wcmckee/github/')


# In[47]:

#podir = ('/home/wcmckee/github/wcmckee.com/posts/')


# In[48]:

jsve.update({'blogdir' : podir})


# In[49]:

postsdir = podir + ('/posts/' )


# In[50]:

#os.system('cp ' + jsve['filefound'] + ' ' + postsdir)


# In[51]:

#for fie in files:
    #print fie
    #print (fie)
    #print ('Copy ' + fie + ' to ' + postsdir)
    #os.system('cp ' + fie + ' ' + postsdir)


# In[52]:

jsve


# In[ ]:




# In[53]:

os.system('cp ' + jsve['filefound'] + ' ' + postsdir)


# In[54]:

if 'y' in writecont:
    oprst = open(podir + '/posts/' + nbog + etnam, 'w')
    oprst.write(contenmak)
    oprst.close()
else:
    os.system('cp ' + jsve['filefound'] + ' ' + postsdir)


# In[55]:

opeza = open(podir + '/posts/' + nbog + '.meta', 'w')
opeza.write(nbog + '\n' + nbog + '\n' + fultim + '\n' + tagmak)

opeza.close()


# In[134]:

#print (podir + '/posts/' + nbog + '.meta')


# In[135]:

#os.chdir(podir)
#os.system('nikola build')


# In[136]:

#os.system('rsync -azP ' + postsdir + ' ' + 'wcmckee@brobeur.com:/home/wcmckee/bb/blog/posts')


# In[137]:

#bro_bot.search_tweets(ndstring)


# In[138]:

#bro_bot.send_tweet(nbog + ' ' + endstring + ' http://brobeur.com/blog/output/posts/' + nbog + '.html')


# In[ ]:




# In[ ]:




# In[ ]:



