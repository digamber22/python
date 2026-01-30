class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.model)          # Model S
print(my_tesla.full_name())    # Tesla Model S

print(my_tesla.__brand)      # AttributeError: 'ElectricCar' object has no attribute '__brand'
                             #  error due to name mangling ( __brand becomes _Car__brand ) , __brand is name-mangled, not strictly private

print(my_tesla.get_brand())  # Tesla !

#
print(my_tesla.fuel_type())  # Electric Charge 
 
safari = Car("Tesla" , "Safari")
print(safari.fuel_type())   # Petrol or Diesel


'''
Name Mangling → __brand becomes _Car__brand
Encapsulation → private data accessed via methods
Inheritance → ElectricCar inherits from Car
Method Overriding → child redefines parent method
Polymorphism → same method name, different behavior
'''