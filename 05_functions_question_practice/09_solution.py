def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i



for num in even_generator(10):
    print(num)



# A generator function is defined using yield keyword
# It generates values one at a time instead of returning all at once

# yield pauses the function execution
# Function state is saved between calls
# Next value is produced on next iteration

# even_generator(limit) generates even numbers up to the given limit
# range(2, limit + 1, 2) starts from 2 and steps by 2

# Generator returns an iterator object
# Values are produced lazily (on demand)

# Used with for loop or next() function
# for loop automatically handles StopIteration

# Memory efficient compared to lists
# Suitable for large data or infinite sequences

# Generator does not store all values in memory
# Each value is generated only when needed

# Commonly used in streaming, file reading, large computations

# one - line 
# Generator function uses yield to produce values one at a time lazily
