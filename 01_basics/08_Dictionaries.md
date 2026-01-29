## Dictionary in Python
#### Dictionaries are unordered collections of items. They store data in key: value pairs. Keys must be unique and immutable (like strings, numbers, tuples), while values can be anything.

```python
## 1.  Creating Dictionaries

# Creating a dictionary using curly braces {}
# Keys: "Masala", "Ginger", "Green" (Strings)
# Values: "Spicy", "Zesty", "Mild" (Strings)

chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print(chai_types)

# Another way to create a dictionary is using the dict() constructor (discussed later)
```
```python
## 2. Accessing Dictonary items

# Accessing value using square brackets []
print(chai_types["Masala"])  # Output: Spicy

# Accessing a non-existent key using [] throws a KeyError
# print(chai_types["Masala2"]) # Error: KeyError

# Accessing value using the .get() method (Safer)
# If the key doesn't exist, it returns None instead of an error.

print(chai_types.get("Ginger"))  # Output: Zesty
print(chai_types.get("Gingerrr")) # Output: None
```

```python
## 3. Modifying Dictionaries 
# Dictionaries are mutable, meaning you can change, add, or remove items after creation.

# Changing the value of an existing item
chai_types["Green"] = "Fresh"
print(chai_types) 

# Output: {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}

# Adding a new item
chai_types["Earl Grey"] = "Citrus"
print(chai_types)

# Output: {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
```
```python
## 4. Looping Through Dictionaries
# You can loop through a dictionary to get keys, values, or both.

# Loop through keys (Default behavior)
for chai in chai_types:
    print(chai)            # giving key as output
# Output: Masala, Ginger, Green, Earl Grey 

# Loop through keys and access values manually
for chai in chai_types:
    print(chai, chai_types[chai])    

# Output: {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'} 

# Loop through both Keys and Values using .items()
# .items() returns a view object that displays a list of a dictionary's key-value tuple pairs.

for key, value in chai_types.items():
    print(key, value)

# Output: {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}

## 5. conditional check

if "Masala" in chai_types:
    print("I have Masala chai")

## 6. dictionary lenth 
print(len(chai_types)) # Output: 4
```
```python
## 7. Removing items 
# pop(key): Removes the item with the specified key and returns its value.need to provide key because of not any sequence is present . 

chai_types.pop("Ginger") # Returns "Zesty"

# popitem(): Removes the last inserted item (LIFO behavior in Python 3.7+)
chai_types.popitem() # Removes "Earl Grey"

# del keyword: Deletes the item with the specified key.
del chai_types["Green"]

print(chai_types) 
# Output: {'Masala': 'Spicy'} (Only Masala remains)

## 8. Copying Dictionaries
# Creating a copy using .copy()
# This creates a shallow copy. Changes to the copy won't affect the original.

chai_types_copy = chai_types.copy()
```
```python
## 9. Nested Dictionaries

tea_shop = {
    "chai": {
        "Masala": "Spicy",
        "Ginger": "Zesty"
    },
    "Tea": {
        "Green": "Mild",
        "Black": "Strong"
    }
}

print(tea_shop)

# Accessing items in a nested dictionary
print(tea_shop["chai"])          # Output: {'Masala': 'Spicy', 'Ginger': 'Zesty'}
print(tea_shop["chai"]["Ginger"]) # Output: Zesty
```
```python
## 10. Dictionary Comprehension

# Creating a dictionary of squares: {x: x**2}

squared_nums = {x: x**2 for x in range(6)}
print(squared_nums)

# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Clearing the dictionary
squared_nums.clear()
print(squared_nums) # Output: {}
```
```python
## 11. Creating Dictionary from Keys

# Using the fromkeys() method to create a dictionary with specified keys and a default value.

keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"

# Create a dictionary where all keys have the same default value
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

# Output: {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}

# Note: If you pass a mutable object (like a list) as the default_value,

# all keys will share the SAME reference to that list. Modifying one will modify all.
```