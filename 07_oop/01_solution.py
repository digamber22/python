class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)


'''
Class :-
A class represents a general category or concept.
In the example, Car represents the general idea of a car.

Object :-
An object is a real instance created from a class.
my_car and my_new_car are two different objects of the same class.

Constructor :- 
A constructor initializes an object at the time of creation.
Here, it assigns brand and model when a car object is created.

Instance Variables :-
Instance variables store data specific to each object.
Each car object has its own brand and model.

self Keyword :-
self refers to the current object being created or accessed.
It ensures values are stored in the correct object.

Data Encapsulation (Basic Level) :-
Data and related logic are grouped together inside a class.
Brand and model belong to the Car class.

Reusability :-
One class can be reused to create multiple objects.
The same Car class creates both Toyota and Tata cars.
'''