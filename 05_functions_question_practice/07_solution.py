def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1, 2, 3))  # output:  (1, 2, 3)     2 4 6      6  
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))


# *args allows a function to accept any number of positional arguments
# The arguments are received as a tuple
# args is just a name — * is what matters and name can be anythings 

# Uses Python’s built-in sum() function
# Adds all elements in the tuple



# *args collects multiple positional arguments
# Data type of args is tuple
# Can be iterated using loops
# Useful when number of arguments is unknown
# Order of arguments is preserved
# Commonly used in utility functions

# *args must come after normal parameters
# def fun(a, b, *args):
