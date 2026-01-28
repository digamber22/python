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
#
# Python Math Modules: Floor vs. Truncate

This section demonstrates the difference between two common mathematical operations in Python: `floor()` and `trunc()`. While they appear similar for positive numbers, they behave very differently for negative numbers.

## 1. `math.floor(x)`
The `floor` function returns the largest integer less than or equal to $x$.

* **Concept:** It always rounds **down** towards negative infinity ($-\infty$).
* **For Positive Numbers:** It behaves like removing the decimal.
* **For Negative Numbers:** It rounds to the next lower integer (further away from zero).

 
## 2. `math.trunc(x)` 
The `trunc` function round towards zero.

Code Examples
```python
import math

# Positive numbers: Rounds down to the nearest integer
print(math.floor(3.5))  # Output: 3
print(math.floor(3.6))  # Output: 3
print(math.floor(3.9))  # Output: 3

# Negative numbers: Rounds down towards negative infinity
print(math.floor(-3.5)) # Output: -4 (because -4 is smaller than -3.5)


# Positive numbers: Removes decimal (Same as floor)
print(math.trunc(2.8))  # Output: 2

# Negative numbers: Removes decimal (Rounds towards zero)
print(math.trunc(-2.8)) # Output: -2
```
```python
>>> (2+3j)*2     # iota number 
(4+6j) 
>>> 0o20    # octal 
16
>>> 0xFF    # hex 
255
>>> 0b1000  # binary
8
>>> oct(64)
'0o100'
>>> hex(64)
'0x40'
>>> bin(64)
'0b1000000'
>>> int('64', 8)
52
>>> int('64' , 16)
100
>>> int('10000' , 2)
16
>>> import random
>>> random.random()
0.6459661548481512
>>> random.random(1,10) # generating random number b/w 1 to 10
8
>>>l1 = ['lemon', 'masala', 'ginger']
>>>random.choice(l1)
'masala'
>>>random.suffle(l1)
```
```python
>>> 0.1 + 0.1 + 0.4
0.6000000000000001          # floating-point precision issue

>>> 0.1 + 0.1 + 0.1
0.30000000000000004         # expected 0.3, but not exact

>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17       # very small error instead of 0

>>> (0.1 + 0.1 + 0.1) - 0.3
5.551115123125783e-17       # same precision problem

>>> from decimal import Decimal   # use Decimal for exact arithmetic
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')

>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')              # exact result, no precision error

>>> from fractions import Fraction   # exact rational numbers
>>> myFra = Fraction(2, 7)
>>> myFra
Fraction(2, 7)
```
## set
```python
>>> setone = {1, 2, 3, 4}
>>> setone & {1, 3}
{1, 3}                        # intersection

>>> setone | {1, 3}
{1, 2, 3, 4}                  # union (no change)

>>> setone | {1, 3, 7}
{1, 2, 3, 4, 7}               # union adds new element

>>> setone
{1, 2, 3, 4}

>>> setone - {1, 2, 3, 4}
set()                         # difference (empty set)

>>> type({})
<class 'dict'>                # {} creates a dictionary, not a set
```
```python
>>> type(True)
<class 'bool'>

>>> True == 1
True                          # True is equal to 1 in value

>>> False == 0
True                          # False is equal to 0 in value

>>> True is 1
<stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False                         # 'is' checks identity, not value

>>> True
True

>>> True + 4
5                             # True behaves like integer 1
>>>
