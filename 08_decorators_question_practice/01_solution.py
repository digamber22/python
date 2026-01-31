import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper


@timer
def example_function(n):
    time.sleep(n)

example_function(2)

'''
🔄 Code Flow (Short & Clear)

@timer decorates example_function
example_function is replaced by wrapper
example_function(2) actually calls wrapper(2)
wrapper records start time
Original function (example_function) runs
Function sleeps for 2 seconds
wrapper records end time
Execution time is printed
Original function’s result is returned

👉 In short:
Call → wrapper → measure time → run function → print time → return result ✅
'''

'''
⏱️ Decorator: timer :-
Decorator: timer is a function that wraps another function to add extra behavior.
Purpose: Measures execution time of the decorated function.
'''