Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # FILE HANDLING
>>> 
>>> fp = open("test.txt")
>>> type(fp)
<type 'file'>
>>> fp.read()
'Hello World!'
>>> import as
SyntaxError: invalid syntax
>>> import os
>>> os.getcwd()
'C:\\Python27'
>>> fp.close()
>>> fp = open("demo.txt")
>>> fp.read()
'Manipal\nUniversity\nJaipur'
>>> fp.read()
''
>>> fp.seek(0,0)
>>> fp.read()
'Manipal\nUniversity\nJaipur'
>>> fp.seek(1,3)
>>> fp.read()
'anipal\nUniversity\nJaipur'
>>> fp.seek()

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    fp.seek()
TypeError: seek() takes at least 1 argument (0 given)
>>> fp.seek(0,0)
>>> fp.readline()
'Manipal\n'
>>> fp.readline()
'University\n'
>>> fp.readline()
'Jaipur'
>>> fp.seek(0,0)
>>> fp.readlines()
['Manipal\n', 'University\n', 'Jaipur']
>>> fp.seek(0,0)
>>> for line in fp:
	print line

	
Manipal

University

Jaipur
>>> fp.close()
>>> fp = open("ml.txt", "w")
>>> 
fp = open("ml.txt", "w")
>>> fp.w

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    fp.w
AttributeError: 'file' object has no attribute 'w'
>>> fp.write('Forsk Machine Learning Lab in MUJ')
>>> fp.close()
>>> import zlib
>>> s = "Forsk Labs are being setup in CEG, center for electronics governance, Rajasthan.....Forsk in Manipal.... Forks in MNIT.......Forsk in JECRC"
>>> len(s)
139
>>> t = zlib.compress(s)
>>> t
'x\x9cU\xccQ\x0e\x820\x10\x04\xd0\xab\xcc\x01H/\xd1\x80\xd1\xa8\x1f\xc4\x0b,\xcd\x80\x15\xb2%\xbb\xd5\xf3\x0b\xfc1\x9f/3\xd3\x15\xf3\x19w\x19\x1cb\xc4\xc0\xac\x13\x9c\xf5\xbb"+b{i\x90\xa8\x95\x86\xb1\x18\xb80U+\x9a\x93c*?\x9a\x8a&6\xe8\xe5#^\xdf\xa2aOw|n\xf3\x87h^e\xd9\r\x1b\xce~\xe0\xf3\xfa\n\xe1\\\xbc\xb5\xb1\x8f\x7f&\xb7.0'
>>> print t
xﾜUÌQﾂ0ЫÌH/рѨÄ,̀ﾲ%ﾻÕóü1ﾟ/3ÓówbÄ,ﾜõﾻ"+b{iﾐﾨﾕﾆﾱﾸ0U+ﾚﾓc*?ﾚﾊ&6èå#^ߢaOw|nóﾇh^eÙÎ~àóú
á\ﾼﾵﾱﾏ&ﾷ.0
>>> len(t)
113
>>> zlib.decompress(t)
'Forsk Labs are being setup in CEG, center for electronics governance, Rajasthan.....Forsk in Manipal.... Forks in MNIT.......Forsk in JECRC'
>>> t
'x\x9cU\xccQ\x0e\x820\x10\x04\xd0\xab\xcc\x01H/\xd1\x80\xd1\xa8\x1f\xc4\x0b,\xcd\x80\x15\xb2%\xbb\xd5\xf3\x0b\xfc1\x9f/3\xd3\x15\xf3\x19w\x19\x1cb\xc4\xc0\xac\x13\x9c\xf5\xbb"+b{i\x90\xa8\x95\x86\xb1\x18\xb80U+\x9a\x93c*?\x9a\x8a&6\xe8\xe5#^\xdf\xa2aOw|n\xf3\x87h^e\xd9\r\x1b\xce~\xe0\xf3\xfa\n\xe1\\\xbc\xb5\xb1\x8f\x7f&\xb7.0'
>>> s
'Forsk Labs are being setup in CEG, center for electronics governance, Rajasthan.....Forsk in Manipal.... Forks in MNIT.......Forsk in JECRC'
>>> t
'x\x9cU\xccQ\x0e\x820\x10\x04\xd0\xab\xcc\x01H/\xd1\x80\xd1\xa8\x1f\xc4\x0b,\xcd\x80\x15\xb2%\xbb\xd5\xf3\x0b\xfc1\x9f/3\xd3\x15\xf3\x19w\x19\x1cb\xc4\xc0\xac\x13\x9c\xf5\xbb"+b{i\x90\xa8\x95\x86\xb1\x18\xb80U+\x9a\x93c*?\x9a\x8a&6\xe8\xe5#^\xdf\xa2aOw|n\xf3\x87h^e\xd9\r\x1b\xce~\xe0\xf3\xfa\n\xe1\\\xbc\xb5\xb1\x8f\x7f&\xb7.0'
>>> s
'Forsk Labs are being setup in CEG, center for electronics governance, Rajasthan.....Forsk in Manipal.... Forks in MNIT.......Forsk in JECRC'
>>> print t
xﾜUÌQﾂ0ЫÌH/рѨÄ,̀ﾲ%ﾻÕóü1ﾟ/3ÓówbÄ,ﾜõﾻ"+b{iﾐﾨﾕﾆﾱﾸ0U+ﾚﾓc*?ﾚﾊ&6èå#^ߢaOw|nóﾇh^eÙÎ~àóú
á\ﾼﾵﾱﾏ&ﾷ.0
>>> # the above is printing ASCII codes of the hexadecimal no.(\x)
>>> 
>>> s = "Forsk lab in Manipal"
>>> t = zlib.c

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    t = zlib.c
AttributeError: 'module' object has no attribute 'c'
>>> t = zlib.compress(s)
>>> len(s)
20
>>> len(t)
28
>>> #the size is increasing because of the additional information caused due conversion of encoding & decoding
>>> 
>>> import urllib2
>>> f = urllib.urlopen ("http://www.labs.forsk.in/")

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    f = urllib.urlopen ("http://www.labs.forsk.in/")
NameError: name 'urllib' is not defined
>>> f = urllib2.urlopen ("http://www.labs.forsk.in/")

>>> f.read(1000)
'<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <title>Forsk - Learn Code Today</title>\r\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">\r\n\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\r\n    <link rel="shortcut icon" href="images/favicon.ico" type="image/x-icon">\r\n    <link href="css/bootstrap.css" rel=\'stylesheet\' type=\'text/css\' />\r\n    <script type="text/javascript" src="js/jquery-1.11.0.min.js"></script>\r\n<script src="js/bootstrap.min.js"></script>\r\n\t<script src="js/navcall.js"></script>\r\n    <link href="css/camera.css" rel="stylesheet" />\r\n    <link href="css/Reset.css" rel="stylesheet" type="text/css" />\r\n    <link href="css/style.css" rel="stylesheet" type="text/css" media="all" />\r\n    <link href="css/owl.carousel.css" rel="stylesheet" />\r\n\r\n    <script src="js/owl.carousel.js"></script>\r\n\r\n\t<script language="javascript">\r\n\tfunction send_message(){\r\n\tvar name = document.getElementById("name").value;\r\n\tvar '
>>> #useful for web-scraping
>>> 
>>> from datetime import date
>>> date.today()
datetime.date(2018, 2, 7)
>>> import math
>>> math.sqrt(16)
4.0
>>> from math import sqrt
>>> sqrt (6)
2.449489742783178
>>> from math import sqrt as ml
>>> ml(6)
2.449489742783178
>>> #IMPORTANT FILES
>>> 
>>> 
>>> import numpy

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    import numpy
ImportError: No module named numpy
>>> import pandas

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    import pandas
ImportError: No module named pandas
>>> import matplotlib

Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    import matplotlib
ImportError: No module named matplotlib
>>> list2 = [1,2,3,4,5]
>>> 4 in list2
True
>>> 4 not in list2
False
>>> a = [1,2]
>>> b = [1,2]
>>> a==b
True
>>> a is b
False
>>> c = a
>>> a is c
True
>>> a == c
True
>>> a = [1,2,3]
>>> [x**2 for x in a]
[1, 4, 9]
>>> # the above task is known as list comprehension
>>> 
>>> [x+1 for x in [x**2 for x in a]]
[2, 5, 10]
>>> # the above task is known as nested list comprehension
>>> 
>>> 
