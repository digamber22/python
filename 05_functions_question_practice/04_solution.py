import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return round(area, 2), round(circumference, 2)   

a, c = circle_stats(3)

print("Area: ", a, "Circumference: ", c)  # Area = 28.27   Circumference = 18.85

# round is using for more precise value after decimal .