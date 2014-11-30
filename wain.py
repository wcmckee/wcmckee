# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os
import time
import dominate
import sys
from dominate.tags import *
import json
import pandas as pd

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
# Janet hadn't aged a day csince Alfred met her. She had long straiht brunette hair. Light complection skin, with frekles covering her face. She wore skinny horozonal glasses that had a light blue tint. On this day she wore a long silky dress. Her black leather jacket was spread out over the back of her computer chair. 
# On her desk sat three wireless 22 inch monitors. One keyboard. One mouse. One drawing tablet. One tablet pen. 
# Janet spent her days at work either coding or digital painting. She had the freedom to choose. If she didn't feel like painting that day, she could code instead.
# Her paintings were quick. Nothing took more than 45 mins. She was working on a logo. 'Spike InfoSec' it read. A furry spikey character held the sign. It's long sloopy tail weiving between the rocks on the ground. The software used for the digital painting was GIMP. Like all software developed and used by Spike InfoSec it is open source and free. 
# 
# The dinosaur roared as Alfred held a large piece of steak. It's nose drew near and sniffed. 
# 'Smells delicious', the dinosaur thought to itself.
# Alfred pushed the meat closer to the dinos nostrols. It spat green slime at Alfred and turned it's back and left in a huff.
# Jsnet hid in the bush nearby waiting for the dino to move out of sight. Alfred was covered in a green slime liquid. It had caused his body to go into shock and shutdown. 
# Janet had to reach Alfred and reboot his system. She creeped closer to Alfreds still body. The dino sniffed the air. Janet stopped moving frozen. The dino continued walking. Janet rushed towards Alfred and grabbed his body. The Dino looked back and saw her moving away. He turned and bagan to give chase to Janet and Alfred. Scrabbambing up a tree Janet was safe from the dino. She had saved Alfred. The dino growed and circed the tree. It scratched the bark from the tree as it grew inpatienct. 
# Janet reached for her backpack and revealed a cellphone. She dialed the number 6 3  2 1 4 5 1. Suddently the dino froze, it had been shutdown. Janet climbed down the tree, still holding onto Alfreds lifeless body. She stepped over the dinos body. Lifeless but the dino never was alive. It was another machine created to hunt her down. She had created them to help people, to make peoples lives easier. But they took her ideas and created evil. The Dark Shape was created by them. Janet never programmed her robots to kill people but others had taken the software and added kill commands. It had created great evil in the universe. 
# 
# The planet Earth population had dropped to just a few thousand people in a matter of days. The machines released a toxin into the oxagin which caused the humans to choke to death. It was a quick death, but it spread quickly and was extremely contagious. Within an hour of the toxin being released half of the worlds population was dead. Over the next twenty four hour it wiped out 99.9% of mankind. 
# Some people that held a special gene were immune. These people were scattedd about the world. 
# Research was to be taken by a group of machines loyal to the humans which wanted to restore mankind. Working together with the few remaining humans they developed a device which allowed dispursion in time. 
# The toxic grew complex and inserted itself into the dispursion of time and then spread the mutated toxic to people in the future, where they had found a cure. This caused the cycle to happen again - 99.9% of the world population was dead in under 24 hours. 
# The remaining human had to find a way to give the cure to a large amount of humans without the machines noticing. They relized that having the machines help them in the cure was useless. They machines would spread their knowlege of the cure to enemy machines which would then develop a mutated toxic that the cure was useless against. The humans worked on traveling back with the cure and stopping the toxic waas being created in the first place. 
# This is their story.
# 
# 
# 
# The ground that Janet walked on was rough. Stones cut into her barefeet. The sun blinded her view, she held her arm above her eyes. Attempting to block out the rays. 
# A figure amurged in the distance.. Squinting she made haste towards the figure. As she drew closer she noticed the figure was a copy of herself. A clone. 
# 'You must be Janet', Janet exampled.
# 'Yes, how do you know?', replied the machine.
# 'Because you are a clone of myself, and my name is Janet'.
# The machine stood still.
# 'Do you know why I am here', Janet asked the machine.
# 'Because you are afraid of the evils that you brought into this world', the machine spoke slowly.
# 'You are here to find a cure', the machine went on.
# 'But I will warn you young one, there is no cure here, only toxics', the machine collabsed to the ground covered in a green slime texture. 
# 
# The number generater returned Noel Locksmart, Elizebeth Goodwill, Trist Gardens, and Ali Turbon. They were inserted into the text in order. Identitys were created. Credit Cards were the main source. Creating a fake identity and building up depit, and not paying it back. 
# Janet scanned the card. Elizebeth Goodwill it the name on the license read. Born 06/11/2014. Spike Infosec: Help Desk 4. The photo was of a straight hair brunete in her early 20s, with frekles covering her face, petite.
# The room reveled a server room with walkways. 
# Goodwill plugged the patch cable from the router. Connected on the otherside was a Raspberry Pi. A green and yellow light turned on by the ethernet port. It had a network. For development and testing Elizebeth perfered to use her own network connection. 
# Truck skretched to a halt on the street. Three toots. Both truck doors opened and two men leaped out. They begain walking towards the propatery at the end of the street. 
# Goodwill could hear several people moving about outside. She triggered her rewind time script. Time slipped back thirty mins. This gave her enough time to exit her home and make it to saftely before the assassians arrived again. 
# The drone showed three people exiting the truck. Two men and a woman. As they scretched to a halt outside the house of Elizebeth Goodwill, was in fact Janet lived there. It was a setup. The house was trapped so that when they entered - they were never going to leave again. 
# Thirty years Noel Locksmart had been a prisnor in the house. He will never forget the night. It was just a standard robbery. Locksmart had recieved word of a computer scientice by the name of Elizebeth Goodwill that had developed software that allowed the replaying of events in the past. The system was complex but started with just one script when Goodwill was just six years old. It was a login and logout script. The first script was the login script. This created a JSON object that included firstname, lastname, date (04/Nov/2014), time (hr:min), reason, and comment. The logout script added to the JSON object logout date, time, and comment. She wrote the script in the programming language Python. Her father  -  Charlie MacDonald had taught her from an early age the basics of programming. She enjoyed it so carried on. At a four year old she was involved in setting up a programming club for children. This idea spread to other towns, cities, and countries. Goodwill would travel with her Father and give demos and talks on their software development. Goodwill went on to co-founder the software development, infomation security, robotics design company: Spike InfoSec.
# 
# 
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
# The dark shape placed the newspaper beside them and stood up. They took the bags of curries and slowly walked towards the door with a large green exit sign at the end of the far wall. 
# Turbons stood frozen untill he heard the exit door close behind the figure. He let out a sigh of relief.
# 'That went better than expected', Alfred spoke. 
# 'Certainly sir, that was much calmer than last time', the voice of Gardens replied. 
# Turbons had to be careful of these anonous bots that were being created. Last time he did an order of curries the bot attacked him and this lab. He had yet to figure out who sent the attack bot but had captured it for tests. He had increased secutiry in order to protect himself and business. 
# Anon Bots that enter the building are now scanned with anti-malware software to test if it had code to attack. Turbons created a white list of bots that he allows to enter. Some of these do have attack code on their system but Turbons trusted the owner that they would not attack. 
# 'Why would people want to attack a kitchen?', was the thought going through his brain. 
# The Police arrived quickly after recieving the emergency signal. Detective Henry Pharrs was in charge of the case. Pharrs was in his late 50s, he had been in the force for 25 year. For 8 years before joining the force he worked as a computer analizt for Spike InfoSec. Today he was investagating a robots that opened fire in a room of humans. Robots created by humans were unable to kill other humans but the robots built robots that had the kill command in the system. 
# Pharrs had studied the kill comand in robots his whole life. His father - Johns Pharrs had studied the kill command much of his life. His Son continued to reasearch the kill command. The goal was to find a cure.
# 
# The door slammed behind the dark shaped as it entered the building. Three security guards stood in front. He moved forward ignoring the guards. They said nothing and didn't move. 
# The alarm went off as the dark shape passed through the dectoror. A guard hit a switch and the alarm stopped. 
# The dark shape moved down the hallway reaching the second door on the left. It turned left. As it passed, the artwork on the walls turned from a bright primary colour scheme to a grayscale, black and white scheme. The Dark Shape left a bitter taste in the air. 
# It reached the foylor. Desks weree empty. It began to wislle as it walked around the desks. The Dark Spaes head darted back and forward between desks, looking for something.
# It's head stopped moving - staring at an item on a desk it moved closer. An item sparkled from the desk.
# The black shape reached out and picked up the item and placed it inside their pocket. 
# It turned around and walked out of the building. 
# Shortly after The Dark Shape left the building, it explodes. 
# 
# Fire engine roars down the road towards the building on fire. The Dark Shape walks down the country side as the engine passes him. Corn fields populate the farm land here. Flying drones fly above the corn - monitoring. The Dark Shape smiles as thir bare feet crunch on the grass. It feels better than the cloth feeing the building had. The Dark Shape turned and watch dark clouds of smoke emurging into the sky. 
# 
# The engine arrived at the building. Much of the building was englufed in flame but the fighters would do their best to save it. Humanolid Robot jumped out of the fire engine and entered the building to check for human that may be still in the building.
# Two of the bots forced the front door open and entered the building. 
# Three security guards stood there englufed in flames. They just beeped gibbish as the firefighters soaked them in anti flame powdered. The flames died down. 
# The fighters contained down the hallway, spraying the ani flame powder as they moved.
# One fighter opened the first door on the left. He entered a large foylor area. Desktop with computers on were englufed in flames. The fighter began to spray the powder at the computer. 
# He noticed a humon figure in the room. It was sitting in the far corner sitting at the desk typing on a keyboard.
# 'Must be a bot, can't be human', the fighter thought to himself. He moved closed to the humanold typing. 
# The fact it didn't stopped typing is strange. Usually an emergeny mode activates when the bots are in danger. The activates a call to authorities and begins a self-repair task.
# The fighter sprayed the bot with anti flame powder. It continued to  type.  
# 
# Charlie MacDonald. Rest in Peace. The grave stone read. Born 24 October 2014. Died 12 December 2093. Trist Gardens stood over the grave. Tears flowing from her eyes. It had been two months since MacDonald passed away. She had worked with him for fifteen years at Spike InfoSec. Together they worked on a automatic cooking device. It was used in billions of home and businesses around the world. Spike InfoSec realeased blueprints of the device so anyone with a 3d printer can just print the device. 
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
# 'wonderful work sir', Jones smiled. 
# 'Kill Jones', MacDonald spoke, his eyes fixed on Jones. 
# The knife snapped out of the claw and started  traveling towards Jones. 
# Jones terrified started moving backwards towards the door. He turned and began running towards the door. 
# The knife traveled faster through the air.Janet Pears
# A cracking sound shoock the room as the knife impayed the brain of Jones. His head was attached to the door. Part of the knife was impayed into the door. It was a instant death. MacDonald didn't have a choice. He was on orders from Trist Gardens. If he didn't follow through and kill his assistant his whole families lives were in danger. 
# 'Clean this up', MacDonald spoke as he walked out of his office. 
# He stood in the foylor. Light blue covered the area. MacDonald could see Janet in distance. She was interviewing a new comer. Alfred Bunnings his name was. MacDonald watched as Janet and Alfred shook hands and took a seat.
# 'He looks like a good test subject', MacDonad spoke. 
# 'Test subject: Alfred Bunnings', the device beeped back. 
# 'Confirm', MacDonald confirmed.
# MacDonald continued to watch Janet and Alfred as they talked. 
# 'So tell me about yourself', Janet had the first question.
# MacDonald had known Janet since she was a toddler. He would push her on the swings in the local park. MacDonalds daughter Elizebeth Goodwill would also be swinging. 
# The Black Cat sat and watched the swings, following the figures in the seats as they moved backwards and forward. 
# 'Black',  a voice behind called and The Black Cat twisted around.
# The Black Cat  moved towards the voice. A dark black shape stood in the distance pouring fresh meat into the cats contaiiner.
# 'Thanks ma'am', The Black Cat spoke, he began eating the meat. 
# The Black Cat was a prototype for the humonald bot. It was used for testing. Under the fake fur and skin was metal and wires. A raspberry Pi computer inside the model with a cell phone and audino connected to that. 
# Human like personioltys were added to the computer. 
# The speech 
# The park ranger - Alfred Bunnings had created this one. He had printed the parts and soultered the robot together. Installing the software was easy - it was all in the software store. Bunnings also worked on scripts for Black. Today he was testing a script that made the robot smell and taste food. As people were pushing their children on the swing he ordered for a humonald robot to activate in the park and send off a signal to attract Black back.
# This script could be used in many areas but Bunnings was developing it so he could find lost or stolen robots. 
# Many times people come into the Park and walk away with a robot. Sometimes I don't relize it. They thing they have made a new friend but really it's a computer belonging to the park. The Park gets an alert that a bot has entered an unauthorised area and sends back gps data. 
# The Park gives the person a friendly phone call or email and offers to either pick the robot up or let the person return the robot themselves. As long as the robot is returned the Park is not worried. Once the robot is returned it's rebooted in order to clear memories of leaving the park. The Park does not want robots remembering what is outside The Park as it causes more robots wanting to leave the park. Rebooting them isn't a problem but there is better work that the staff could be working on - such as new features. 
# Black purred as he ate the fresh meat from his bowl.
# The little girl on the swing with straight brunette hair hoped off the swing and ran toward Black. He purred louder as the girl - Elizebeth Goodwill patted Black. The adult continued to push the other child - a girl with blonde hair and a darker completion than Goodwill.
# The Farm had rows of vegetables growing. On the pathway around the veges walked humonald robots working on the garden. 
# Bunnings walked past the onion gardens. He smiled at the group of humanold robots in suits discussing the Onion garden. 
# 'We need to speed haviousting up by 150% in the next three weeks', Bunnings overheard them as he walked past. 
# The Onion Gardens were thriving. A cold and wet June month meant rain every day. The claw pulled the onion and dropped it into the crate with the rest of the onions that had been havested. 
# The Claw moved fast, pulling another onion out of the ground in less than two seconds. 
# Bunnings whisiled a tune as he walked past the Onion Gardens. Harvesting was excellent with the onions this year. They were experiencing a demand in onions and had increased the amount of The Claw that worked on the gardens. 
# Bunnings entereded the carrot gardens. These parsely like vegetables added sweetness to the companies curries. Bunnings watched a The Claw plucked the carrots from the ground and dropped them in large containers. The next step for the carrots was washing, then it entered the kitchen.
# Bunnings entereed the tomatoe gardens. Rich red tomatoes grew on the stalk. In this garden the company used humonald robots as a majority over the claw. The humonalds were given custom arms that allows for careful picking of the tomatoes. The tomatoes were dropped into containers where they were washed and moved into the kitchen. 
# The herb gardens were next. Here coroondir and other herbs were grown for the Indian Spice Mix.
# 
# The Resturent was where customers could come and eat, or take away curry. Open 24hour/7days. They also offered a delivery service. 
# Humanold robots greeted the customers and showed them to their seat. 
# If they were takeaway they offered a room to sit and read magazines/books. A room that is filled with computers - these are running 24 hours and offer swipe card assess. Security cameras and drones operate in the building to keep an eye on everything. Secuirity drones analze the cameras for any unusual activity. Tonight they had found a human bot spiking the food with toxin. Camera 532 had spoted the crime. A Claw drone spoted the activity on the monitor. Alarms had already activated. Secutiry drones and bots headed towards the area. The human bot that was spiking the food activated a self return to base mode. It caused the bot to turn invisible and extremely tiny - the size of a mouse. The bot was still able to travel at fast speeds but it was also small like a mouse, and invisible. Devices had been developed that allowed for tracking of invisible units. The Claw Drones had invisible cloaking devices build in. This allowed them to become invisible for up to 48 hours. They can enter a sleep mode that allows them to run for months without needed to land. They are able to charge themselves remotly by downloading charge off a connection. This allowed more advance space travel by allowing humans to send robots which could self repair and charge. This allowed robots leaving earth to a far away planet that took thousands of years to reach. The robots finally reached the planet and sent back message to earth on the news. It took the robots 8,500 years to reach the planet. The news took 2,500 years to arrive. The message reached Earth on December 18th 3543. The humans that sent the bots into space and to the  planet had long since extint. Some of the older robots on Earth rememberd the mission and were able to decode the news file. It gave the robots great exciment that these robots had reached the planet and news had arrived back. The Robots of Earth created a time warp portal and linked to the robots on the planet. They ere able to travel between planets instantly. For the robots it felt like they had just woken up from a sleep. They work with the robots in order to get a toxic sent back in time to wipe out a certain group of humans that later develop a toxin that wipes out the human race. The toxin that is sent back is a success but spreads to forign targets - only activating again in 6 generations. 
# When the toxin activates the nervious system in the throat stop working, causing the person to choke to death. A similar kill program was writen for the robots. It caused the robots harddrive to corrupt spreading the corruption to other systems.
# "I'm feeling better now", The Claw said to the humanold robot. The Claw was loading onions from the garden to the containers. These onions had been enjected with a toxin that would later cause much of the human race to die. The toxins had been placed in the onions by robots in the future with the help from a few remainings humans. Their plan was to wipeout a certain amount of humans, presuving human life in the future. Robots more in the future realized that this was a mistake and sent robots back in order to revirse the toxin.
# The only way for the toxin to not be created was to make sure the Spike InfoSec never waas founded. Humans were sent back in order to stop the foundation. Janet Goodwill was the number one target. The humans killed Goodwill many times but each time it was a clone. If the human form of Janet Goodwill is killed then the humans can insert the toxin into her system - sending it back generations. This simple exercise causes the company Spike InfoSec to never be founded. 
# Alfred stood outside an empty building. He looked up. He remembers there was a Spike InfoSec sign hanging here. Instead it's a old video game store mixed with a coke logo, both fading and pealing off. The glass sliding doors didnt excist. A woodern door stood in front of Alfred. He turned the handle. It opened to a small foylor that looks like it was used for a small supermarket. Old broken trolies were scatted around the room. Cobwebs covered the room. A rat scatted accross the room. Followed by a black cat. Alfred walked down the hallway - it was filled with posters from ancient movies. They were faded and pealing off the room. Behind was a light blue textured wallpaper. the ground was a grey-blue carpet. It despritly needed a clean as dirt and grime covered it. 
#                                 
# How shell this day end? 
# 
# 
#  He had plans to create his own Infomation Security company.                                               

# <markdowncell>

# TODO
# 
# html page of page 100 logins/logouts - append all json as one html
# different ways of viewing the data - current loged in, day view, 
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
# records time when child eats/drinks. Keeps track of childrens hunger levels. Alerts if kids havnt aten after certain time. Tag what kids eat - data over time. 
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

reser = pd.Series(opred)

# <codecell>

pd.DataFrame(reser)

# <codecell>

rezda = []

# <codecell>

for res in reser:
    print res
    rezda.append(res)

# <codecell>

rezda

# <codecell>

len(rezda)

# <codecell>


# <codecell>


