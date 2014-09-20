# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# kim dot com
# 
# linux
# 

# <codecell>

import requests

from bs4 import BeautifulSoup


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

for divs in mydivs:
    print divs.findAll('th')
    print divs.findNext('td')
    print divs.findNext('tr')
    

# <codecell>

devsa
    

# <codecell>

soup.find_all('tr')

# <codecell>

soup = BeautifulSoup(eletextg)
print(soup.prettify())

# <codecell>


