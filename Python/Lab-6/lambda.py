# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 17:31:37 2018

@author: Shardul Negi
"""

#following are the examples of the lamda function

f = lambda x, y : x + y

print f(1, 1)


#filter 

def f(x): return x % 3 == 0 or x % 5 == 0

x = filter (f, range(2, 25))

#Map

def cube(x): return x*x*x

map(cube, range(1, 11)) # will return only one value

#Reduce

def add(x, y): return x+y
reduce(add, range(1,2,3,4,5,6,7,8,9,10)) #1+2=3+3=6+4=10....... 

map(add, [1,2,3,4,5,6,7,8,9,10])



#---------------------------------------------------------------
#Using map and Lambda together

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27
       
       print filter(lambda x: x % 3 == 0,foo)













 








