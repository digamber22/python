class Car:
    total_car = 0 

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod                     # static method -> decorator 
    def general_description():        # no self 
        return "Cars are means of transport "

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(my_tesla.fuel_type())  # Electric Charge 
 
safari = Car("Tesla" , "Safari")
safariThree = Car("Tata" , "Nexon")
print(safari.fuel_type())   # Petrol or Diesel 

print(Car.total_car)    # 3    i.e (safari, safariThree, my_tesla)

# 
print(safari.general_description())   # (error not sure ,check later) TypeError: general_description() takes 1 positional argument but 0 were given

print(Car.general_description())      # Cars are means of transport


# notes 
'''
Decorator (Python) :-

A decorator is used to modify or extend the behavior of a function or method.
Written using the @ symbol.
Applied before the function definition.
Does not change the original function code.
Commonly used for method type control and code reusability.
'''

'''
Common Built-in Decorators :- 

@staticmethod
→ Defines a method that does not use self or cls.

@classmethod
→ Defines a method that uses cls (class reference).

@property
→ Used to access methods like attributes.

'''