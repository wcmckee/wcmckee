
# coding: utf-8

# TwitFol
# 
# script to send tweet from random list of subreddits containing a random submission of the subreddit.
# 
# Also searches twitter for something containing a hashtag of gamejams currently happening etc.

# In[36]:

from TwitterFollowBot import TwitterBot
import requests
import json
import praw
import random


# In[ ]:




# In[37]:

bb_bot = TwitterBot('/home/wcmckee/brobeur-tweet/brobeur.txt')


# In[68]:

wcm_bot = TwitterBot('/home/wcmckee/wcm-tweet/config.txt')


# In[38]:

r = praw.Reddit(user_agent='wcmckeepython')


# In[69]:

wcmsubreds = ['python', 'ipython', 'webdev', 'coding', 'databases', 'hacking', 'haskell', 'linux']


# In[49]:

scribred = ['writing', 'gaming', 'InternetIsBeautiful', 'Minecraft', 'skyrim', 'linux', 'opensource', 'wow']


# In[70]:

wcmrasub = random.choice(wcmsubreds)


# In[71]:

hashwcm = ('#' + wcmrasub)


# In[50]:

randscr = random.choice(scribred)


# In[51]:

hashse = ('#' + randscr)


# In[52]:

getnewr = r.get_subreddit(randscr)


# In[53]:

randscr


# In[73]:

getwcms = r.get_subreddit(wcmrasub)


# In[74]:

twcm = getwcms.get_random_submission()


# In[75]:

wtit = twcm.title


# In[76]:

wurl = twcm.url


# In[77]:

wcm_bot.send_tweet(wtit + ' ' + wurl + ' ' + hashwcm)


# In[54]:

#for getr in getnewr:
#    print (getr)


# In[55]:

getrsub = getnewr.get_random_submission()


# In[56]:

gtia = getrsub.title


# In[57]:

gurl = getrsub.url


# In[58]:

bb.send_tweet(gtia + ' ' + gurl + ' ' + hashse)


# In[59]:

#reqjok = requests.get('http://tambal.azurewebsites.net/joke/random')


# In[60]:

#jsjok = reqjok.text


# In[61]:

#dicjok = json.loads(jsjok)


# In[62]:

#str(dicjok.values())


# In[63]:

#for dicv in dicjok.values():
#    print (dicv)
#    my_bot.send_tweet(dicv)


# In[64]:

#my_bot.sync_follows()


# In[65]:

#my_bot.auto_unfollow_nonfollowers()


# In[79]:

wcmretw = ['#ForgeConf', '#lascot15', '#code', '#programming', '#linux']


# In[66]:

tweval = ['#gamedev', '#ludumdare', '#1GAM', '#gaming', '#gta', '#uncharted', '#unity3d', ]


# In[78]:

bbranrt = random.choice(tweval)


# In[80]:

wcretw = random.choice(wcmretw)


# In[ ]:




# In[67]:

bb_bot.auto_rt(tweval, count = 1 )


# In[81]:

wcm_bot.auto_rt(wcretw, count= 1 )


# In[ ]:



