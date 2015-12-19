
# coding: utf-8

# gif pokmon
# 
# script to explore the pokemon api and get gifs. 

# In[42]:

import requests
import json
import shutil


# In[29]:

reqg = requests.get('http://pokeapi.co/api/v1/pokedex/1/')


# In[30]:

retxt = reqg.text


# In[31]:

pokload = json.loads(retxt)


# In[32]:

allpok = len(pokload['pokemon'])


# In[36]:

print(pokload['pokemon'][200])


# In[37]:

allpok


# In[ ]:

opwritj = requests.get('http://api.giphy.com/v1/gifs/search?q=' + (pokload['pokemon'][alpo]['name']) + '&api_key=dc6zaTOxFJmzC')


# In[43]:

for alpo in range(allpok):
    print(pokload['pokemon'][alpo]['name'])
    opwritj = requests.get('http://api.giphy.com/v1/gifs/search?q=' + (pokload['pokemon'][alpo]['name']) + '&api_key=dc6zaTOxFJmzC')
    wrijrd = opwritj.text
    jswri = json.loads(wrijrd)
    jswln = len(jswri['data'])
    for jsw in range(0, jswln):
        if '.gif' in jswri['data'][jsw]['images']['downsized']['url']:
            print(jswri['data'][jsw]['images']['downsized']['url'])
            response = requests.get((jswri['data'][jsw]['images']['downsized']['url']), stream=True)
            with open('/home/wcmckee/Downloads/gify/' + (pokload['pokemon'][alpo]['name']) + str(jsw) + '.gif', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
                del response

