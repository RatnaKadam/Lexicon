#inheritance
#1. Veichle Inheritance
# Create a Python program that models a hierarchy of vehicles using inheritance. Start with a base class
# Vehicle, and then create two or more derived classes (e.g., Car, Bicycle, Motorcycle) that inherit from
# the Vehicle class. Each class should have specific attributes and methods related to the type of vehicle
# it represents.
# 1. Define the Vehicle base class with common attributes such as make, model, and year, and
# methods like start(), stop(), and fuel_up().
# 2. Create derived classes for different types of vehicles, e.g., Car, Bicycle, and Motorcycle. Each
# derived class should inherit from the Vehicle base class and add attributes and methods
# specific to that type of vehicle. For example, the Car class might have attributes like
# num_doors, and the Bicycle class could have attributes like num_gears.
# 3. Implement specific methods for each derived class. For instance, the Car class might have a
# method to honk the horn, and the Bicycle class could have a method to ring the bell.
# 4. Create instances of each vehicle type and demonstrate their specific methods and attributes.
# For example, you can create a car, bicycle, and motorcycle, and call mmethods like start(),
# stop(), and their specific methods like honk_horn() or ring_bell().

#Base class
class Vehicle:  
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"This is a {self.make} {self.model},launched in {self.year}."

    def start(self):
        return f"{self.make} {self.model} is getting started...."

    def stop(self):
        return f"Stop the {self.make} {self.model}\n"

    def fuel_up(self):
        return f"Filling the tank for {self.make} {self.model}"


v1 = Vehicle("Tata","Nano",2010)

#derived class
class Car(Vehicle):
    def __init__(self,make,model,year,num_doors):
        super().__init__(make,model,year)
        self.num_doors = num_doors
    
    def doors(self):
        return f"{self.make} {self.model} has {self.num_doors} doors."
    
    def horn(self):
        return f"{self.make} {self.model} goes Beep Beep Beep..."


#derived class
class Motorcycle(Vehicle):
    def __init__(self,make,model,year,side_car):
        super().__init__(make,model,year)
        self.side_car = side_car
    
    def num_side_cars(self):
        return f"{self.make} {self.model} has {self.side_car} side cars atteched to it."
    
    def horn(self):
        return f"{self.make} {self.model} goes Vroom Vroom Vroom..."

    def fuel_up(self):
        return f"{self.make} {self.model} is an Electric Bike."

#derived class
class Bicycle(Vehicle):
    def __init__(self,make,model,year,num_gears):
        super().__init__(make,model,year)
        self.num_gears = num_gears
    
    def __str__(self):
        return f"{super().__str__()}"
    
    def gears(self):
        return f"{self.make} {self.model} has {self.num_gears} gears"
    
    def fuel_up(self):
        return f"Bicycle doesn't need Fuel..."
    
    def ring_bell(self):
        return f"Bicycle rings Tring Tring Tirng...."
    

car = Car("Mahindra","Thar",2000,4)
bike = Motorcycle("Royal Enfield","Bullet",1995,1)
cycle = Bicycle("Hero", "XYZ", 2024,6)

vehicles = [car, bike, cycle]
for vehicle in vehicles:
    print(vehicle)
    if isinstance(vehicle, Car):
        print(vehicle.doors())
        print(vehicle.horn())
    elif isinstance(vehicle, Motorcycle):
        print(vehicle.num_side_cars())
        print(vehicle.horn())
    elif isinstance(vehicle, Bicycle):
        print(vehicle.gears())
        print(vehicle.ring_bell())
    
    print(vehicle.start())
    print(vehicle.fuel_up())
    print(vehicle.stop())
    print() 
    

