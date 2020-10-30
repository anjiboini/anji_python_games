Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> 2+5-8
-1
>>> tup = (21,36,14,25)
>>> tup
(21, 36, 14, 25)
>>> tup[1]
36
>>> a = (22,25,14,21,5)
>>> a
(22, 25, 14, 21, 5)
>>> s
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> a
(22, 25, 14, 21, 5)
>>> s = (25,14,98,63,75,98)
>>> s
(25, 14, 98, 63, 75, 98)
>>> 
>>> 
>>> 
>>> num = 5
>>> num
5
>>> id(num)
1751230448
>>> name = 'Anjaiah'
>>> name
'Anjaiah'
>>> id(name)
41705600
>>> 
>>> a = 10
>>> b = a
>>> a
10
>>> b
10
>>> id(a)
1751230528
>>> id(b)
1751230528
>>> 
>>> 
>>> id(10)
1751230528
>>> k = 10
>>> k
10
>>> id(k)
1751230528
>>> a = 9
>>> a
9
>>> id(a)
1751230512
>>> id(b)
1751230528
>>> id(k)
1751230528
>>> k = a
>>> k
9
>>> id(k)
1751230512
>>> b =8
>>> b
8
>>> id(b)
1751230496
>>> PI = 3.14
>>> PI
3.14
>>> type(PI)
<class 'float'>
>>> data types
SyntaxError: invalid syntax
>>> 
>>> num = 2.5
>>> num
2.5
>>> type(num)
<class 'float'>
>>> num = 5
>>> num
5
>>> type(num)
<class 'int'>
>>> num = 6+9j
>>> num
(6+9j)
>>> type(num)
<class 'complex'>
>>> a = 5.6
>>> b = int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> k = float(b)
>>> k
5.0
>>> k = 6
>>> c = comples(b,k)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    c = comples(b,k)
NameError: name 'comples' is not defined
>>> c = comples(b,k)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    c = comples(b,k)
NameError: name 'comples' is not defined
>>> c
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> c
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> c = complex(b,k)
>>> c
(5+6j)
>>> b<k
True
>>> bool = b<k
>>> bool
True
>>> type(bool)
<class 'bool'>
>>> b > k
False
>>> int (True)
1
>>> int (False)
0
>>> lst = [25,36,45,12]
>>> lst
[25, 36, 45, 12]
>>> type(lst)
<class 'list'>
>>> s = (25,36,45,15,12,25)
>>> s
(25, 36, 45, 15, 12, 25)
>>> type(s)
<class 'tuple'>
>>> s = [25,36,45,15,12,25]
>>> s
[25, 36, 45, 15, 12, 25]
>>> type(s)
<class 'list'>
>>> s = {25,26,45,15,12,25}
>>> s
{12, 45, 15, 25, 26}
>>> type(s)
<class 'set'>
>>> t = (25,36,4,57,12)
>>> t
(25, 36, 4, 57, 12)
>>> type(t)
<class 'tuple'>
>>> 
>>> 
>>> 
>>> str = "thanu"
>>> str
'thanu'
>>> st = 'a'
>>> st
'a'
>>> type(st)
<class 'str'>
>>> range(10)
range(0, 10)
>>> list[range(10)]
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    list[range(10)]
TypeError: 'type' object is not subscriptable
>>> list{range(10)}
SyntaxError: invalid syntax
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list
<class 'list'>
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> type(range(10))
<class 'range'>
>>> d = ('navin','samsung','rahul'iphone',kiran','oneplus')
SyntaxError: invalid syntax
>>> d = ('navin','samsung','rahul','iphone','kiran','oneplus')
>>> d
('navin', 'samsung', 'rahul', 'iphone', 'kiran', 'oneplus')
>>> d.keys()
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    d.keys()
AttributeError: 'tuple' object has no attribute 'keys'
>>> d
('navin', 'samsung', 'rahul', 'iphone', 'kiran', 'oneplus')
>>> d = ('navin':'samsung','rahul':'iphone','kiran','oneplus')
SyntaxError: invalid syntax
>>> d = ('navin':'samsung','rahul':'iphone','kiran','oneplus')
SyntaxError: invalid syntax
>>> d = ('navin':'samsung','rahul':'iphone','kiran':'oneplus')
SyntaxError: invalid syntax
>>> d = ('navin': 'samsung', 'rahul': 'iphone', 'kiran': 'oneplus')
SyntaxError: invalid syntax
>>> d = ('navin': 'samsung')
SyntaxError: invalid syntax
>>> d = ('navin'; 'samsung')
SyntaxError: invalid syntax
>>>  d = {'navin' : 'samsung'}
 
SyntaxError: unexpected indent
>>> d = ['navin' : 'samsung']
SyntaxError: invalid syntax
>>> 
>>> 
>>> d = {'thanu','samsung','yeshu','iphone','anji','oneplus'}
>>> d = {'thanu':'samsung','yeshu':'iphone','anji':'oneplus'}
>>> d
{'thanu': 'samsung', 'yeshu': 'iphone', 'anji': 'oneplus'}
>>> d.keys()
dict_keys(['thanu', 'yeshu', 'anji'])
>>> 
>>> d.values()
dict_values(['samsung', 'iphone', 'oneplus'])
>>> d['thanu']
'samsung'
>>> d['anji']
'oneplus'
>>> d['yeshu']
'iphone'
>>> d.get('anji')
'oneplus'
>>> d.get('thanu')
'samsung'
>>> d.get('yeshu')
'iphone'
>>> 
>>> 
>>> 
>>> x =2
>>> y = 3
>>> x+y
5
>>> x-y
-1
>>> x*y
6
>>> x/y
0.6666666666666666
>>> x = x + 2
>>> x
4
>>> x+ = 2
SyntaxError: invalid syntax
>>> x
4
>>> x + = 2
SyntaxError: invalid syntax
>>> x+=2
>>> x
6
>>> x*=3
>>> x
18
>>> x/=3
>>> x
6.0
>>> a,b = 5,6
>>> a
5
>>> b
6
>>> n=7
>>> n
7
>>> -n
-7
>>> n
7
>>> n=-n
>>> n
-7
>>> a<b
True
>>> b<a
False
>>> a>b
False
>>> b>a
True
>>> a==b
False
>>> a=6
>>> a==b
True
>>> a<=b
True
>>> a.=b
SyntaxError: invalid syntax
>>> a>=b
True
\
>>> a<=b
True
>>> a>=b
True
>>> a!=b
False
>>> b=7
>>> a!=b
True
>>> a=5
>>> b=4
>>> a<8
True
>>> a<8 and b<5
True
>>> a<8 and b<2
False
>>> a<8 or b<2
True
>>> x= True
>>> x
True
>>> not x
False
>>> x=not x
>>> x
False
>>> 
>>> 
>>> 
>>> 
>>> 
>>> True
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> bin(25)
'0b11001'
>>> 0b0101
5
>>> 0b11001
25
>>> oct(25)
'0o31'
>>> hex(25)
'0x19'
>>> hex(10)
'0xa'
>>> 0xf
15
>>> 0xa
10
>>> 0x19
25
>>> 0b110011010
410
>>> 
>>> 
>>> 
>>> 
>>> a = 5
>>> b = 4
>>> a
5
>>> b
4
>>> print(a)
5
>>> print(b)
4
>>> a= a+b
>>> a
9
>>> a=5
>>> b=6
>>> a=a+b
>>> a
11
>>> b=a-b
>>> b
5
>>> a= a-b
>>> a
6
>>> a
6
>>> a= a-b
>>> a
1
>>> 
>>> 
>>> 
>>> 
>>> ~12
-13
>>> bin(130

    bin(13)
    
SyntaxError: invalid syntax
>>> bin(13)
'0b1101'
>>> 12 & 13
12
>>>  12 | 13
 
SyntaxError: unexpected indent
>>> 12|13
13
>>> 25&30
24
>>>  12 ^ 13
 
SyntaxError: unexpected indent
>>> 12^13
1
>>> 25^30
7
>>> 10<<2
40
>>> 10>>2
2
>>> 