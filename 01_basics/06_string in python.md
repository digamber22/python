# string 
```python
>>> num_list = "0123456789"
>>> num_list[:]                 # full string (copy)
'0123456789'

>>> num_list[3:]                # from index 3 to end
'3456789'

>>> num_list[:7]                # from start to index 6
'0123456'

>>> num_list[0:7:2]             # step = 2 (skip every 1 char)
'0246'

>>> num_list[0:7:3]             # step = 3 (skip two chars)
'036'
```
chai = "   Masala Chai   "

### Case Conversion
```python
print(chai.lower())  # Output: '   masala chai   '
print(chai.upper())  # Output: '   MASALA CHAI   '

# Removing whitespace (Strip)
print(chai.strip())  # Output: 'Masala Chai' (Removes leading/trailing spaces)

chai = "Lemon Chai"

# Replace 'Lemon' with 'Ginger'
new_chai = chai.replace("Lemon", "Ginger")

print(chai)      # Output: 'Lemon Chai' (Original remains unchanged)
print(new_chai)  # Output: 'Ginger Chai'

chai_varieties = "Lemon, Ginger, Masala, Mint"

# Split by comma and space
chai_list = chai_varieties.split(", ")

print(chai_list) 
# Output: ['Lemon', 'Ginger', 'Masala', 'Mint']

chai = "Masala Chai"

# Find position (Returns index of first occurrence)
print(chai.find("Chai"))  # Output: 7
print(chai.find("Coffee")) # Output: -1 (Means not found)

# Count occurrences
chai_count = "Masala Chai Chai Chai"
print(chai_count.count("Chai")) # Output: 3

chai_type = "Masala"
quantity = 2

# Using .format() placeholder
order = "I ordered {} cups of {} chai"
print(order.format(quantity, chai_type))
# Output: I ordered 2 cups of Masala chai

chai_list = ['Lemon', 'Ginger', 'Masala']

# Join with a specific separator (e.g., ", " or " ")
print(", ".join(chai_list)) # Output: "Lemon, Ginger, Masala"
print(" ".join(chai_list))  # Output: "Lemon Ginger Masala"

chai = "Chai"

# Get Length
print(len(chai)) # Output: 4

# Loop through every letter
for letter in chai:
    print(letter)
# Output:
# C
# h
# a
# i

# Escaping quotes inside a string
quote = "He said, \"Masala Chai is awesome\""
print(quote)
# Output: He said, "Masala Chai is awesome"

# Raw String for paths (prevents \n or \t from being interpreted)
# Without 'r', \n might create a new line
path = r"C:\Users\User\Desktop\new_folder" 
print(path)
C:\Users\User\Desktop\new_folder

 # Membership Check
chai = "Masala Chai"

print("Masala" in chai)  # Output: True
print("Coffee" in chai)  # Output: False
```