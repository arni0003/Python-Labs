import math

radius_string = input("What is the radius of your circle? ")

radius_float = float(radius_string)

area = math.pi * (radius_string ** 2)

print(area)

input("Press Enter to exit.")
