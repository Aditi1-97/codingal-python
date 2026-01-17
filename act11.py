from abc import ABC, abstractmethod
import math


class Polygon(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth



class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height



class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius



print("1. Rectangle")
print("2. Square")
print("3. Triangle")
print("4. Circle")

choice = int(input("Enter your choice: "))

if choice == 1:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    obj = Rectangle(l, b)

elif choice == 2:
    s = float(input("Enter side: "))
    obj = Square(s)

elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    obj = Triangle(base, height)

elif choice == 4:
    r = float(input("Enter radius: "))
    obj = Circle(r)

else:
    print("Invalid choice")
    exit()

print("Area =", obj.area())
