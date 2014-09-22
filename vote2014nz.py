# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <h1>vote2014nz</h1>
# 
# Python script to get data on Election 2014 New Zealand Results
# 

# <markdowncell>

# TODO

# <codecell>

import requests
from bs4 import BeautifulSoup
import dominate

# <codecell>

elecreq = ('http://www.electionresults.govt.nz/electionresults_2014/partystatus.html')

# <codecell>

elecreq.upper()

# <codecell>

elecaz = requests.get(elecreq)

# <codecell>

eletextg = elecaz.text

# <codecell>

eletextg

# <codecell>

soup = BeautifulSoup(eletextg)
print(soup.prettify())

# <codecell>

soup.find_all('a')

# <codecell>

mydivs = soup.findAll("tr", { "class" : "hhevy" })

devsa = soup.findAll("td", { "class" : "orhdg"})

# <codecell>

votelis = []

# <codecell>

divlist = []

for divs in mydivs:
    print divs.findAll('th')
    divlist.append(divs.findAll('th'))
    #votelis.append(divs.findALL('th'))
    print divs.findNext('td')
    divlist.append(divs.findNext('td'))
                   
    #votelis.append(divs.findNext('td'))
    #print divs.findNext('tr')
    

# <codecell>

for devz in devsa:
    print(devz)
    votelis.append(devz)

# <codecell>

votelis

# <codecell>

votezcont = []

# <codecell>

for votez in votelis:
    print votez.contents
    votezcont.append(votez.contents)

# <codecell>

for numz in votezcont:
    print(numz)

# <codecell>

votaz = votez.getText()

# <codecell>

numadd = []

# <codecell>

for lets in votaz:
        print lets
        numadd.append(lets)

# <codecell>

for numza in numadd:
    print numza

# <codecell>

for numz in numadd:
    if int in numz:
        print numz

# <codecell>

soup.find_all('tr')

# <codecell>

X

# <codecell>

TODO:
    

# <codecell>


# <codecell>


# <codecell>

for divs in mydivs:
    print divs.findAll[('tr')

# <codecell>

for divs in mydivs:
    print divs.find_next('tr')

# <codecell>

divlist

# <codecell>


# <codecell>


