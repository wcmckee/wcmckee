
# coding: utf-8

# Number Nerd
# 
# Game to test knowledge of numbers. 
# Code based on:
# http://www.nzqa.govt.nz/assets/qualifications-and-standards/qualifications/ncea/NCEA-subject-resources/Digital-Technologies/91076/91076-EXP-Student2-001.pdf
# 
# ncea level one

# In[119]:

import random
import getpass
import giphypop
#from IPython.display import Image
#from IPython.core.display import HTML 

import webbrowser


# Instead of asking for name use getpass and get the username that the user is loged in as. 

# In[120]:

#get username
#username = input('What is your name? ')
theusr = getpass.getuser()
print('''Hello {}, welcome to this game of Number Nerd. 
In this game you will learn to work out which of given set of numbers is the biggest, 
or which is the smallest.'''.format(theusr))


# In[121]:

score = 0


# Generate two random number that are not the same. Instead of using randint use sample instead. 
# 
# Thanks stackoverflow:
# 
# http://stackoverflow.com/questions/22842289/python-generate-n-unique-random-numbers-within-a-range

# In[122]:

ransam = random.sample(range(1,75), 2)


# Random choose whether to ask the user to pick the smallest number or the biggest number, then ask the user these questions until they get 5 points. 

# In[123]:

randchoic = random.randint(0,1)


# In[124]:

smallnum = min(ransam)


# In[125]:

largenum = max(ransam)


# In[126]:

largenum


# In[ ]:

g = giphypop.Giphy()

winres = [x for x in g.search('win')]

wingifz = winres[random.randint(0, len(winres))]


# In[ ]:

failres = [x for x in g.search('fail')]

failgif = winres[random.randint(0, len(failres))]


# In[ ]:

wingifz.media_url


# In[ ]:

failgif.media_url


# Not happy with the if inside a if, plus repeating code with only change being 0/1 and small/bigger. Merge these?

# In[ ]:

if randchoic == 0:
    while True:
        try:
            answer = int(input("Of {} and {}, which number is smaller? ".format(ransam[0], ransam[1])))
            break
        except ValueError:
            print('Please type in one of the given numbers as your answer')
    
    if answer == smallnum:
        score += 1
        
        print('Well done {}! You now have {} points. '.format(theusr, score))
        #Image(url= wingifz.media_url)
        webbrowser.open_new(wingifz.media_url)
        print(wingifz.media_url)
    else:
        print('That is wrong!')
        #Image(url= failgif.media_url)
        print(failgif.media_url)
        webbrowser.open_new(failgif.media_url)


# In[ ]:

failgif.media_url


# In[ ]:

if randchoic == 1:
    while True:
        try:
            answer = int(input("Of {} and {}, which number is biggest? ".format(ransam[0], ransam[1])))
            break
        except ValueError:
            print('Please type in one of the given numbers as your answer')
            
    if answer == largenum:
        score += 1
        print('Well done {}! You now have {} points. '.format(theusr, score))
        #Image(url= wingifz.media_url)
        webbrowser.open_new(wingifz.media_url)

    else:
        #Image(url= failgif.media_url)
        print('That is wrong!')
        webbrowser.open_new(failgif.media_url)


# In[ ]:

#Image(url=wingifz.media_url)


# open web browser to image

# In[ ]:



