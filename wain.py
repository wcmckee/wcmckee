# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os
import time
import dominate
import sys
from dominate.tags import *
import json

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
# 'Alfred Bunnings, who is this guy?', he thought to himself. 'Jones, get over here and see this', Charlie yelled out to his Assistent.
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
# The guard typed characters into the comput
# 'Alright, that seems fine sir', the guard replied'. 'Please make your way down the hall and take the second right on your left'.
# 'Thank you', Afred said as he begain walking down the hallway. 
# 
# Everything was white. The ground, ceiling and floor. He passed the first turn off on the left and kept walking. He reached the second turn and turned left. 
# 
# The colour scheme changed, colours filled the walls. Character and Landscapes scatted the walls. It was painted with a dark naples yellow, red, and a light blue. The backgrounds were blue and the characters and foreground landscapes were yellow and red. 
# 
# Alfred admired the walls as he contined walking down the hallway. At the end of the hallway was a foylor with several desks setup with computers. A woman sat at the further one typing. 
# The foylar was plainer than the hallway. Art murels still scatted the area, but they were less freuent. The are had a light blue background, with yellow and red character and landscape artwork. 
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
# Three security guards stood there. All with very serious looks on their faces. Unlike the day he walked into the building for a job interview the guards were humanoild shaped robots. The guard looked and sounded like the same security guards on that first day. Under their fake human skin was just metal and wires.  
# 'Morning fellas', Alfred said as he flashed his ID badge and walked down the corodilol. 
# The corodor was still completely white, like the first time he entered the building. 
# He walked down the hallway. Passing the first door on the left, and turning left at the second turn. 
# The murals had changed. The colour scheme had stayed the same but the images had changed. Alfred had contrubited several times to the repainting of the murals. It was a annual event, each year five people are awarded with the job of recreating the murals. 
# He wondered down the colourful hallway. During his third year working for Spike Infosec he won along with four other people - Noel Locksmart, Elizebeth Goodwill, Trist Gardens, and Ali Turbon. Individially they started by working on sketches. 
# He reached the foylor - desks with computers scatted the foylor. This was the main room where people worked. It was an open space, and the desks had wheels on so they were able to be moved around the building freely. There were several breakoff rooms where smaller groups could go to work.
# 
# Alfred scanned the room. People filled the desks. Sitting or standing they typed. 
# 'Today is special', a familar voice for Alfred sounds from behind a monitor.
# Janets face poped out, with a smile. 
# 'Goodmorning Janet', Alfred smiled.
# Janet rose from her chair.
# 'Time for a coffee I believe', she said.
# Janet hadn't aged a day since Alfred met her. She had long straight brunette hair. Light complection skin, with frekles covering her face. She wore skinny horozonal glasses that had a light blue tint. On this day she wore a long silky dress. Her black leather jacket was spread out over the back of her computer chair. 
# On her desk sat three wireless 22 inch monitors. 
# 
# The ground that Janet walked on was rough. Stones cut into her barefeet. The sun blinded her view, she held her arm above her eyes. Attempting to block out the rays. 
# A figure amurged in the distance.. Squinting she made haste towards the figure. As she drew closer she noticed the figure was a copy of herself. A clone. 
# 'You must be Janet', Janet exampled.
# 
# The number generater returned Noel Locksmart, Elizebeth Goodwill, Trist Gardens, and Ali Turbon. They were inserted into the text in order. Identitys were created. Credit Cards were the main source. Creating a fake identity and building up depit, and not paying it back. 
# Janet scanned the card. Elizebeth Goodwill it the name on the license read. Born 06/11/2014. Spike Infosec: Help Desk 4. The photo was of a straight hair brunete in her early 20s, with frekles covering her face, petite.
# The room reveled a server room with walkways. 
# Goodwill plugged the patch cable from the Vodafone router. Connected on the otherside was a Raspberry Pi. A green and yellow light turned on by the ethernet port. It had a network. For development and testing Elizebeth perfered to use her own network connection. 
# Truck skretched to a halt on the street. Three toots. Both truck doors opened and two men leaped out. They begain walking towards the propatery at the end of the street. 
# Goodwill could hear several people moving about outside. 
# The drone showed three people exiting the truck. Two men and a woman. As they scretched to a halt outside the house of Elizebeth Goodwill, was in fact Janet lived there. It was a setup. The house was trapped so that when they entered - they were never going to leave again. 
# Thirty years Noel Locksmart had been a prisnor in the house. He will never forget the night. It was just a standard robbery. Locksmart had recieved word of a computer scientice by the name of Elizebeth Goodwill that had developed software that allowed the replaying of events in the past. The system was complex but started with just one script when Goodwill was in her early twentys. It was a login and logout script. The first script was the login script. This created a JSON object that included firstname, lastname, date (04/Nov/2014), time (hr:min), reason, and comment. The logout script added to the JSON object logout date, time, and comment. 
# 
# Ali Turbon wislied as he mixed the Indian spice together. Pandora radio was playing from his bluetooth speaker. It was on the family dinner table. Next to the speaker was a nonbranded laptop running Fedora. KDE was the desktop enviorment. Firefox was open with a IPython Notebook on the screen. This window was on the left side of the monitor. On the right top side of the monitor a television show played. It was   George Benson played. 'Onions are ready to go, confirm? Y/n', a device in Turbon's left chefs jacket beeped. Turbon reached for his phone and hit enter. Three claws reached inside the cubord and picked up an onion each. The bench was a woodern bench. The claws dropped the onions on the bench then went back to the cubard to collect more onions. Several more trips back and forward then the claws switched into the next phase - cutting of the onion. The onions were lined up perfectly on the bench. Three rows, five collums. Fifteen onions. Chef knives snapped out of the claws of the device and started to cut up the onions. Each onion was cut in half, then quarters, and finally sliced. The onions were scopped up and droped into a pan of oil to fry. Once the onions were a lovely gold color they were tiped into a slow cooker. 
# 'Carrots are ready to go, confirm? Y/n', the device The claws grabbed a orange carrot and dropped it on the bench. The same amount of carrots were used as onions. The knives cut the carrots by a slice lengthways in half, then quarters, and finally slicing. Scopped up by the claws they are dropped in a pan to be fried with oil. Once goldern the carrots are tipped into the slow cooker. Fifteen cups of soft chickpeas are tipped into the pan of oil and fried. They are tipped into the slow cooker. Fifteen medium sized tomatoes travel through the room, being griped by the claw. They are crushed and tipped into the slowcooker.  
# Five tea spoons of Indian spice mix is tipped into the slowcooker. 
# 'Coconuts are ready to go, confirm? Y/n', beeped the device in Turbons hand. Enter was hit. The claws moved towards the cubard to retreave the coconuts. Seven medium sized ripe coconuts are dropped on the woodern bench. The knife snaps out of the claw and cuts the coconut clean in half. The claw snaps the knife away and revieles a sharp scoop. The white coconut insides are cut, scooped and tiped into the slowcooker.
# 'Item ready to cook. Is there anything else?', the device spoke. 
# The voice was that of Trist Gardens. Her voice was sharp and clear. She spoke with confidence and joy. 
# 'Fifteen garlic and salt', Turbon requested.
# 'Garlic are ready to go, confirm Y/n', the device beeped. Turbon slammed the enter key. The claws moved to the cubards and dragged out fifteen cloves of garlic. The knives snapped out and sliced it up finely. Garlic was scooped up and tipped into the slow cooker. 
# 'Salt is ready to go, conf', before the device had finished beeping Tubon hit the enter key. Salt was tipped into the slow cooker. 
# 'Item read to cook. Is there anything else?', Gardens voice asked. 
# 'Confirm', Turbon confirmed. 
# The claws began mixxing the slowcooker mixture together. Turbon had a late order for a chickpea curry that he was putting though last mintute. 
# It was a Sunday night and he had a client that wanted a Chickpea Curry for lunch on Monday despritly. Normally he charges extra for weekend food orders but this night he made an exception. This client was special and he knew business would be better in the future because of it. 
# A raspberry Pi and Audino powered his commucial resturont cooking device. His cellphone was connected to the raspberry pi computer that was connected to the Audino. The laptop was his portable devlopment machine. 
# Turbon pressed a button a door opened. Server room with racks of servers running. small selfdriving cars moved up and down the hallway. The cars were careful to avoid Turbon as he walled down the hallway. He nodded at each car as they passed by. 
# The cars had no wheels and moved along the ground by twisting. They moved along with the awkward twist movement. Rubberlike commpletion. Majority of the cars were a yellow and red colour scheme. Several had grayscale colour scheme and traveled in groups of three to five. The grayscale moved slower than the colour scheme and was quick to move out the way when one was heading towards them.
# Turbons reached a door. It was a large door, double his height. He banged at the door three times.
# The device in his pocket beeped, 'door status: open'.
# Turbon turned the handle and opened the door. He stepped into the room. Mid gray covered the room. A dark shape sat in the corner, reading a newspaper. 
# Turbon paused as his eyes noticed the black shape. he was pulled closer and began walking towards the shape. He stood in front of the shape.
# 'Chickpea Curry is ready to go, confirm Y/n', Turbons spoke. 
# A page of the newspaper was flicked over. Turbon waited, frozen.
# 'Confirm', a sound came from the black shape. The voice was that of Trist Gardens. She still continued to read the newspaper. 
# Turbons dropped sixteen bags of curries. In each bag were 5 trays of curry. Eighty trays of curry in total. Every tray of curry also came with a tray of rice. Turbon dropped another sixteen bags. In each of these bags were 5 trays of rice.
# 'Enjoy your curry', Turbons said. 
# 'Thank you', the voice of Gardens replied. 
# The dark shape placed the newspaper beside them and 
# 
# Charlie MacDonald. Rest in Peace. The grave stone read. Born 24 October 2014. Died 12 December 2093. Trist Gardens stood over the grave. Tears flowing from her eye. It had been two months since MacDonald passed away. She had worked with him for fifteen years at Spike InfoSec. Together they worked on a automatic cooking device. It was used in billions of home and businesses around the world. Spike InfoSec realeased blueprints of the device so anyone with a 3d printer can just print the device. 
# 
# Drone hovered by MacDonalds head. The claw was attached to a woodern board. MacDonald placed a onion on the board. 
# 'Cut', he spoke clearly. 
# 'Confirm', the device beeped back.
# A knive snapped out of the claw and sliced the onion in half. 
# A smile rose on MacDonalds face. 
# 'Jones, get over here and see this'. The door opened and Jones walked towards MacDonald. 
# 'What is it sir?', Jones asked.
# 'Watch this Jones', MacDonald said as he placed a onion on the woodern board.
# 'Cut', he spoke once again. 
# 'Confirm', the device deeped back. 
# The knife snapped out. The onion was sliced clean in half.
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

#checkdict = dictcreate('check', 'this')

# <codecell>

#checkdict

# <codecell>

def dictcreate(keyval, firnam):
    return dict({keyval: firnam})

#def updatedict(keyvalz, othnam):
#    return checkdict.update({keyvalz: othnam})

def returndate():
    return time.strftime(("%d" + "-" + "%b" + "-" + "%Y"))

def returntime():
    return time.strftime("%H:%M:%S")

def returan():
    return os.urandom(16)

#def blahblah():
    #open('/home/wcmckee/visignsys/posts/' + ixtwe + '.html', 'w')
    #savpos.write(str(doc))
    #savpos.close()
    
    

# <codecell>


# <codecell>

#updatedict('omg', 'not again')

# <codecell>

returan()

# <codecell>

returntime()

# <markdowncell>

# DictNows.dictcreate('check')

# <codecell>

dictcreate('name', 'wcm')
#updatedict()

# <codecell>

#updatedict('checking', 'this works')

# <codecell>

lasnam = raw_input('Last Name: ')
firnam = raw_input('First Name: ')
dopz = raw_input('dob: ')
mname = ('William Mckee')
ename = raw_input('Email: ')
signin = raw_input('Reason: ')
usecom = raw_input('Comments: ')

# <codecell>

#bitdict = 

# <codecell>

betdict = {'first-name': firnam}

# <codecell>

#betdict.update({'lastname': lasnam})

# <codecell>

dayr = time.strftime("%d" + "-" + "%b" + "-" + "%Y")
hrmn = time.strftime("%H:%M:%S")

# <codecell>

betdict.update({'last-name': lasnam})
betdict.update({'reason': signin})
betdict.update({'signin-comment': usecom})
betdict.update({'signin-date': dayr})
betdict.update({'signin-hrmin': hrmn})

# <codecell>

betdict

# <codecell>

betjsn = json.dumps(betdict)
betjsn

# <codecell>

#for itz in updatedict():
#    print itz

# <codecell>

opind = open('/home/wcmckee/visignsys/index.json', 'r')
opred = opind.read()

# <codecell>

opred

# <codecell>

opjsnd = json.dumps(opred)

# <codecell>

str(opjsnd)

# <codecell>


# <codecell>

#json.load(opred)

# <codecell>


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
        p(opred)
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


