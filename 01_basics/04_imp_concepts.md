## Internal Working of python | Copy, reference counts, slice
### important concept on list with ref 
#

```python
>>> myListOne = [1, 2, 3]
>>> myListTwo = myListOne          # both variables point to the SAME list
>>> myListOne = 'chai'             # myListOne now points to a new object (string)
>>> myListTwo
[1, 2, 3]                          # unchanged, still refers to old list

>>> myListOne = [1, 2, 3]          # new list created
>>> myListTwo
[1, 2, 3]
>>> myListOne
[1, 2, 3]

>>> myListOne[0] = 33              # modifying only myListOne
>>> myListOne
[33, 2, 3]
>>> myListTwo
[1, 2, 3]                          # myListTwo is NOT affected
```
#
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1                     # both l1 and l2 refer to the SAME list object
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]

>>> l1[0] = 44                  # change through l1
>>> l1
[44, 2, 3]
>>> l2
[44, 2, 3]                      # reflected in l2 (same reference)
```
#
```python
>>> p1 = [1, 2, 3]
>>> p2 = p1                      # p2 points to the SAME list as p1
>>> p2 = [1, 2, 3]               # p2 now points to a NEW list (reference broken)
>>> p1[0] = 55                   # modifying p1 only
>>> p1
[55, 2, 3]
>>> p2
[1, 2, 3]                        # p2 unaffected (different list)
```
#
```python
>>> h1 = [1, 2, 3]
>>> h2 = h1[:]                   # shallow copy using slicing
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]

>>> h1[0] = 55                   # modify original list
>>> h1
[55, 2, 3]
>>> h2
[1, 2, 3]                        # h2 unchanged (separate list)

>>> import copy
>>> h2 = copy.deepcopy(h1)       # deep copy (completely independent)
```
#
```python
>>> n = [1, 2, 3]
>>> m = n                       # m and n refer to the SAME list
>>> m
[1, 2, 3]
>>> n
[1, 2, 3]

>>> m == n                      # value comparison
True
>>> m is n                      # reference (identity) comparison
True

>>> n = [1, 2, 3]               # n now points to a NEW list
>>> m == n
True                            # values are same
>>> m is n
False                           # references are different

>>> m = [1, 2, 3]               # m also points to a new list
>>> m == n
True
>>> m is n
False
```