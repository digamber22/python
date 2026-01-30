class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.model)          # Model S
print(my_tesla.full_name())    # Tesla Model S

print(my_tesla.__brand)      # AttributeError: 'ElectricCar' object has no attribute '__brand'
                             #  error due to name mangling ( __brand becomes _Car__brand ) , __brand is name-mangled, not strictly private

print(my_tesla.get_brand())  # Tesla !


'''
model → public, directly accessible ✔️
full_name() → accesses __brand inside the class, so it works ✔️
__brand → private (name-mangled), not accessible from outside ❌
get_brand() → public getter, correct way to access private data ✔️

'''

# setter and getter both
'''
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    # Getter
    def get_brand(self):
        return self.__brand

    # Setter
    def set_brand(self, brand):
        self.__brand = brand

    def full_name(self):
        return f"{self.__brand} {self.model}"

my_car = Car("Tesla", "Model S")

my_car.set_brand("Tata")
print(my_car.get_brand())     # Tata

'''