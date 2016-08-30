
# coding: utf-8

# TwitFol
# 
# script to send tweet from random list of subreddits containing a random submission of the subreddit.
# 
# Also searches twitter for something containing a hashtag of gamejams currently happening etc.

# In[1]:

from TwitterFollowBot import TwitterBot
import requests
import json
import praw
import random


# In[2]:

#bb_bot = TwitterBot('/home/wcmckee/brobeur-tweet/brobeur.txt')


# In[102]:

wcm_bot = TwitterBot('/home/pi/bro-tweet/config.txt')


# In[103]:

r = praw.Reddit(user_agent='wcmckeepython')


# In[104]:

wcmretw = ['#gamedev', '#ludumdare', '#android', '#gaming', '#pokemon', '#uncharted', '#unity3d']


# In[105]:

randhab = random.choice(wcmretw)


# In[ ]:




# In[ ]:

wcmbots = wcm_bot.search_tweets(randhab, count=1)


# In[83]:

wcmbots['search_metadata']


# In[ ]:




# In[84]:

mylist = list()
hashlist = list()


# In[85]:

mylist.append(wcmbots['statuses'])


# In[86]:

for myl in mylist:
    myle = len(myl[0]['entities']['hashtags'])
    for mya in range(myle):
        print(myl[0]['entities']['hashtags'][mya]['text'])
        hashlist.append((myl[0]['entities']['hashtags'][mya]['text']))


# In[87]:

hashlist


# In[98]:

hashlist


# In[5]:

wcmsubreds = ['writing', 'gaming', 'InternetIsBeautiful', 'Minecraft', 'skyrim', 'linux', 'opensource', 'warcraft']


# In[6]:

#scribred = ['writing', 'gaming', 'InternetIsBeautiful', 'Minecraft', 'skyrim', 'linux', 'opensource', 'warcraft']


# In[7]:

wcmrasub = random.choice(wcmsubreds)


# In[8]:

hashwcm = ('#' + wcmrasub)


# In[9]:

#randscr = random.choice(scribred)


# In[10]:

#hashse = ('#' + randscr)


# In[11]:

#getnewr = r.get_subreddit(randscr)


# In[12]:

#randscr


# In[13]:

getwcms = r.get_subreddit(wcmrasub)


# In[14]:

getwcms


# In[15]:

twcm = getwcms.get_random_submission()


# In[16]:

wtit = twcm.title


# In[83]:

wurl = twcm.url


# In[84]:

wjson = twcm.json_dict


# In[86]:

wurl


# In[87]:

hashpy = ('#{}'.format(wcmrasub))


# In[88]:

sublen = len(hashpy)


# In[89]:

sublen


# In[90]:

matot = 139 - sublen


# In[91]:

matot


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

#wcmsendtw = wcm_bot.send_tweet('{} {} {}'.format(wtit, wurl, hashwcm)) 


# In[ ]:




# In[25]:

#wcm_bot.send_tweet(wtit + ' ' + wurl + ' ' + hashwcm)


# In[26]:

#for getr in getnewr:
#    print (getr)


# In[55]:

#getrsub = getnewr.get_random_submission()


# In[56]:

#gtia = getrsub.title


# In[57]:

#gurl = getrsub.url


# In[58]:

#bb.send_tweet(gtia + ' ' + gurl + ' ' + hashse)


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


# In[52]:

ranhash = random.choice(hashlist)


# In[66]:

#tweval = ['#gamedev', '#ludumdare', '#1GAM', '#gaming', '#gta', '#uncharted', '#unity3d', ]


# In[78]:

#bbranrt = random.choice(tweval)


# In[53]:

wcretw = random.choice(ranhash)


# In[ ]:




# In[54]:

#bb_bot.auto_rt(tweval, count = 1 )


# In[55]:

wcm_bot.auto_rt(wcretw, count= 1 )


# In[ ]:



