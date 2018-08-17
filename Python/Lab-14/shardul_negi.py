# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:15:39 2018

@author: Shardul Negi
"""

#import the library used to query a website
import urllib2

#specify the url
icc ="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(icc)

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)
all_tables=soup.find_all('table')
right_table=soup.find('table', class_='table')

#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]


for row in right_table.findAll("tr"):
 cells = row.findAll('td')
 states=row.findAll('th') 
 #To store second column data
 if len(cells)==4: 
     
#Only extract table body not heading
     
     A.append(cells[0].find(text=True))
     B.append(states[0].find(text=True))
     C.append(cells[1].find(text=True))
     D.append(cells[2].find(text=True))
     E.append(cells[3].find(text=True))



#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Pos'])
df['Team']=B
df['Matches']=C
df['Points']=D
df['Rating']=E

print df
