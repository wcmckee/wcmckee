
# coding: utf-8

# In[36]:

from TwitterFollowBot import TwitterBot
import requests
import json
import praw
import random
my_bot = TwitterBot()


# In[ ]:




# In[ ]:




# In[101]:

r = praw.Reddit(user_agent='wcmckeepython')


# In[112]:

scribred = ['python', 'programming', 'web_design', 'coding', 'hacking', 'opensource', 'compsci']


# In[113]:

randscr = random.choice(scribred)


# In[114]:

hashse = ('#' + randscr)


# In[115]:

hashse


# In[ ]:




# In[116]:

getnewr = r.get_subreddit(randscr)


# In[117]:

#for getr in getnewr:
#    print (getr)


# In[118]:

getrsub = getnewr.get_random_submission()


# In[119]:

gtia = getrsub.title


# In[ ]:




# In[120]:

gurl = getrsub.url


# In[ ]:




# In[121]:

my_bot.send_tweet(gtia + ' ' + gurl + ' ' + hashse)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[3]:

#reqjok = requests.get('http://tambal.azurewebsites.net/joke/random')


# In[4]:

#jsjok = reqjok.text


# In[5]:

#dicjok = json.loads(jsjok)


# In[ ]:




# In[6]:

#str(dicjok.values())


# In[92]:

#for dicv in dicjok.values():
#    print (dicv)
#    my_bot.send_tweet(dicv)


# In[ ]:




# In[73]:

#my_bot.sync_follows()


# In[9]:

#my_bot.auto_unfollow_nonfollowers()


# In[88]:

my_bot.auto_follow_followers()


# In[89]:

mybowp = my_bot.search_tweets('wordpress')


# In[90]:

mybp = mybowp['statuses'][0]['user']['screen_name']


# In[91]:

my_bot.send_tweet('@' + mybp + ' ' + 'Check out Nikola - secure and simple unlike Wordpress ' + 'https://getnikola.com/')


# In[ ]:




# In[13]:

sectalk = my_bot.search_tweets('blackhat2015')


# In[95]:

sectalk['search_metadata']


# In[128]:

sectalk['statuses'][0]


# In[ ]:




# In[ ]:




# In[ ]:




# In[125]:

sectalk


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[100]:

my_bot.auto_follow("#hackfest")


# In[ ]:




# In[ ]:



