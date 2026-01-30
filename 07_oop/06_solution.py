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



'''
total_car :-
Counts total objects created.
Updated inside constructor.
Shared across parent and child classes.
'''