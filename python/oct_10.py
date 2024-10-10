
# Task :- Develope a Simulation system for zoo
#base class
class LivingBeing:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hi!! My name is {self.name} and I am {self.age} years old"

#derived class
class Creature(LivingBeing):
    def __init__(self,name,age,animal,food):
        super().__init__(name,age)
        self.animal = animal
        self.food = food
        self.energy_level = 5
   
    def __str__(self):
        return f"{super().__str__()} {self.animal}."
   
    def animal_type(self):
        herbivore_foods = {"veggie", "nuts", "fruits"}
        if self.food in herbivore_foods:
            return f"{self.animal} is a herbivorous animal.\n{self.animal} doesn't hunt."
        elif self.food == "meat":
            return f"{self.animal} is a carnivorous animal.\n{self.animal} hunts for survival... {self.animal} loves fresh meat :)"
        else:
            return "It's not a valid food."
    
    def sleep(self):
        return f"{self.animal} is so Sleepy Sleepy..."
    
    def eat(self):
        print(f"I am eating yummy {self.food} and getting energisd...:)")
        self.energy_level += 1
    
    def check_energy(self):
        if self.energy_level < 5:
            print(f"{self.animal}'s current energy level is {self.energy_level} and I am having Low enery today :(")
        else:
            print(f"{self.animal}'s current energy level is {self.energy_level} and I have High Energy today :)")
    
    def play_time(self,game):
        self.energy_level -= 1
        print(f"{self.animal} is {game} ...:)")
    
#derived class
class Visitor(LivingBeing):
    def __init__(self,name,age):
        super().__init__(name,age)

    def __str__(self):
        return f"{super().__str__()}"
    
    def feed_animal(self,food_item,animal):
        animal.energy_level +=1
        self.food_item = food_item
        print(f"{self.name} is feeding {self.food_item} to {animal.animal}...whooo.... :)")

#creating objects
monkey = Creature("Pookie", 5, "monkey", "fruits")
lion = Creature("Lio", 20, "lion", "meat")
man = Visitor("Peter", 30)

#printing Animals' and visiotr's information
print(monkey)
print(monkey.animal_type())
print("\n")
print(lion)
print(lion.animal_type())
print("\n")
print(man)
print("\n")

# Feeding animals
man.feed_animal("banana", monkey)
man.feed_animal("meat", lion)
print("\n")

# Checking energy levels
monkey.check_energy()
lion.check_energy()
print("\n")

# Playtime for animals
monkey.play_time("jumping on trees")
lion.play_time("hunting")
print("\n")

#checking energy level after play
monkey.check_energy()
lion.check_energy()
print("\n")

# Animals are tired and sleepy
print(monkey.sleep())
print(lion.sleep())




