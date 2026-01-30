username = "chaiaurcode"

def func():
    # username = "chai"
    print(username)

print(username)
func()


x = 99 
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x
#     x = 12
    
# func3()
# print(x)



def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()             # myResult = f2 


 # another concept (till below)
def chaicoder(num):
    # Higher-order function: returns another function

    def actual(x):
        # Closure: remembers 'num' from outer scope
        return x ** num

    # 'num' is a free variable captured by the closure
    return actual


# Each call creates a separate closure with its own 'num'
f = chaicoder(2)   # square function
g = chaicoder(3)   # cube function

# Functions behave like objects and can store state via closures
print(f(3))  # 9
print(g(3))  # 27


# What Happens Internally (Flow) :- 
# chaicoder(2) is called
# actual() is created and captures num = 2
# f now points to that function
# f(3) → 3 ** 2 = 9
# Same flow for chaicoder(3) → 3 ** 3 = 27

# Closure allows a function to remember variables from its enclosing scope even after that scope has finished execution.