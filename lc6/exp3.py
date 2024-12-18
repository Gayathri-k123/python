from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# User Input
print("Calculate Area of Rectangle")
length = float(input("Enter Length: "))
breadth = float(input("Enter Breadth: "))
rectangle = Rectangle(length, breadth)
print(f"Rectangle Area: {rectangle.calculate_area()}")

print("\nCalculate Area of Triangle")
base = float(input("Enter Base: "))
height = float(input("Enter Height: "))
triangle = Triangle(base, height)

print(f"Triangle Area: {triangle.calculate_area()}")
