Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 0
>>> type(a)
<type 'int'>
>>> str1 = "Machine Learning"
>>> len(str1)
16
>>> str1.upper()
'MACHINE LEARNING'
>>> str2

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    str2
NameError: name 'str2' is not defined
>>> str1
'Machine Learning'
>>> str1.find
<built-in method find of str object at 0x05F728E0>
>>> str1.find('l')
-1
>>> str1.find('L')
8
>>> a = input("Enter the number: ")
Enter the number: 12
>>> a
12
>>> print a
12
>>> name = input("Enter the namw: ")
Enter the namw: sharul

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    name = input("Enter the namw: ")
  File "<string>", line 1, in <module>
NameError: name 'sharul' is not defined
>>> name = inpput("Enter the name: ")

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    name = inpput("Enter the name: ")
NameError: name 'inpput' is not defined
>>> name = raw_input("Enter the name: ")
Enter the name: Shardul Negi
>>> name
'Shardul Negi'
>>> print name
Shardul Negi
>>> a = 3.4
>>> int(a)
3
>>> 
============ RESTART: F:/Machine Learning/Python/machine_test.py ============
10
11
12
13
14
15
16
17
18
19
20
>>> 
============ RESTART: F:/Machine Learning/Python/machine_test.py ============
Enter a no.4
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
>>> 
============ RESTART: F:/Machine Learning/Python/machine_test.py ============
Enter a no.35252345
35252345
>>> 
============ RESTART: F:/Machine Learning/Python/machine_test.py ============
Enter a no.3352432
>>> 
============ RESTART: F:/Machine Learning/Python/machine_test.py ============
Enter a no.34567
>>> 43
43
>>> 2232
2232
>>> 
============ RESTART: F:/Machine Learning/Python/machine_test.py ============
Enter a no.344322
>>> 22
22
>>> 
============ RESTART: F:/Machine Learning/Python/machine_test.py ============
Enter a no.2232332
>>> 21121
21121
>>> 
============ RESTART: F:/Machine Learning/Python/machine_test.py ============
Enter a no.4222424

Traceback (most recent call last):
  File "F:/Machine Learning/Python/machine_test.py", line 7, in <module>
    r=m%10
NameError: name 'm' is not defined
>>> 
============ RESTART: F:/Machine Learning/Python/machine_test.py ============
Enter a no.234234234

Traceback (most recent call last):
  File "F:/Machine Learning/Python/machine_test.py", line 9, in <module>
    rev= rev*10+r
NameError: name 'rev' is not defined
>>> 
============ RESTART: F:/Machine Learning/Python/machine_test.py ============
Enter a no.342342342
34234234
3423423
342342
34234
3423
342
34
3
0
>>> 
============ RESTART: F:/Machine Learning/Python/machine_test.py ============
Enter a no.9876543210
987654321
98765432
9876543
987654
98765
9876
987
98
9
0
>>> x = [1,2,3,4,5,6,7]
>>> type(x)
<type 'list'>
>>> x[0]
1
>>> x[0:5]
[1, 2, 3, 4, 5]
>>> x[-1]
7
>>> x[0] = 10
>>> x[0]
10
>>> print x
[10, 2, 3, 4, 5, 6, 7]
>>> x.app

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x.app
AttributeError: 'list' object has no attribute 'app'
>>> x.append(12)
>>> x
[10, 2, 3, 4, 5, 6, 7, 12]
>>> x.insert(0, 13)
>>> x
[13, 10, 2, 3, 4, 5, 6, 7, 12]
>>> len(x)
9
>>> 
>>> x.remove(13)
>>> x.sort()
>>> print x
[2, 3, 4, 5, 6, 7, 10, 12]
>>> print x.reverse()
None
>>> x.reverse()
>>> x
[2, 3, 4, 5, 6, 7, 10, 12]
>>> x
[2, 3, 4, 5, 6, 7, 10, 12]
>>> x.reverse
<built-in method reverse of list object at 0x05EB0238>
>>> x.reverse()
>>> x
[12, 10, 7, 6, 5, 4, 3, 2]
>>> y = ['Saba', 'Mehak', 'Parth', 'Saumya', 'Shashwat', 'Shardul']
>>> y
['Saba', 'Mehak', 'Parth', 'Saumya', 'Shashwat', 'Shardul']
>>> z =[12, 13, 14, 15]
>>> x.append(Z)

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    x.append(Z)
NameError: name 'Z' is not defined
>>> z
[12, 13, 14, 15]
>>> x.append(z)
>>> x
[12, 10, 7, 6, 5, 4, 3, 2, [12, 13, 14, 15]]
>>> x[7]
2
>>> x[8]
[12, 13, 14, 15]
>>> x[7][1]

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    x[7][1]
TypeError: 'int' object has no attribute '__getitem__'
>>> x.extend(z)
>>> x
[12, 10, 7, 6, 5, 4, 3, 2, [12, 13, 14, 15], 12, 13, 14, 15]
>>> list1 = []
>>> list2

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    list2
NameError: name 'list2' is not defined
>>> list1
[]
>>> list1 = list()
>>> for item in x:
	print item

12
10
7
6
5
4
3
2
[12, 13, 14, 15]
12
13
14
15
>>> for value in x:
	print value

12
10
7
6
5
4
3
2
[12, 13, 14, 15]
12
13
14
15
>>> for i in x:
	print value

15
15
15
15
15
15
15
15
15
15
15
15
15
>>> value
15
>>> i
15
>>>  os = ('Android', 'iOS')
 
  File "<pyshell#76>", line 2
    os = ('Android', 'iOS')
    ^
IndentationError: unexpected indent
>>> os[0]

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    os[0]
NameError: name 'os' is not defined
>>> os = ('Android', 'iOS')
>>> OS[0]

Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    OS[0]
NameError: name 'OS' is not defined
>>> divmod(34, 6)
(5, 4)
>>> type()divmod
SyntaxError: invalid syntax
>>> type(divmod)
<type 'builtin_function_or_method'>
>>> type(divmod(34,6))
<type 'tuple'>
>>> x
[12, 10, 7, 6, 5, 4, 3, 2, [12, 13, 14, 15], 12, 13, 14, 15]
>>> y
['Saba', 'Mehak', 'Parth', 'Saumya', 'Shashwat', 'Shardul']
>>> x, y =divmod(34, 6)
>>> x
5
>>> y
4
>>> x=(5)
>>> type(x)
<type 'int'>
>>> x = (5,)
>>> type(x)
<type 'tuple'>
>>> z.pop()
15
>>> z.pop()
14
>>> z.pop()
13
>>> z.pop()
12
>>> z.pop()

Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    z.pop()
IndexError: pop from empty list
>>> z
[]
>>> #key value clear
>>> dic1 = {}
>>> type(dic1)
<type 'dict'>
>>> dic1= {'fname' : 'Arsh', 'lname': "Singh", "Branch": 'CSE'}
>>> dic1
{'lname': 'Singh', 'Branch': 'CSE', 'fname': 'Arsh'}
>>> # ordered dict is used to print the data as we have written
>>> 
>>> dict['City'] = "Delhi"

Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    dict['City'] = "Delhi"
TypeError: 'type' object does not support item assignment
>>> dic1['City'] = "Delhi"
>>> dic1
{'lname': 'Singh', 'City': 'Delhi', 'Branch': 'CSE', 'fname': 'Arsh'}
>>> dic['name']

Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    dic['name']
NameError: name 'dic' is not defined
>>> dic1['name']

Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    dic1['name']
KeyError: 'name'
>>> dic1['fname']
'Arsh'
>>> 

>>> #Tuples cannot be modified
>>> 
>>> some_list = [1,2,3,4,5,6]
>>> 3 in some_list
True
>>> 10 in some_list
False
>>> 10 not in some_list
True
>>> a= [1,2]
>>> b= [1,2]
>>> a is b
False
>>> a == b
True
>>> a
[1, 2]
>>> c = a
>>> a is c
True
>>> c is b
False
>>> c == b
True
>>> x = [1,2,3,4,5,6,7,6,6]
>>> x.remove(6)
>>> x
[1, 2, 3, 4, 5, 7, 6, 6]
>>> x.remove(6)
>>> x
[1, 2, 3, 4, 5, 7, 6]
>>> x.remove(6)
>>> x
[1, 2, 3, 4, 5, 7]
>>> x = [1,2,3,4,5,6,7,6,6]
>>> len(x)
9
>>> 
================ RESTART: F:/Machine Learning/Python/test2.py ================

================ RESTART: F:/Machine Learning/Python/test2.py ================

================ RESTART: F:/Machine Learning/Python/test2.py ================
[1, 2, 3, 4, 5, 7]
>>> 
================ RESTART: F:/Machine Learning/Python/test2.py ================
[1, 2, 3, 4, 5, 7]
>>> for item in x:
	if item == 6:
		x.remove(item)

>>> x
[1, 2, 3, 4, 5, 7]
>>> x = [1,2,3,4,5,6,7,6,6]
>>> x
[1, 2, 3, 4, 5, 6, 7, 6, 6]
>>> for item in x:
	if item == 6:
		x.remove(item)

>>> x
[1, 2, 3, 4, 5, 7, 6]
>>> #in for loop we will get the wrong answer since it will delete 6 and each time its indexing isgetting change due to   which the indexing mechanism is getting disturbed.
>>> 
>>> #Functions
>>> 
>>> def add_numbers(a, b)
SyntaxError: invalid syntax
>>> def add_numbers(a, b):
	return a+b

>>> add_numbers()

Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    add_numbers()
TypeError: add_numbers() takes exactly 2 arguments (0 given)
>>> add_numbers(4,3)

7
>>> add_numbers(141,123)
264
>>> def add(a,b,c):
	print a+b+c

>>> add(2,3,4)
9
>>> print add(2,3,4)
9
None
>>> 
>>> #DEFAULT PARAMETERS
>>> 
>>> def test(a, b = -99):
	if a > b:
		return True
	else:
		return False

	
>>> test(12,42)
False
>>> test(13)
True
>>> #since default value b=-99, so here b is the default parameters. default parameters are always the last parameters
>>> test(b = 30, a = 13)
False
>>> #in this case we are explicitly mentioning the value.......
>>> 
>>> test()

Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    test()
TypeError: test() takes at least 1 argument (0 given)
>>> #error
>>> 
>>> 
>>> #LIBRARY
>>> 
>>> from daetime import date

Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    from daetime import date
ImportError: No module named daetime
>>> print date.today()

Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    print date.today()
NameError: name 'date' is not defined
>>> from datetime import date
>>> print date.today()
2018-01-31
>>> os.getcwd()

Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    os.getcwd()
NameError: name 'os' is not defined
>>> os.getcwd()

Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    os.getcwd()
NameError: name 'os' is not defined
>>> import os
>>> os.getcwd()
'F:\\Machine Learning\\Python'
>>> import pandas

Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    import pandas
ImportError: No module named pandas
>>> import numpy

Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    import numpy
ImportError: No module named numpy
>>> import matplotlib

Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    import matplotlib
ImportError: No module named matplotlib
>>> import sklearn

Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    import sklearn
ImportError: No module named sklearn
>>> 
