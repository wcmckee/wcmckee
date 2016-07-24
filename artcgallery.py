
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
# need to read a config file which lists the blog to update. 
# 
# 

# In[147]:

import os
import arrow
import getpass
import shutil


# In[148]:

myusr = getpass.getuser()


# In[149]:

myusr


# In[150]:

raw = arrow.now()


# In[151]:

yraw = raw.strftime("%Y")
mntaw = raw.strftime("%m")
dytaw = raw.strftime("%d")


# In[152]:

fulda = yraw + '/' + mntaw + '/' + dytaw


# In[153]:

fultim = fulda + ' ' + raw.strftime('%H:%M:%S')


# In[154]:

arnow = arrow.now()


# In[155]:

curyr = arnow.strftime('%Y')


# In[156]:

curmon = arnow.strftime('%m')


# In[157]:

curday = arnow.strftime('%d')


# In[158]:

artctrlpath = '/home/{}/git/artctrl/'.format(myusr)


# In[197]:

galerdir = ('{}galleries/'.format(artctrlpath))


# In[198]:

galdir = os.listdir(galerdir)


# In[208]:

if curyr in galdir:
    pass
else:
    os.mkdir(galerdir + curyr)


# In[202]:

mondir = os.listdir(galerdir + curyr)


# In[209]:

if curmon in mondir:
    pass
else:
    os.mkdir(galerdir + curyr + '/' + curmon)


# In[210]:

fridpath = ('{}{}/{}/{}').format(galerdir, curyr, curmon, curday)


# In[211]:

fridpath


# In[212]:

fulldaypath = (galerdir + curyr + '/' + curmon + '/' + curday)


# In[213]:

#fulldaypath


# In[203]:

daydir = os.listdir(galerdir + curyr + '/' + curmon )


# In[214]:

if curday in daydir:
    pass
else:
    os.mkdir(galerdir + curyr + '/' + curmon + '/' + curday)


# In[215]:

galdir


# In[216]:

mondir


# In[217]:

daydir


# In[218]:

str(arnow.date())


# In[219]:

nameofblogpost = input('Post name: ')


# check to see if that blog post name already excist, if so error and ask for something more unique! 
# 
# input art piece writers. Shows the art then asks for input, appending the input below the artwork. Give a name for the art that is appended above. 

# In[220]:

daypost = ('{}posts/{}.md'.format(artctrlpath, nameofblogpost))


# In[221]:

daypost


# In[222]:

daymetapost = ('{}posts/{}.meta'.format(artctrlpath, nameofblogpost))


# In[223]:

daymdpost = ('{}posts/{}.md'.format(artctrlpath, nameofblogpost))


# In[224]:

#daypost = open('{}/posts/{}.md'.format(artctrlpath, nameofblogpost), 'w')


# In[225]:

#daymetapost = open('{}/posts/{}.meta'.format(artctrlpath, nameofblogpost), 'w')


# In[226]:

#with open(daymetapost, 'w') as daympo: 
#    daympo.write('.. title: ' + nameofblogpost + ' \n' + '.. slug: ' + nameofblogpost + ' \n' + '.. date: ' + fultim + ' \n' + '.. author: wcmckee')


# In[227]:

with open(daymetapost, 'w') as daympo: 
    daympo.write('.. title: {} \n.. slug: {} \n.. date: {} \n.. author: {}'.format(nameofblogpost, nameofblogpost, fultim, myusr))


# In[228]:

#daymetapost.write('.. title: ' + nameofblogpost + ' \n' + '.. slug: ' + nameofblogpost + ' \n' + '.. date: ' + fultim + ' \n' + '.. author: wcmckee')


# In[229]:

#daymetapost.close()


# In[230]:

#mediapath = ('/media/removable/USB Drive/artnew/* {}'.format(fridpath))


# In[233]:

#mediapath


# In[258]:

newartlis = os.listdir('/media/removable/USB Drive/newart')


# In[263]:

for newar in newartlis:
    shutil.copy('/media/removable/USB Drive/newart/{}'.format(newar), fridpath)
    


# Copy images from folder to galleries path. Needs to cp files that on usb drive across OR copy from network. 

# In[265]:

#shutil.copyfile('/media/removable/USB Drive/artnew/*.png', fridpath)


# In[266]:

todayart = os.listdir(fulldaypath)


# In[267]:

titlewor = list()


# In[268]:

titlewor


# ![themilkcollective-line](/galleries/2015/10/themilkcollective-line.png)

# In[269]:

#galpath = ('/galleries/' + curyr + '/' + curmon + '/' + curday + '/')


# In[270]:

gallerpath = ('/galleries/{}/{}/{}/'.format(curyr, curmon, curday))


# In[271]:

gallerpath


# In[272]:

#galpath


# In[273]:

todayart.sort()


# In[274]:

todayart


# In[275]:

with open(daymdpost, 'w') as daymark:
    for toar in todayart:
        daymark.write('![{}]({}{})\n'.format(toar.strip('.png'), gallerpath, toar))


# In[276]:

#for toar in todayart:
#    daypost.write(('!' + '[' + toar.strip('.png') + '](' + galpath + toar + ')\n'))


# In[277]:

#daypost.close()

