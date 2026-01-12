# Object Types / Data Types
## dir(name) --> use to help in python

- Number : 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List : [1, [2, 'three'], 4.5], list(range(10))
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

- Set : set('abc'), {'a', 'b', 'c'}

- File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')

- Boolean : True, False
- None : None
- Funtions, modules, classes

- Advance: Decorators, Generators, Iterators, MetaProgramming
#

### Numbers
```python
>>> 12 + 12
24
>>> 2.5 * 5
12.5
>>> 2 ** 100  python handle large numbers easily 
1267650600228229401496703205376
>>> import math
>>> math.pi
3.141592653589793
>>> import random
>>> random.random()
0.8335743089987432
>>> random.choice([1,2,3,4,5])
3
```

### string
```python
>>> username = "chaiaurcode"
>>> len(username)
11
>>> username[0]
'c'
>>> username[0] = 'A'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> username[0]
'c'
>>> username[-1]
'e'
>>> username[-2]
'd'
>>> username[1:3]
'ha'


>>> dir(username)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__',
 '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
 '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust',
 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
# 
### list :  is same as array in c++

```python
>>> mylist = [123, "chai", 3.14]
>>> mylist
[123, 'chai', 3.14]
>>> len(mylist)
3
>>> mylist[0]
123
>>> mylist[-1]
3.14
```

#
### dictonary : is same as map in c++
```python
>>> myD = {'one':'lemon', 'two':'ginger', 'comic':'haagraj'}
>>> myD
{'one': 'lemon', 'two': 'ginger', 'comic': 'haagraj'}
>>> myD['comic']
'haagraj'
>>> myD['comics']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'comics'
```
#
### Tuple 
```python
>>> myTup = (1,2,3)
>>> myTup[0]
1
>>> len(myTup)
3
```
#
## Difference between List and Tuple in Python

| Feature | List | Tuple |
|--------|------|-------|
| Mutability | Mutable (can be changed) | Immutable (cannot be changed) |
| Syntax | `[]` | `()` |
| Modify elements | Allowed | Not allowed |
| Methods | Many methods available | Very few methods |
| Performance | Slower | Faster |
| Memory usage | Uses more memory | Uses less memory |
| Use case | Dynamic / changeable data | Fixed / constant data |
| Hashable | No | Yes (if elements are immutable) |

### Example

```python
# List
mylist = [1, 2, 3]
mylist[0] = 10

# Tuple
mytuple = (1, 2, 3)
mytuple[0] = 10  # Error
```