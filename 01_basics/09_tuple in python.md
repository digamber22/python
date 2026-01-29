## Tuple in python
```python
## 1. Creating Tuples
# Tuples are created using parentheses (). They are similar to lists but are immutable.

# Creating a tuple with tea varieties
tea_types = ("Black", "Green", "Oolong")
print(tea_types)
# Output: ('Black', 'Green', 'Oolong')

## 2.Accessing Tuple Items
# You can access tuple elements using index numbers (positive or negative).

# Accessing the first item (Index 0)
print(tea_types[0]) 
# Output: 'Black'

# Accessing the last item (Negative Indexing)
print(tea_types[-1]) 
# Output: 'Oolong'

# Slicing (Getting a range of items)
print(tea_types[1:]) 
# Output: ('Green', 'Oolong')

## 3. Immutability (The Key Feature)

# Tuples cannot be changed after creation. Trying to assign a new value to an index raises an error.

# Try to change "Black" to "Lemon"
# tea_types[0] = "Lemon" 

# Error Output:
# TypeError: 'tuple' object does not support item assignment

##  4. Tuple Operations

# Getting the length of the tuple
print(len(tea_types)) 
# Output: 3

# Creating another tuple
more_tea = ("Herbal", "Earl Grey")

# Concatenating two tuples (Creates a NEW tuple)
all_tea = more_tea + tea_types
print(all_tea)
# Output: ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')

##  5. Conditional Checks

if "Green" in all_tea:
    print("I have Green Tea")
# Output: I have Green Tea

##  6. Tuple Methods

# Tuples have fewer methods than lists. The most common are count() and index().

# Creating a tuple with duplicate values
more_tea = ("Herbal", "Earl Grey", "Herbal")

# Counting occurrences of a value
print(more_tea.count("Herbal")) 
# Output: 2

# Checking for a value that doesn't exist
print(more_tea.count("Mint"))
# Output: 0

## 7. Unpacking Tuples

#You can extract values from a tuple directly into variables. The number of variables must match the number of items in the tuple.

tea_types = ("Black", "Green", "Oolong")

# Unpacking into variables
(black, green, oolong) = tea_types

print(black)  # Output: 'Black'
print(green)  # Output: 'Green'
print(oolong) # Output: 'Oolong'

# Note: The variable names (black, green) are arbitrary, 
# but the order matches the tuple's order.

##  8. Checking Type
# Verifying that the object is indeed a tuple.

print(type(tea_types))
# Output: <class 'tuple'>

##  9. Nested Tuples

# Tuples can contain other tuples (or lists, strings, etc.) inside them.

# A tuple containing a string, another tuple, and a string
nested_tuple = ("Chai", ("Masala", "Ginger"), "Tea")

# Accessing the inner tuple
print(nested_tuple[1])
# Output: ('Masala', 'Ginger')

# Accessing an element inside the inner tuple
print(nested_tuple[1][0])
# Output: 'Masala'
```