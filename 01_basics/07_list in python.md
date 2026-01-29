## List
```python
## 1. Creating a list
tea_varieties = ["Black", "Green", "Oolong", "White"]
print(tea_varieties)

# Accessing individual items
print(tea_varieties[0])   # Output: 'Black'
print(tea_varieties[-1])  # Output: 'White' (Last item)
print(tea_varieties[1])   # Output: 'Green'

## 2. Slicing Lists
# Basic Slicing [start : end] (end is exclusive)
print(tea_varieties[0:2]) # Output: ['Black', 'Green']
print(tea_varieties[:2])  # Output: ['Black', 'Green']
print(tea_varieties[1:])  # Output: ['Green', 'Oolong', 'White']
print(tea_varieties[1:3]) # Output: ['Green', 'Oolong']

## 3. Modifying Lists
# Changing a specific item
tea_varieties[3] = "Herbal"
print(tea_varieties) 
# Output: ['Black', 'Green', 'Oolong', 'Herbal']

# Replacing a slice (One-to-One)
tea_varieties = ["Black", "Green", "Oolong", "White"]
tea_varieties[1:2] = ["Lemon"]
print(tea_varieties)
# Output: ['Black', 'Lemon', 'Oolong', 'White']

# Replacing a slice with multiple items (Injection)
tea_varieties = ["Black", "Green", "Oolong", "White"]
tea_varieties[1:2] = ["Lemon", "Ginger"]
print(tea_varieties)
# Output: ['Black', 'Lemon', 'Ginger', 'Oolong', 'White'] (Green is replaced by two items)

>>> tea_varities
['Black', 'green', 'Masala', 'White']

>>> tea_varities[1:1]                 # empty slice
[]

>>> tea_varities[1:1] = ["test", "test"]   # insert elements at index 1
>>> tea_varities
['Black', 'test', 'test', 'green', 'Masala', 'White']

>>> tea_varities[1:2]                 # slice with one element
['test']

>>> tea_varities[1:3]                 # slice with two elements
['test', 'test']

>>> tea_varities[1:3] = []             # delete slice
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>>


## 4. Loops with Lists
tea_varieties = ["Black", "Green", "Oolong", "White"]

# Basic Loop
for tea in tea_varieties:
    print(tea)

# Black
# Green
# Oolong
# White

# Loop with custom end character (instead of new line)
for tea in tea_varieties:
    print(tea, end="-")
# Output: Black-Green-Oolong-White-

## 5. Conditional check 
if "Oolong" in tea_varieties:
    print("I have Oolong tea")

# If "Oolong" is not in the list, nothing prints.

## 6. Adding and Removing methods
tea_varieties = ["Black", "Green", "Oolong", "White"]

# 1. Append (Adds to the end)
tea_varieties.append("Masala")
print(tea_varieties)
# Output: ['Black', 'Green', 'Oolong', 'White', 'Masala']

# 2. Pop (Removes and returns the last item)
last_tea = tea_varieties.pop()
print(last_tea)      # Output: 'Masala'
print(tea_varieties) # Output: ['Black', 'Green', 'Oolong', 'White']

# 3. Remove (Removes a specific value)
tea_varieties.remove("Green")
print(tea_varieties)
# Output: ['Black', 'Oolong', 'White']

# 4. Insert (Inserts at a specific index)
tea_varieties.insert(1, "Green") # Insert 'Green' at index 1
print(tea_varieties)
# Output: ['Black', 'Green', 'Oolong', 'White']

## 7. Copying Lists (imp)
#Understanding the difference between reference assignment and actual copying.
tea_varieties = ["Black", "Green", "Oolong", "White"]

# Reference Copy (Dangerous if unwanted)
# Both variables point to the SAME memory location.
copy_ref = tea_varieties 
copy_ref.append("Lemon")
# This changes BOTH lists
print(tea_varieties) # Has Lemon
print(copy_ref)      # Has Lemon

# Actual Copy (Safe)
# Creates a NEW list in a different memory location.
tea_varieties_copy = tea_varieties.copy() # ref is different now . 
tea_varieties_copy.append("Ginger")

# Only the copy has Ginger
print(tea_varieties)      # No Ginger
print(tea_varieties_copy) # Has Ginger

## 8. List Comprehensive
# Checking what range returns
print(range(10))
# Output: range(0, 10)

# Generating a list of squared numbers from 0 to 9
squared_nums = [x**2 for x in range(10)]
print(squared_nums)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Generating a list of cubed numbers from 0 to 4
cube_nums = [y**3 for y in range(5)]
print(cube_nums)
# Output: [0, 1, 8, 27, 64]