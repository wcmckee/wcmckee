
# coding: utf-8

# In[188]:

import random
#import math

import requests 
import bs4

import arrow


# In[173]:

import getpass


# In[189]:

raw = arrow.now()

yraw = raw.strftime("%Y")
mntaw = raw.strftime("%m")
dytaw = raw.strftime("%d")

fulda = yraw + '/' + mntaw + '/' + dytaw

fultim = fulda + ' ' + raw.strftime('%H:%M:%S')

arnow = arrow.now()

curyr = arnow.strftime('%Y')

curmon = arnow.strftime('%m')

curday = arnow.strftime('%d')


# In[174]:

myusr = getpass.getuser()


# In[181]:

nikpos = '/home/{}/writersdenhamilton/posts/'.format(myusr)


# In[144]:

nountlist = ["Dream","Dreamer","Dreams","Waves", 
"Sword","Kiss","Sex","Lover", 
"Slave","Slaves","Pleasure","Servant", 
"Servants","Snake","Soul","Touch", 
"Men","Women","Gift","Scent", 
"Ice","Snow","Night","Silk","Secret","Secrets", 
"Game","Fire","Flame","Flames", 
"Husband","Wife","Man","Woman","Boy","Girl", 
"Truth","Edge","Boyfriend","Girlfriend", 
"Body","Captive","Male","Wave","Predator", 
"Female","Healer","Trainer","Teacher", 
"Hunter","Obsession","Hustler","Consort", 
"Dream", "Dreamer", "Dreams","Rainbow", 
"Dreaming","Flight","Flying","Soaring", 
"Wings","Mist","Sky","Wind", 
"Winter","Misty","River","Door", 
"Gate","Cloud","Fairy","Dragon", 
"End","Blade","Beginning","Tale", 
"Tales","Emperor","Prince","Princess", 
"Willow","Birch","Petals","Destiny", 
"Theft","Thief","Legend","Prophecy", 
"Spark","Sparks","Stream","Streams","Waves", 
"Sword","Darkness","Swords","Silence","Kiss", 
"Butterfly","Shadow","Ring","Rings","Emerald", 
"Storm","Storms","Mists","World","Worlds", 
"Alien","Lord","Lords","Ship","Ships","Star", 
"Stars","Force","Visions","Vision","Magic", 
"Wizards","Wizard","Heart","Heat","Twins", 
"Twilight","Moon","Moons","Planet","Shores", 
"Pirates","Courage","Time","Academy", 
"School","Rose","Roses","Stone","Stones", 
"Sorcerer","Shard","Shards","Slave","Slaves", 
"Servant","Servants","Serpent","Serpents", 
"Snake","Soul","Souls","Savior","Spirit", 
"Spirits","Voyage","Voyages","Voyager","Voyagers", 
"Return","Legacy","Birth","Healer","Healing", 
"Year","Years","Death","Dying","Luck","Elves", 
"Tears","Touch","Son","Sons","Child","Children", 
"Illusion","Sliver","Destruction","Crying","Weeping", 
"Gift","Word","Words","Thought","Thoughts","Scent", 
"Ice","Snow","Night","Silk","Guardian","Angel", 
"Angels","Secret","Secrets","Search","Eye","Eyes", 
"Danger","Game","Fire","Flame","Flames","Bride", 
"Husband","Wife","Time","Flower","Flowers", 
"Light","Lights","Door","Doors","Window","Windows", 
"Bridge","Bridges","Ashes","Memory","Thorn", 
"Thorns","Name","Names","Future","Past", 
"History","Something","Nothing","Someone", 
"Nobody","Person","Man","Woman","Boy","Girl", 
"Way","Mage","Witch","Witches","Lover", 
"Tower","Valley","Abyss","Hunter", 
"Truth","Edge", "Dream","Dreamer","Dreams","Waves", 
"Kiss","Sex","Lover", 
"Slave","Slaves","Pleasure","Servant", 
"Servants","Snake","Soul","Touch", 
"Men","Women","Gift","Scent", 
"Ice","Snow","Night","Silk","Secret","Secrets", 
"Game","Fire","Flame","Flames", 
"Husband","Wife","Man","Woman","Boy","Girl", 
"Truth","Edge","Boyfriend","Girlfriend", 
"Body","Captive","Male","Wave",
"Female","Healer","Trainer","Teacher", 
"Hunter","Obsession","Hustler","Consort", 
"Dream", "Dreamer", "Dreams","Rainbow", 
"Dreaming","Flight","Flying","Soaring", 
"Wings","Mist","Sky","Wind", 
"Winter","Misty","River","Door", 
"Gate","Cloud",
"End","Beginning","Tale", 
"Tales","Prince","Princess", 
"Willow","Birch","Petals", 
"Spark","Sparks","Stream","Streams","Waves", 
"Kiss", 
"Butterfly","Shadow","Ring","Rings","Emerald", 
"Storm","Storms","Mists", 
"School","Rose","Roses","Stone","Stones", 
"Tears","Touch","Son","Sons","Child","Children", 
"Gift","Word","Words","Thought","Thoughts","Scent", 
"Ice","Snow","Night","Silk","Guardian","Angel", 
"Angels","Secret","Secrets","Search","Eye","Eyes", 
"Danger","Game","Fire","Flame","Flames","Bride", 
"Husband","Wife","Time","Flower","Flowers", 
"Light","Lights","Door","Doors","Window","Windows", 
"Bridge","Bridges","Ashes","Memory","Thorn", 
"Thorns","Name","Names","Past", 
"History","Something","Nothing","Someone", 
"Nobody","Person","Man","Woman","Boy","Girl", 
"Way","Mage","Lover", 
"Tower","Valley","Abyss","Hunter", 
"Truth","Edge"]

adjectivelist =  ["Lost","Only","Last","First", 
"Third","Sacred","Bold","Lovely", 
"Final","Missing","Shadowy","Seventh", 
"Dwindling","Missing","Absent", 
"Vacant","Cold","Hot","Burning","Forgotten", 
"Weeping","Dying","Lonely","Silent", 
"Laughing","Whispering","Forgotten","Smooth", 
"Silken","Rough","Frozen","Wild", 
"Trembling","Fallen","Ragged","Broken", 
"Cracked","Splintered","Slithering","Silky", 
"Wet","Magnificent","Luscious","Swollen", 
"Erect","Bare","Naked","Stripped", 
"Captured","Stolen","Sucking","Licking", 
"Growing","Kissing","Green","Red","Blue", 
"Azure","Rising","Falling","Elemental", 
"Bound","Prized","Obsessed","Unwilling", 
"Hard","Eager","Ravaged","Sleeping", 
"Wanton","Professional","Willing","Devoted", 
"Misty","Lost","Only","Last","First", 
"Final","Missing","Shadowy","Seventh", 
"Dark","Darkest","Silver","Silvery","Living", 
"Black","White","Hidden","Entwined","Invisible", 
"Next","Seventh","Red","Green","Blue", 
"Purple","Grey","Bloody","Emerald","Diamond", 
"Frozen","Sharp","Delicious","Dangerous", 
"Deep","Twinkling","Dwindling","Missing","Absent", 
"Vacant","Cold","Hot","Burning","Forgotten", 
"Some","No","All","Every","Each","Which","What", 
"Playful","Silent","Weeping","Dying","Lonely","Silent", 
"Laughing","Whispering","Forgotten","Smooth","Silken", 
"Rough","Frozen","Wild","Trembling","Fallen", 
"Ragged","Broken","Cracked","Splintered",
"Lost","Only","Last","First", 
"Third","Sacred","Bold","Lovely", 
"Final","Missing","Shadowy","Seventh", 
"Dwindling","Missing","Absent", 
"Vacant","Cold","Hot","Burning","Forgotten", 
"Weeping","Dying","Lonely","Silent", 
"Laughing","Whispering","Forgotten","Smooth", 
"Silken","Rough","Frozen","Wild", 
"Trembling","Fallen","Ragged","Broken", 
"Cracked","Splintered","Slithering","Silky", 
"Wet","Magnificent","Luscious","Swollen", 
"Erect","Bare","Naked","Stripped", 
"Captured","Stolen","Sucking","Licking", 
"Growing","Kissing","Green","Red","Blue", 
"Azure","Rising","Falling","Elemental", 
"Bound","Prized","Obsessed","Unwilling", 
"Hard","Eager","Ravaged","Sleeping", 
"Wanton","Professional","Willing","Devoted", 
"Misty","Lost","Only","Last","First", 
"Final","Missing","Shadowy","Seventh", 
"Dark","Darkest","Silver","Silvery","Living", 
"Black","White","Hidden","Entwined","Invisible", 
"Next","Seventh","Red","Green","Blue", 
"Purple","Grey","Bloody","Emerald","Diamond", 
"Frozen","Sharp","Delicious","Dangerous", 
"Deep","Twinkling","Dwindling","Missing","Absent", 
"Vacant","Cold","Hot","Burning","Forgotten", 
"Some","No","All","Every","Each","Which","What", 
"Playful","Silent","Weeping","Dying","Lonely","Silent", 
"Laughing","Whispering","Forgotten","Smooth","Silken", 
"Rough","Frozen","Wild","Trembling","Fallen", 
"Ragged","Broken","Cracked","Splintered" ]
  


# In[145]:

reqadv = requests.get('http://donjon.bin.sh/fantasy/adventure/')


# In[146]:

bsadv = bs4.BeautifulSoup(reqadv.text)


# In[ ]:




# In[147]:

adsee = bsadv.findAll(id="adventure")


# In[148]:

themlist = list()


# In[149]:

shorting = list()


# In[150]:

for ads in adsee:
    #print(ads.findAll('td'))
    #themlist.append(ads.findAll('td'))
    #print(ads.findAll('b'))
    for adb in ads.findAll('b'):
        #for theml in themlist:
            #print(theml)
        print(adb.text)
        shorting.append(adb.text)
    #shor


# In[151]:

shorting


# In[152]:

random.randint(1, 103)


# In[153]:

random.randint(0, 500)


# In[154]:

unisex_name = ['Sam','Bob','Morgan','Jamie', 'Jody','Robin','Alex','Lee','Ash']

physical = ['short','tall','strong','weak',	'muscular','puny','ugly','hot','sexy','fat',
'thin','slim','curvy','slender','handsome','stunning','beautiful','pale','hairy','bald','porky','podgy',
'grubby', 'scruffy', 'smart', 'flabby']

species =['werewolf','vampire','mermaid','wizard', 'angel','demon','alien','ghost','loch ness monster','phantom cat',
'goblin','pixie','unicorn','yeti','gremlin','zombie','dragon','serpent','fairy','elf','god','fallen angel',
'gargoyle', 'siren', 'shape shifter', 'yeti']

accident=['drunk driving','sausage','flying','boating',	'catapulting','hit and run','apocalyptic','magic','golfing',
'polo','motor','unfortunate','bear baiting','crocodile taming','safari','bungee jumping','dancing','pointless','fang',
'skating','biking']

vulnerable = ['old lady',
'chicken',
'baby',
'toddler',
'old man',
'kitten',
'puppy',
'blind person',
'deaf person',
'injured bird',
'disabled person',
'baby bird',
'owl']

role = ['Mummy', 'Daddy', 'Doctor', 'Dentist', 'Sis', 'Bro',
'Teacher', 'Headmaster', 'Honey', 'Darling', 'Dear', 'Mother', 'Mum', 'Father', 'Dad', 'Nan', 'Grandma', 'Grandpa', 
        'Auntie', 'Uncle']

pos_character =['gentle', 'thoughtful', 'modest', 'adorable', 'brave', 'helpful','loving', 'special', 'hopeful', 
                'optimistic', 'charming','kind', 'grateful', 'gracious', 'delightful', 'patient','generous', 
                'energetic', 'down to earth', 'admirable', 'friendly','smart', 'considerate','noble', 'articulate', 
                'caring','intuitive', 'sympathetic','clever', 'daring', 'courageous','hilarious', 'understanding', 
                'incredible','funny', 'popular', 'virtuous', 'lovable', 'remarkable', 'cute', 'sweet', 'splendid',
                'stable', 'witty', 'admirable', 'giving', 'intelligent', 'brave', 'bold']

neg_character = ['greedy','callous','selfish','spiteful','mean','cowardly','stupid', 'spiteful', 'scheming','wild',
                 'tactless','peculiar','creepy','sinister', 'arrogant', 'proud', 'ruthless', 'cold-blooded', 'smelly', 
                 'vile', 'snotty', 'hungry', 'predatory', 'malicious', 'deranged', 'snooty', 'violent', 'cowardly', 
                 'brutal', 'controlling', 'clumsy', 'forgetful', 'thoughtless', 'stingy', 'rude', 'tight-fisted']
          
phys_adj = ['sloppy','slimy','spiky','greasy','ginger','brunette','brown', 'blonde', 'red','tall','short','fat','squat',
          'chubby', 'skinny', 'pointy', 'scrawny', 'wobbly', 'wide', 'vast', 'solid', 'fragile', 'fluffy', 'hairy', 
          'grubby', 'dirty', 'moist', 'ugly', 'pretty', 'charming', 'handsome', 'beautiful', 'sticky', 'curvaceous', 
          'curvy', 'ample', 'ruddy']


# In[155]:

jobsjobs = ["Corporate","Data Broker","Driver","Hacker","Mechanic","Media","Mercenary","Paramedic","Smuggler","Technician"]


# In[156]:

pertype = ["Modern Male","Modern Female","Chinese Male","Chinese Female","Japanese Male","Japanese Female", 
           "Russian Male","Russian Female","Netrunner"]


# In[157]:

worlds = ["Mortal World", "Abyss Astral Sea", "Elemental Chaos", "Feywild", "Nine Hells", "Shadowfell"]


# In[158]:

terrain = ["Aquatic","Desert","Forest","Hill","Marsh","Mountain","Plain","Underground"]


# In[159]:

AnyClass = ["Engineer", "Explorer", "Mercenary", "Paramedic", "Pilot", "Rogue", "Scientist", "Smuggler", "Technician"]


# In[160]:

AnyClass


# In[161]:

plotidea = list()


# In[162]:

for skipid in range(10):
    uniname = random.choice(unisex_name)
    spec = random.choice(species)

    accid = random.choice(vulnerable)

    rol = random.choice(role)

    poschar = random.choice(pos_character)

    negchar = random.choice(neg_character)

    physad = random.choice(phys_adj)

    jobjo = random.choice(jobsjobs)

    pert = random.choice(pertype)
    ranwor = random.choice(worlds)
    
    tera = random.choice(terrain)
    
    clcla = random.choice(AnyClass)
    
    plotidea.append(rol + ' ' + uniname + ', ' + spec + ', ' +clcla + ', ' + accid + ', ' + poschar + ', ' + negchar + ', ' + physad + ', ' + 
       jobjo + ', ' + pert + ', ' + ranwor + ', ' + tera)


# In[163]:

noveldict = dict()


# In[ ]:




# In[164]:

for plotc in plotidea:
    print (plotc)


# In[165]:

shorting


# In[166]:

uniname = random.choice(unisex_name)
spec = random.choice(species)

accid = random.choice(vulnerable)

rol = random.choice(role)

poschar = random.choice(pos_character)

negchar = random.choice(neg_character)

physad = random.choice(phys_adj)

jobjo = random.choice(jobsjobs)

pert = random.choice(pertype)
ranwor = random.choice(worlds)


# In[167]:

print (rol + ' ' + uniname + ', ' + spec + ', ' + accid + ', ' + poschar + ', ' + negchar + ', ' + physad + ', ' + 
       jobjo + ', ' + pert + ', ' + ranwor)


# In[169]:

ranoun = random.choice(nountlist)


# In[170]:

adnoun = random.choice(adjectivelist)


# In[176]:

booktit = ranoun + ' ' + adnoun


# In[178]:

booknos = booktit.replace(' ', '-')


# In[179]:

booknos


# In[190]:

with open(nikpos + booknos + '.rst', 'w') as mok:
    for plotc in plotidea:
        print (plotc)
        mok.write(plotc + '\n\n')
    
    for sho in shorting:
        mok.write(sho + '\n\n')
        
        
with open(nikpos + booknos + '.meta', 'w') as dok:
        dok.write('.. title: {} \n.. slug: {} \n.. date: {} \n.. author: {}'.format(booktit, booknos, fultim, myusr))
        
        


# In[ ]:



