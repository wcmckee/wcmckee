# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Visitor Sign System
# 
# This script was created as an altenative to a printed spreadsheet that you use a physical pen to write - date, name, reason, time in, time out. 
# There is a comment book that this could be used to replace also. 
# Currently people write comments in pen on lined refil. Comments 
# The script is basic. It saves the time, date, name, reason, and added in comments as an html page and json object. Archieve of past logins are saved.
# It is split into two scripts. The first wain or whaxlu is used for the login. 
# The second script is whaiout which is the logout script. It takes the output of wain or whaxlu and appends logout data - time, date, and comment.

# <markdowncell>

# Currently I use the script to sign in and out at a early learning centre that I am employed to work 2 hours a day, 5 days a week. 
# It could be applied in any area where you want to keep a record of time, comments, 
# 
# Similarity to twitter. 
# 
# Avatars
# 
# Mention, taging, hashtags
# 
# There is often a line around the sign in/out book.
# 
# Generates summery
# 

# <markdowncell>

# The site was live. It was running on a simple python web server but it worked. The script was exacuted by the Raspberry Pi B+ computer running Debian. Red pixels appeared on the screen, or #543243 if you want to be fussy. 
# Luck had nothing to do with it. Testing was the key.
# 
# The text had rendered. 
# 
# 1. Alfred Bunnings
# 2. 09:00
# 3. 01/Nov/2014
# 4. InfoSec
# 5. everything seems fine
# 
# Charlie MacDonald sat at his desk steering at the monitor. 
# 'Alfred Bunnings, who is this guy?', he thought to himself. 'Jones, get over here and check this for me', Charlie yelled out to his Assistent.
# 'Coming Sir!', a voice sharply replied. 
# Into Charlies office walked Jones. Tall, 6 foot 3. Dark Brown hair, curly and down to his shoulders. On this day his hair was tied up, usually he left it down but today was special.
# 'What's up sir', Jones asked, squinting at the monitor. 
# 'Take a look for yourself', replied Charlie as he stood up. 
# Jones took a seat at Charlies computer station. Charlie paced up and down his office.
# 'Sir, I've seen nothing like this before. What the hell is going on?', Jones asked Charlie.
# Standing still Charlie spoke:
# 'It's a god damn nightmare that is, this Alfred character has breached the networks. We need to find them.'
# 
# Alfred sat on the bus. The same seat he had every day. The bus was old, 50 years old and rust was pealing rom the rail. At least the button still works. He was on his way to visit an old friend, he hasn't seen in five years. Normally lfred drives his car but today was different. He felt like relaxing on the buss.
# His Dell laptop sat on his lap. The desktop enviorment was KDE, running Debian. He dudn't have much running. Two web browser windows, a terminal, and Pithos. On the left split was his IPython Notebook (running locallly), on the right split documation web page that he is following. The terminal window was behind the web page window. A TMUX session was running. The was split into three windows.  Inside the sessoion was The IPython Notebook Kernal running on port 80. One the second window - Motion. This is used to capture save mpeg files from the Dell laptop camera. 
# 
# The Streets were playing on Pithos. Stay Positive. Pithos is a desktop client for Pandora Radio.
# 
# SPIKE INFOSEC
# 
# The sign read. Alfred stood looking up above him. The skyscraper went on for miles. Squinting he could see the peak.
# 
# Today he was here for a job interview. Two days ago he had been sent a message that a position had came up and the company was interested in hiring him. 
# 
# The automate doors opened as he approched them. Inside stood three security guards and a metal detotor. 
# 'Name and reason/person visit', one of the guards asked him. 
# 'Alfred Bunnings, I'm here for a job interview with Janet Pears'.
# The guard typed characters into the computer.
# 'Alright, that seems fine sir', the guard replied'. 'Please make your way down the hall and take the second right on your left'.
# 'Thank you', Afred said as he begain walking down the hallway. 
# 
# Everything was white. The ground, ceiling and floor. He passed the first turn off on the left and kept walking. He reached the second turn and turned left. 
# 
# The colour scheme changed, colours filled the walls. Character and Landscapes scatted the walls. It was painted with a dark naples yellow, red, and a light blue. The backgrounds were blue and the characters and foreground landscapes were yellow and red. 
# 
# Alfred admired the walls as he contined walking down the hallway. At the end of the hallway was a foylor with several desks setup with computers. A woman sat at the further one typing. 
# She looked up and smiled at Alfred.
# 'You must be Alfred', she exampled. 
# Alfred approched her desk and held out he hand to shake it.
# 'I'm Janet', she said - shaking his hand. 'Take a seat Alfred'. 
# 
# Alfred looked back at the sign on the building.
# 
# SPIKE INFOSEC
# 
# Twenty years he had worked there. Today he was moving on, had sold his shares of the company.
# He approched the doors. They opened automatitly. 
# Three security guards stood there. All with very serious looks on their faces.
# 'Morning fellas', Alfred said as he flashed his ID badge and walked down the corodilol. 
# The corodor was still completely white, like the first time he entered the building. 
# He walked down the hallway. Passing the first door on the left, and turning left at the second turn. 
# The murals had changed. The colour scheme had stayed the same but the images had changed. 
# 
# 
# He had plans to create his own Infomation Security company.                                               

# <markdowncell>

# TODO
# 
# html page of page 100 logins/logouts - append all json as one html
# 
# graph of weekly/day hours and how they change.
# 
# work out time between login and logout.
# 
# question that you comment on that includes the sketch daily reddit gets drawn. 
# 
# fake name encription for kids/everyone?
# Take a name and turn into into a new name, run a script again to turn it back
# 
# records time when child eats/drinks
# 
# Sig for parents when signing in/out kids
# 
# txt/email alerts to parents on changes to kids signin/out
# 
# If someone doesnt signin/signout before certain time - alert
# 
# import pandas. Need to free up space on raspberry pi
# 
# Filter - new/popular comments, people, signins, signouts,  
# 
# Date 01 November 2014
# 
# 0000
# 
# Daily Rosted/Working chart. 
# Spread sheet - names colum, time rows.
# 
# example:
#      | Dino1 | Dino2 | Dino3 |
# 
# 0700 | signin + comment!
# 
# 0701 | signout + comment!
# 
# so on..
# 
# Live updates of the floor. 
# Inside, Outside, Inside Float, Outside Float, General Float.
# Tagging. Tag people for breaks. 
# eg - you are busy with a project, but need a break/lunch. Someone tags you and takes over at area. You go for break/lunch. When you return, tag back and carry on.
# The person that was just taged back moves onto the next person to tag for break/lunch.
# This person cycles through a group of people.
# 
# Live updates of child location.
# gps info of each area of centre and count how many children are there. 
# 
# Panic Button. Signal to call for assistence, part-tag, allow for image/sound record. 
# 

# <codecell>

valname = ('lasnam', 'signin', 'usercom', 'dayr', 'htmn')

# <codecell>


# <codecell>

for itzval in valname:
    print itzval

# <markdowncell>

# This function creates a dict, another updates it. 
# Function is working to create it but update is coming back with error.
# 
# How do I refer to the created dict as the one to update?

# <codecell>

class DictNows():

    def dictcreate(keyval, firnam):
        return dict({keyval: firnam})

    def updatedict(keyvalz, othnam):
        return dictcreate.update({keyvalz: othnam})

# <codecell>

checkdict = dictcreate('check', 'this')

# <codecell>

checkdict

# <codecell>

def dictcreate(keyval, firnam):
    return dict({keyval: firnam})

def updatedict(keyvalz, othnam):
    return checkdict.update({keyvalz: othnam})

def returndate():
    return time.strftime(("%d" + "-" + "%b" + "-" + "%Y"))

def returntime():
    return time.strftime("%H:%M:%S")

def returan():
    return os.urandom(16)

def blahblah():
    with open('/home/wcmckee/visignsys/posts/' + ixtwe + '.html', 'w')
    #savpos.write(str(doc))
    #savpos.close()

# <codecell>

updatedict('omg', 'not again')

# <codecell>

returan()

# <codecell>

returntime()

# <codecell>

DictNows.dictcreate('check')

# <codecell>

dictcreate('name', 'wcm')
#updatedict()

# <codecell>

updatedict('checking', 'this works')

# <codecell>

dayr = time.strftime("%d" + "-" + "%b" + "-" + "%Y")
hrmn = time.strftime("%H:%M:%S")

# <codecell>

betdict.update({'lastname': lasnam})
betdict.update({'reason': signin})
betdict.update({'signin-comment': usecom})
betdict.update({'signin-date': dayr})
betdict.update({'signin-hrmin': hrmn})

# <codecell>

betdict.update({'lastname': lasnam})

# <codecell>

for itz in updatedict():
    print itz

# <codecell>

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <h2>visitor sign system</h2>
# 
# This is a python script used to sign in and signout, keeping track of hours and creating a more automative system.
# 
# Make sign in and out faster, easier to keep track of.
# 
# Never forget. 
# 
# Auto roll check. 
# 
# Two random hex codes for security and correct checking. Made use of tthese by using one as file name when saving.
# 
# Creates xls file with data, also uses sqlalchemy for databases, web server, html page: 
# input (or auto) name, reason, auto day/month/year hr/min - of signin.
# 
# when launched asked if you want to signin or signout. 
# 
# how i want this to run for william:
# 
# william arrives into whai. On his phone he runs the signin script. On signing out for the day the script is run onto final part, signout. asks for comment first then records time, and date. 
# 
# comment system. leave comment for staff, parent, tag staff, area, story, parent, child.
# 
# signout - enter code of session you want to signout. 
# 
# Screw the excel file, im just dealing with index page. i am saving achieve in posts folder under urandom 13 character code. 

# <codecell>

import os
import time
import dominate
import sys
from dominate.tags import *
import json

lasnam = raw_input('Last Name: ')
firnam = raw_input('First Name: ')
dopz = raw_input('dob: ')
mname = ('William Mckee')
ename = raw_input('Email: ')
signin = raw_input('Reason: ')

numroll = []

# <codecell>

for det in range(6):
    #print det
    numroll.append(det)

usecom = raw_input('Comments: ')



betdict = {'first': firnam}

# <codecell>

dayr = time.strftime("%d" + "-" + "%b" + "-" + "%Y")
hrmn = time.strftime("%H:%M:%S")

# <codecell>

betdict.update({'lastname': lasnam})
betdict.update({'reason': signin})
betdict.update({'signin-comment': usecom})
betdict.update({'signin-date': dayr})
betdict.update({'signin-hrmin': hrmn})

# <codecell>

betjsn = json.dumps(betdict)

# <codecell>

betjsn


doc = dominate.document(title='Visitor Sign Sheet')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(id='header').add(ol()):
        h1('Visitor Sign Sheet')
        for i in betdict.values():
            li(a(i))

    with div():
        attr(cls='body')
        p('last updated: ' + time.strftime("%H:%M"))
        p('Visitor Sign Sheet is open source')
        a('http://github.com/wcmckee/wcmckee', href='https://github.com/wcmckee/wcmckee')

#print doc

# <codecell>

savindex = open('/home/wcmckee/visignsys/index.html', 'w')

# <codecell>

savindex.write(str(doc))
savindex.close()

# <codecell>
ixran = os.urandom(16)
ixtwe = ixran[0:16]

# <codecell>

savpos = open('/home/wcmckee/visignsys/posts/' + ixtwe + '.html', 'w')
savpos.write(str(doc))
savpos.close()

# <codecell>

savpos = open('/home/wcmckee/visignsys/posts/' + ixtwe + '.json', 'w')
savpos.write(str(betjsn))
savpos.close()

# <codecell>

#savpos = open('/home/wcmckee/visignsys/index.meta', 'w')
#savpos.write(str(wsdict.keys()))
#savpos.close()

# <codecell>

savpos = open('/home/wcmckee/visignsys/index.json', 'a')
savpos.write(str(betjsn))
savpos.close()

print ('sign in complete')

# <codecell>

cat index.json

# <codecell>

opind = open('/home/wcmckee/visignsys/index.json', 'r')
opred = opind.read()

# <codecell>

opred

# <codecell>

opjsnd = json.dumps(opred)

# <codecell>

opjsnd

# <codecell>


