# Create a Python program that explores polymorphism using a hierarchy of shapes. Start with a base
# class Shape, and then create two or more derived classes (e.g., Circle, Rectangle, Triangle) that
# inherit from the Shape class. Each shape class should have its own implementation of methods like
# area() and perimeter(). These methods will calculate the area and perimeter of the respective shape.
# 1. Define the Shape base class with methods like area() and perimeter(). You can initialize any
# common attributes in the base class.
# 2. Create derived classes for different shapes, e.g., Circle, Rectangle, and Triangle. Each derived
# class should inherit from the Shape base class and implement its own version of the area()
# and perimeter() methods.
# 3. Implement specific methods for each derived class. For example, the Circle class might have a
# method to calculate its area based on the radius, and the Rectangle class could have a
# method to calculate its area based on length and width.
# Create instances of each shape type and demo

# Base class
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
    
# Derived Class
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        area_of_circle = 3.14*self.radius*self.radius
        return f"Area of circle with radius {self.radius}cm is {area_of_circle}sq.cm."
    
    def perimeter(self):
        perimeter_of_circle = 2*3.14*self.radius
        return f"Perimeter of circle is {perimeter_of_circle:.2f}cm"

# Derived Class
class Triangle(Shape):
    def __init__(self, base,height):
        self.base = base
        self.height = height
    
    def area(self):
        area_of_triangle = self.base*self.height*0.5
        return f"The area of triagle is {area_of_triangle}sq.cm."

# Derived Class
class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        area_of_square = self.side*self.side
        return f"Area of Square with side {self.side}cm is {area_of_square}sq.cm."

    def perimeter(self):
        perimeter_of_square = 4*self.side
        return f"Perimeter of square with side {self.side}cm is {perimeter_of_square}cm "

# Creating objects
circle = Circle(10)
triangle = Triangle(4,6)
square = Square(5)

shapes = [circle,triangle,square]

for every_shape in shapes:
    if isinstance (every_shape, Triangle):
        print(every_shape.area())
    elif isinstance(every_shape, Circle):
        print(every_shape.area())
        print(every_shape.perimeter())
    elif isinstance(every_shape, Square):
        print(every_shape.area())
        print(every_shape.perimeter())
    print("\n")