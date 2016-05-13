
# coding: utf-8

# In[11]:

import artcgallery
import nose
import arrow
import os
import getpass
import nikola
import random


# In[ ]:




# In[2]:

#nikola.plugin_categories.Command


# In[3]:

#from nikola.plugin_categories import Command


# In[4]:

#class CommandLicence(Command):
#    name = ("licence")
#    doc_usage = "[options]"
    
#    cmd_options = (
#        {
#            'name' : 'licence',
#            'short' : 'l',
#            'long' : 'licence',
#            'type' : str,
#            'default' : 'ccby',
#            'help' : 'Licence for sit (default: ccby)',
#        }
#    )
#    
#    def _execute(self, options, args):
        
    


# Tests for creating a blog post for artctrl artworks. 
# 
# Ideas on what needs testing:
# 
# Check that directory exists and if not make directory.
# 
# Test making new md file in posts folder
# 
# Test making new meta file in posts folder
# 
# Test copy of png files to galleries folder
# 
# Test writing sorted images from the daily gallery folder to md 
# folder.
# 
# Test writing of meta files 

# In[5]:

timenow = arrow.now()


# In[6]:

myusr = getpass.getuser()


# In[7]:

artgfil = '/home/{}/artcontrolme'.format(myusr)


# In[8]:

timyr = timenow.strftime('y')


# In[9]:

os.getcwd()


# In[12]:

#numbguess = 0 


# In[ ]:




# In[14]:

#def testday():
#    assert artcgallery.DayStuff.getDay() == timenow.strftime('%d')
    
#def testpath():
#    assert os.path.exists(artcgallery.DayStuff.galdayPath())
    
#def testgalpath():
#    assert os.path.exists(artcgallery.DayStuff.galyrPath())
    
#def testdaypath():
#    assert os.path.exists(artcgallery.DayStuff.galdayPath())
    
def testwotyr():
    assert timenow.strftime('%y') == '16'
    
def testartcontrolpath():
    if os.path.exists(artgfil):
        pass   
    
def testpostpath():
    if os.path.exists('{}/posts'.format(artgfil)):
                      pass
        
def testgalpath():
    if os.path.exists('{}/galleries'.format(artgfil)):
        pass

def testyrpath():
    if os.path.exists('{}/galleries/{}'.format(artgfil, timyr)):
        pass
    
def testpathfol():
    if os.path.exists('{}/posts/'.format(artgfil)):
        pass

def testrand():
    assert random.randint(0,9) == 0
    
    
#def testposfo():
    #with open('{}/posts/fooblog.rst'.format(artgfil, 'r')) as foo:
        #pass
        
#def testwritefil():
#    if not os.path.exists('{}/posts/fooblog.rst'.format(artgfil, 'r')) as foo:
#        with open('{}/posts/fooblog.rst', 'w') as fh:
#            fh.write('a new test')


#def testopefil():
#    try:
#        with open('{}/posts/')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



