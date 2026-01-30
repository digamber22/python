class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.brand)     # Toyota
print(my_car.model)     # Corolla

print(my_car.full_name())    # Toyota Corolla

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)      # Safari
