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
import xlutils
import xlwt
import xlrd
import dominate
import sys
from dominate.tags import *
#from sqlalchemy import Column, ForeignKey, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
#from sqlalchemy import create_engine

# <codecell>

mname = ('William Mckee')
ename = ('will@artcontrol.me')
signin = ('ESW')

# <codecell>

#Base = declarative_base()
 
#class Person(Base):
#    __tablename__ = 'person'
#    # Here we define columns for the table person
#    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    name = Column(String(250), nullable=False)
 
#class Address(Base):
#    __tablename__ = 'address'
#    # Here we define columns for the table address.
#    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    datesignin = Column(String(250))
#    hrminsignin = Column(String(250))
#    usernamesignin = Column(String(250), nullable=False)
#    reasonsignin = Column(String(250))
#    person_id = Column(Integer, ForeignKey('person.id'))
#    person = relationship(Person)
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
#engine = create_engine('sqlite:///sqlalchemy_example.db')
 
# Create a$ll tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
#Base.metadata.create_all(engine)

# <codecell>

#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
 
#from sqlalchemy_declarative import Address, Base, Person
 
#engine = create_engine('sqlite:///sqlalchemy_example.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
#Base.metadata.bind = engine
 
#DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
#session = DBSession()
 
# Insert a Person in the person table
#new_person = Person(name='new person')
#session.add(new_person)
#session.commit()
 
# Insert an Address in the address table
#new_address = Address(post_code='00000', person=new_person)
#session.add(new_address)
#session.commit()

# <codecell>

#wrkbook = xlrd.open_workbook('/home/wcmckee/whai/index.xls')

# <codecell>

#print wrkbook.sheet_names()

#worksheet = wrkbook.sheet_by_name('visitor sign database')

# <codecell>

#swlis = []

# <codecell>

#num_rows = worksheet.nrows - 1
#curr_row = -1
#while curr_row < num_rows:
#    curr_row += 1
#    row = worksheet.row(curr_row)
#    print row
#    swlis.append(row)

# <codecell>

#valis = []

# <codecell>

#for swl in swlis[1]:
#    print swl.value
#    valis.append(swl.value)

# <codecell>

#valis

# <codecell>

time.strftime("%a, %d %b %Y %H:%M: +0000", time.gmtime())

# <codecell>

wb = xlwt.Workbook()
ws = wb.add_sheet('visitor sign database')

# <codecell>

rangen = []

# <codecell>

for genz in range(8):
    print os.urandom(128).encode('hex')
    rangen.append(os.urandom(128).encode('hex'))

# <codecell>

rangen

# <codecell>

exran = os.urandom(128).encode('hex')

# <codecell>

ixran = os.urandom(128).encode('hex')

# <codecell>

rawdets = ['In Date', 'In Time', 'In Code', 'Name', 'Reason', 'Out Date', 'Out Time']

# <codecell>

numroll = []

# <codecell>

for det in range(6):
    print det
    numroll.append(det)
    #ws.write(0, det, )

# <codecell>

numroll

# <codecell>

for rad in rawdets:
    print rad
    #print len(rad)
    print rad.upper()
    #range(20)

# <codecell>

ws.write(0, 0, 'In Date')
ws.write(0, 1, 'In Time')
ws.write(0, 2, 'In Code')
ws.write(0, 3, 'Name')
ws.write(0, 4, 'Reason')
ws.write(0, 5, 'Out Date')
ws.write(0, 6, 'Out Time')
ws.write(0, 7, 'Out Code')

# <codecell>

#strftime is %d (day), 

ws.write(1, 0, time.strftime("%d" + "-" + "%b" + "-" + "%Y"))

ws.write(1, 1, time.strftime("%H:%M"))

# <codecell>

#getname = raw_input('Name: ')
#getreason = raw_input('Reason: ')

# <codecell>

ws.write(1, 2, exran)

# <codecell>

ws.write(1, 3, mname)

# <codecell>

ws.write(1, 4, signin)

# <codecell>

#wb.save('/home/wcmckee/whai/' + xlvs)
wb.save('/home/wcmckee/whai/index.xls')

# <codecell>


# <codecell>

wsdict = {mname: rangen[0]}

# <codecell>

wsdict

# <codecell>

wsdict.update({time.strftime("%d" + "-" + "%b" + "-" + "%Y"): rangen[1]})

# <codecell>

wsdict.update({ time.strftime("%H:%M"): rangen[2]})

# <codecell>

wsdict.update({signin: rangen[3]})

# <codecell>

wsdict

# <codecell>

wsdict.keys()

# <codecell>

doc = dominate.document(title='visitor sign sheet')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(id='header').add(ol()):
        for i in wsdict.keys():
            li(a(i))

    with div():
        attr(cls='body')
        p('last updated: ' + time.strftime("%H:%M"))

print doc

# <codecell>

savindex = open('/home/wcmckee/visignsys/index.html', 'w')

# <codecell>

savindex.name

# <codecell>

savindex.write(str(doc))
savindex.close()

# <codecell>

ixtwe = ixran[0:12]

# <codecell>

savpos = open('/home/wcmckee/visignsys/posts/' + ixtwe + '.html', 'w')
savpos.write(str(doc))
savpos.close()

# <codecell>


