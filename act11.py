from abc import ABC, abstractmethod


# Abstract base class
class Polygon(ABC):

    @abstractmethod
    def area(self):
        pass


# Rectangle class
class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# Square class
class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Triangle class
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Menu-driven program
print("Choose a Polygon to Calculate Area")
print("1. Rectangle")
print("2. Square")
print("3. Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    shape = Rectangle(l, b)

elif choice == 2:
    s = float(input("Enter side: "))
    shape = Square(s)

elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    shape = Triangle(base, height)

else:
    print("Invalid choice!")
    exit()

print("Area =", shape.area())
