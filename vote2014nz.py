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

elecreq = ('http://www.electionresults.govt.nz/partystatus.html')

# <codecell>

elecreq.upper()

# <codecell>

elecaz = requests.get(elecreq)

# <codecell>

eletextg = elecaz.text

# <codecell>

soup.find_all('a')

# <codecell>

mydivs = soup.findAll("tr", { "class" : "hhevy" })

devsa = soup.findAll("td", { "class" : "orhdg"})

# <codecell>

votelis = []

# <codecell>

for divs in mydivs:
    print divs.findAll('th')
    #votelis.append(divs.findALL('th'))
    print divs.findNext('td')
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
    print numz

# <codecell>

votez
    

# <codecell>

soup.find_all('tr')

# <codecell>

soup = BeautifulSoup(eletextg)
print(soup.prettify())

# <codecell>


# <codecell>


# <codecell>


# <codecell>


