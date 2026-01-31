import time

def cache(func):
    cache_value = {}
    print(cache_value)   # {}   (printed once when decorator is applied)

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]

        result = func(*args)
        cache_value[args] = result
        return result

    return wrapper


@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b


print(long_running_function(2, 3))   # output:
# (wait 4 seconds)
# 5

print(long_running_function(2, 3))   # output:
# (instant, from cache)
# 5

print(long_running_function(4, 3))   # output:
# (wait 4 seconds)
# 7


'''
Flow :- 

Program starts
        ↓
@cache executes immediately
        ↓
cache(long_running_function) is called
        ↓
cache_value = {}
        ↓
print(cache_value) → {}
        ↓
wrapper is returned
        ↓
long_running_function = wrapper
'''

'''
long_running_function → wrapper (NOT original anymore)
func → original function stored inside wrapper
'''

'''
First Call → long_running_function(2,3):- 
Call long_running_function(2,3)
        ↓
Actually calls wrapper(2,3)
        ↓
args = (2,3)
        ↓
Check if (2,3) in cache_value → NO
        ↓
func(*args)
        ↓
original function runs
        ↓
time.sleep(4)
        ↓
returns 5
        ↓
wrapper receives result = 5
        ↓
cache_value[(2,3)] = 5
        ↓
wrapper returns 5
        ↓
print → 5

cache now :
{(2,3): 5}
'''

''' 
Second Call → long_running_function(2,3) :-
Call long_running_function(2,3)
        ↓
wrapper(2,3)
        ↓
args = (2,3)
        ↓
Check cache → YES
        ↓
return cache_value[(2,3)]
        ↓
returns 5 instantly
        ↓
print → 5
'''

'''
Third Call → long_running_function(4,3) :-
Call long_running_function(4,3)
        ↓
wrapper(4,3)
        ↓
args = (4,3)
        ↓
Check cache → NO
        ↓
func(*args)
        ↓
original function runs
        ↓
time.sleep(4)
        ↓
returns 7
        ↓
wrapper stores cache_value[(4,3)] = 7
        ↓
wrapper returns 7
        ↓
print → 7

cache now 
{(2,3): 5, (4,3): 7}
'''

'''
Final One-Line Summary :
Call → wrapper → check cache → 
      found → return
      not found → call original → store → return
'''

