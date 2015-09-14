
# coding: utf-8

# BroBeur Studios
# Web Site.
# 
# All content on one page. Use # to nav between 
# 
# Render latest post from posts folder here. 
# 
# 
# 
# Avable for hirBroBeur Studios was founded in 2013 by William Mckee. It acted as an extension his his 2d art site - artcontrol.me: The Art Of William Mckee. The major goal of BroBeur Studios is to build open source video games.
# During 2013 BroBeur Studios partook in many game jams - releasing the results on BroBeur.com.
# Development slowed in 2014, but still released two games. 
# 
# Games are released with source under a MIT licence/Creative Commons BY. 
# 
# Games are developed either solo or in a small team. 
# 
# Twitter @brobeur
# e. Concept Art, 3d, Game Design.
# 
# Games. Sort games by platform. Android, Windows, Mac, Linux.
# 
# About. 
# 
# BroBeur Studios was founded in 2013 by William Mckee. It acted as an extension his his 2d art site - artcontrol.me: The Art Of William Mckee. The major goal of BroBeur Studios is to build open source video games.
# During 2013 BroBeur Studios partook in many game jams - releasing the results on BroBeur.com.
# Development slowed in 2014, but still released two games. 
# 
# Games are released with source under a MIT licence/Creative Commons BY. 
# 
# Games are developed either solo or in a small team. 
# 
# Twitter @brobeur
# 
# Random Image of The Day from GetsDrawnDotCom
# 
# 
# 
# Majority of games created were for game jams.
# 
# 
# 

# In[1408]:

import dominate
from dominate.tags import *
from time import gmtime, strftime
import getpass
import random
import bs4
import os


# In[1409]:

getusr = getpass.getuser()


# In[1410]:

bbdir = ('/home/wcmckee/bb')


# In[1411]:

logzdir = (bbdir + '/imgs/logo/')


# In[1412]:

bbposts = (bbdir + '/posts/')


# In[1413]:

gamdir = bbdir + '/games/'


# In[1414]:

artctrlf = (bbdir + '/artctrl')


# In[1415]:

artctrlew = (artctrlf + '/logo')


# In[1415]:




# In[1416]:

brobem = ('/var/host/media/removable/lemonyellow/brobeur/')


# In[1417]:

allposts = os.listdir(bbposts)


# In[1418]:

bbscreen = (bbdir + '/imgs/screenshot')


# In[1419]:

allscreen = os.listdir(bbscreen)


# In[1420]:

ranscreen = random.choice(allscreen)


# In[1421]:

fixscrn = ('/imgs/screenshot/' + ranscreen)


# In[1422]:

screedir = (bbscreen + '/' + ranscreen)


# In[1423]:

apos = []


# In[1424]:

for metz in allposts:
    if '.wp' in metz:
        #print metz
        apos.append(metz)


# In[1425]:

ranposz = random.choice(apos)


# In[1426]:

ranmeta = ranposz[:-3] +'.meta'


# In[1427]:

opmeta = open(bbposts + '/' + ranmeta, 'r')

oprdz = opmeta.readlines()


# In[1428]:

tagz = oprdz[3].replace('\n', '')


# In[1429]:

timz = oprdz[2].replace('\n', '')


# In[1429]:




# In[1429]:




# In[1429]:




# In[1430]:

oprzb = open(bbposts + '/' + ranposz, 'r')

rdopz = oprzb.read()


# In[1431]:

bs = bs4.BeautifulSoup(rdopz)


# In[1432]:

bslinkz = bs.find_all('a')


# In[1433]:

bslinkz


# In[1434]:

bslran = random.choice(bslinkz)


# In[1435]:

bslstr = str(bslran)


# In[1436]:

linkf = bs4.BeautifulSoup(bslstr)


# In[1437]:

#sort list of date time from newest to oldest. 


# In[1438]:

'''for mea in allposts:
    if '.meta' in mea:
        file = open(bbposts + mea, 'r')
        metaf = file.readlines()
        apdid.update({metaf[2].rstrip(): metaf[1].rstrip()})#, file.readline()}
        #apdid.update({'title': metaf[1].rstrip()})
        #apdid.update({'date': metaf[2].rstrip()})
        #apdid.update({'tags': metaf[3].rstrip()})
        #print chzdir
        #alldic.append(chzdir)
        file.close()
        print apdid.keys()
        filis.append(apdid.keys())'''


# In[1439]:

bstxt = bs.text.replace('\n', '')


# In[1440]:

logolis = os.listdir(logzdir)


# In[1441]:

ranlogz = random.choice(logolis)


# In[1442]:

opmdz = open(bbdir + '/md/about.md', 'r')


# In[1443]:

mdlis = opmdz.readlines()


# In[1444]:

for mdl in mdlis:
    print mdl


# In[1445]:

aboutmd = opmdz.read().replace('\n', '')


# In[1446]:

rawp = ranposz.replace('.wp', '')


# In[1447]:

brolisd = os.listdir(gamdir)


# In[1448]:

for broa in brolisd:
    if '.apk' in broa:
        #android apk
        print broa


# In[1449]:

for broz in brolisd:
    if '.rar' in broz:
        #mix of windows/linux/osx native.
        print broz


# In[1450]:

for brol in brolisd:
    if '.html' in brol:
        #unity3d web browser games
        print brol


# In[1451]:

#Embed artctrl logo under game lists. use artctrl folder to 
#embed stuff from artcontrol into bb.


# In[1452]:

artctrlloglis = os.listdir(artctrlew)


# In[1453]:

ranarclogis = random.choice(artctrlloglis)


# In[1454]:

ranarclogis


# In[1455]:

navitems = ['home', 'blog', 'games', 'artcontrol', 'getsdrawn']


# In[1456]:

screedir


# In[1457]:

doc = dominate.document(title='BroBeur Studios')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')
    
    with div(id="home"):
        p('BroBeur Studios')
        for navi in navitems:
            with div(cls = 'nav-item', id= 'nav-' + navi):
                a(navi, href = ('#' + navi))
                
        p(' ')
            
        p(a(' BroBeur Twitter ', href = 'http://twitter.com/brobeur', src = 'http://twitter.com/brobeur')) 

        p(img('imgs/logo/' + ranlogz, src='imgs/logo/' + ranlogz))
        p('Updated ', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        #p(panz)
                
        for mdl in mdlis:
            p(mdl)
            

        #p(bodycom)
        p(img(fixscrn, src= fixscrn))
                        
            
        

with doc:
        #for rdz in lisrgc:
            #h1(rdz.title)
            #a(rdz.url)
            #if 'http://i.imgur.com' in rdz.url:
                #print rdz.url
            #   p(img(rdz.url, src='%s' % rdz.url))
                
            #print rdz.url
            #if '.jpg' in rdz.url:
            #    img(rdz.urlz)
            #else:
            #    a(rdz.urlz)
            #h1(str(rdz.author))
            
            #li(img(i.lower(), src='%s' % i))
    #with div():
        #attr(cls='about', id='about')
        #h3('About BroBeur Studios')
        #p(aboutmd)

    with div():
        attr(cls='blog', id='blog')
        h3('BroBeur Studios Random Blog Post')
        p(rawp)
        p(timz)
        p(tagz)
        p(bstxt)
        #p(bslstr)
        p(img(bslran['href'], width="480", height="320", src = bslran['href']))
        
    with div():
        attr(cls='games', id='games')
        h3('Open Source Games')
        
        h3('Android')
        for broa in brolisd:
            if '.apk' in broa:
            #android apk
                p(p(a(broa, href= '/games/' + broa)))
                
        h3('Unity Webplayer')
        for brol in brolisd:
            if '.html' in brol:
                #unity3d web browser games
                p(p(a(brol, href = '/games/' + brol)))
                
        h3('Desktop')
        for broz in brolisd:
            if '.rar' in broz:
                #mix of windows/linux/osx native.
                p(p(a(broz, href = '/games/' + broz)))
                #p(broz)

                
    with div():
        attr(cls='artcontrol', id='artcontrol')
        h3('artcontrol')
        
        #p(img('imgs/logo/' + ranlogz, src='imgs/logo/' + ranlogz))

        p(img('/artctrl/logo/artctrl-logo.png', src = '/artctrl/logo/artctrl-logo.png', href = 'http://artcontrol.me'))
        
        p('A preview of ArtControl: The Art Of WCMCKEE')
        
        p(p(a('Visit ArtControl: The Art Of WCMCKEE', href='http://artcontrol.me/')))

        p(img('artctrl/artctrlpers.png', src = 'artctrl/artctrlpers.png')) 
        
        
    with div():
        attr(cls='GetsDrawn', id='getsdrawn')
        h3('GetsDrawn')
        
        p('A preview of GetsDrawn')

        
        
        #List of published games on google play store.
        #link to their github.
        #Download apk/linux/web embed
    
#print doc


# In[1458]:

indfil = (bbdir + '/index.html')


# In[1459]:

docre = doc.render()

yourstring = docre.encode('ascii', 'ignore').decode('ascii')

mkind = open(indfil, 'w')
mkind.write(yourstring)
mkind.close()


# In[1459]:




# In[1459]:




# In[1459]:




# In[1459]:




# In[1459]:



