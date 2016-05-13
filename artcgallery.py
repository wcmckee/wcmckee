
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

# In[3]:

import os
import arrow
import getpass


# In[50]:

raw = arrow.now()
myusr = getpass.getuser()
galpath = ('/home/{}/git/artcontrolme/galleries/'.format(myusr))

galpath = ('/home/{}/git/artcontrolme/galleries/'.format(myusr))
  
popath = ('/home/{}/git/artcontrolme/posts/'.format(myusr))
    


# In[ ]:




# In[51]:

class DayStuff():
    def getUsr():
        return getpass.getuser()

    def reTime():
        return raw()

    def getYear():
        return raw.strftime("%Y")

    def getMonth():
        return raw.strftime("%m")

    def getDay():
        return raw.strftime("%d")

    def Fullday():
        return (getYear() + '/' + getMonth() + '/' + getDay())

    def fixDay():
        return (raw.strftime('%Y/%m/%d'))

    #def postPath():
        #return ('/home/{}/git/artcontrolme/posts/'.format(myusr))

    
    def listPath():
        return os.listdir(popath)

    #def galleryPath():
    #    return (galpath)

    def galyrPath():
        return ('{}{}'.format(galpath, getYear()))
    
    def galmonPath():
        return('{}{}/{}'.format(galpath, getYear(), getMonth()))
    
    def galdayPath():
        return('{}{}/{}/{}'.format(galpath, getYear(), getMonth(), getDay()))
    
    def galleryList():
        return os.listdir('/home/{}/git/artcontrolme/galleries/'.format(myusr))
    
    def galyrList():
        return os.listdir('/home/{}/git/artcontrolme/galleries/{}/{}'.format(myusr, getYear()))

    def galmonList():
        return os.listdir('/home/{}/git/artcontrolme/galleries/{}/{}'.format(myusr, getYear(), getMonth())) 
    
    def galdayList():
        return os.listdir('/home/{}/git/artcontrolme/galleries/{}/{}/{}'.format(myusr, getYear(), getMonth(), getDay()))    
    

    def checkYear():
        if getYear() not in galleryList():
            return os.mkdir('{}{}'.format(galleryPath(), getYear()))


    def checkMonth():
        if getMonth() not in DayStuff.galyrList():
            return os.mkdir('{}{}'.format(galleryPath(), getMonth()))
        
    def checkDay():
        if getDay() not in DayStuff.galmonList():
            return os.mkdir('{}/{}/{}'.format(galleryPath(), getMonth(), getDay()))
        
    #def makeDay



# In[44]:

#DayStuff.getUsr()


# In[45]:

#DayStuff.getYear()


# In[46]:

#DayStuff.getMonth()


# In[47]:

#DayStuff.getDay()


# In[48]:

#DayStuf


# In[49]:

#DayStuff.Fullday()


# In[26]:

#DayStuff.postPath()


# In[ ]:

#DayStuff.


# In[7]:

#DayStuff.galmonPath()


# In[226]:

#DayStuff.galdayPath()


# In[ ]:




# In[159]:

#DayStuff.galyrList()


# In[157]:

#getDay()


# In[160]:

#getMonth()


# In[161]:

#galleryList()


# In[156]:

#DayStuff.checkDay()


# In[ ]:




# In[ ]:




# In[166]:

#DayStuff.galyrList()


# In[148]:

#DayStuff.galmonList()


# In[ ]:




# In[145]:

#DayStuff.checkDay()


# In[ ]:

#DayStuff.checl


# In[150]:

#DayStuff.checkMonth()


# In[149]:

#DayStuff.galyrList()


# In[ ]:




# In[117]:

#listPath()


# In[122]:

#if getYear() not in galleryList():
#    os.mkdir('{}{}'.format(galleryPath(), getYear()))


# In[113]:

#galleryPath()


# In[102]:

#fixDay()


# In[103]:

#galleryPath()


# In[104]:

#Fullday()


# In[105]:

#getDay()


# In[106]:

#getYear()


# In[107]:

#getMonth()


# In[108]:

#getusr()


# In[48]:

#yraw = raw.strftime("%Y")
#mntaw = raw.strftime("%m")
#dytaw = raw.strftime("%d")


# In[49]:

#fulda = yraw + '/' + mntaw + '/' + dytaw


# In[50]:

#fultim = fulda + ' ' + raw.strftime('%H:%M:%S')


# In[51]:

#arnow = arrow.now()


# In[52]:

#curyr = arnow.strftime('%Y')


# In[53]:

#curmon = arnow.strftime('%m')


# In[54]:

#curday = arnow.strftime('%d')


# In[55]:

#galerdir = ('/home/wcmckee/github/artcontrolme/galleries/')


# In[73]:

#galdir = os.listdir('/home/wcmckee/github/artcontrolme/galleries/')


# In[74]:

#galdir


# In[75]:

#mondir = os.listdir(galerdir + curyr)


# In[76]:

#daydir = os.listdir(galerdir + curyr + '/' + curmon )


# In[77]:

#daydir


# In[78]:

#galdir#


# In[79]:

#mondir


# In[80]:

#daydir


# In[81]:

#if curyr in galdir:
#    pass
#else:
#    os.mkdir(galerdir + curyr)


# In[82]:

#if curmon in mondir:
#    pass
#else:
#    os.mkdir(galerdir + curyr + '/' + curmon)


# In[83]:

#fulldaypath = (galerdir + curyr + '/' + curmon + '/' + curday)


# In[84]:

#if curday in daydir:
#    pass
#else:
#    os.mkdir(galerdir + curyr + '/' + curmon + '/' + curday)


# In[85]:

#galdir


# In[86]:

#mondir


# In[87]:

#daydir


# In[88]:

#str(arnow.date())


# In[90]:

#nameofblogpost = input('Post name: ')


# check to see if that blog post name already excist, if so error and ask for something more unique! 
# 
# input art piece writers. Shows the art then asks for input, appending the input below the artwork. Give a name for the art that is appended above. 

# In[94]:

#daypost = open('/home/{}/github/artcontrolme/posts/{}.md'.format(getusr(), nameofblogpost), 'w')


# In[95]:

#daymetapost = open('/home/{}/github/artcontrolme/posts/{}.meta'.format(getUsr(), nameofblogpost), 'w')


# In[ ]:




# In[69]:

#daymetapost.write('.. title: ' + nameofblogpost + ' \n' + '.. slug: ' + nameofblogpost + ' \n' + '.. date: ' + fultim + ' \n' + '.. author: wcmckee')


# In[70]:

#daymetapost.close()


# In[71]:

#todayart = os.listdir(fulldaypath)


# In[72]:

#titlewor = list()


# In[73]:

#titlewor


# ![themilkcollective-line](/galleries/2015/10/themilkcollective-line.png)

# In[74]:

#galpath = ('/galleries/' + curyr + '/' + curmon + '/' + curday + '/')


# In[75]:

#galpath


# In[76]:

#todayart.sort()


# In[77]:

#todayart


# In[78]:

#for toar in todayart:
#    daypost.write(('!' + '[' + toar.strip('.png') + '](' + galpath + toar + ')\n'))


# In[79]:

#daypost.close()

