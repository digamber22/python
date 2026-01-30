class Car:
    total_car = 0 

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod                     # static method -> decorator 
    def general_description():        # no self 
        return "Cars are means of transport "

    @property                     # property decorator  (use when need not want to change)
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(isinstance(my_tesla, Car))           # True
print(isinstance(my_tesla, ElectricCar))   # True 


# print(my_tesla.fuel_type())  # Electric Charge 
# safari = Car("Tesla" , "Safari")
# safari.model = "City"
#   print(safari.model())   # error 
# print(safari.model)        # Safari
#  safariThree = Car("Tata" , "Nexon")
