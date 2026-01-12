# Numbers in depth in python

```python
>>> x = 2
>>> y = 3
>>> z = 4
>>> x + y
5

>>> 40 + 2.23
42.23

>>> 'hitesh' + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

>>> int(2.23)
2
>>> float(40)
40.0

>>> 'chai' + 'code'
'chaicode'
```
#
```python
>>> x, y, z
(2, 3, 4)

>>> x + 1, y * 2
(3, 6)

>>> y % 2
1

>>> z ** 2
16

>>> z ** 5
1024

>>> 100 ** 2
10000

>>> 2 ** 100
1267650600228229401496703205376

>>> 2 ** 1000
1071508607186267320948425049060001810561404811705533607443750388370
3510511249361224931983788156958581275946729175531468251871452856923
1404359845775746985748039345677748242309854210746050623711418779541
8215304647498358194126739876755916554394607706291457119647768654216
7660429831652624386837205668069376
```
```python
>>> result = 1/3.0
>>> result
0.3333333333333333

>>> repr('chai')
"'chai'"

>>> str('chai')
'chai'

>>> print('chai')
chai
```
### repr()

- Used for **developers**
- Shows the **exact representation** of an object
- Output can often be used to **recreate the object**
- **Example:**
  ```python
  >>> repr('chai')
  "'chai'" 
  
### str()

- Used for **users**
- Gives a **clean, readable** form
- No extra formatting
- **Example:**
  ```python
  >>> str('chai')
  'chai'

## print()

- Displays output to the **console**
- Uses `str()` internally
- Returns **nothing (`None`)**
- **Example:**
  ```python
  >>> print('chai')
  chai
