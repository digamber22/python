class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.model)          # Model S
print(my_tesla.full_name())    # Tesla Model S



'''
| Concept          | Python Word           | C++ Word                       |
| ---------------- | --------------------- | ------------------------------ |
| Class            | `class`               | `class`                        |
| Object           | Object                | Object                         |
| Current object   | `self`                | `this`                         |
| Constructor      | `__init__`            | Class name                     |
| Destructor       | ❌ (GC based)         | `~ClassName()`                 |
| Inheritance      | `class B(A)`          | `class B : public A`           |
| Parent access    | `super()`             | `Base::`                       |
| Method           | Function inside class | Member function                |
| Data member      | Instance variable     | Data member                    |
| Access specifier | ❌ (by convention)    | `public / private / protected`|
| Method call      | `obj.method()`        | `obj.method()`                 |
| Override         | Same method name      | `virtual / override`           |
| Polymorphism     | Dynamic by default    | `virtual` keyword              |
| Memory mgmt      | Automatic (GC)        | Manual / RAII                  |

'''
