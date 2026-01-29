def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")


# **kwargs allows a function to accept any number of keyword arguments
# The arguments are received as a dictionary
# kwargs is just a name — ** is what matters and name can be anything

# Each argument is passed as key=value pair
# Keys are strings (parameter names)
# Values can be of any data type

# kwargs.items() returns key-value pairs
# Can be iterated using for loop
# Order of arguments is preserved (Python 3.7+)

# Useful when argument names are not fixed
# Commonly used in configuration, logging, APIs

# **kwargs must come after normal parameters
# def fun(a, b, **kwargs):

# Can be used together with *args
# def fun(*args, **kwargs):
