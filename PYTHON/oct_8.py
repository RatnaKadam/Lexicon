#In this lab, we will create a Python program to model a basic student database using OOP concepts.
# Define a Student Class:
# Define a class named Student with the following attributes:
# name: Name of the student (string).
# age: Age of the student (int).
# grade: Grade level of the student (int).
# Add Methods:
# Add the following methods to the Student class:
# get_info( ): Method to display the student's information.
# promote ( ): Method to promote the student to the next grade level.
# Test the Class:
# Create instances of the Student class and test its methods:
# Create a student named "Anna" with age 15 and grade 9. Use the get_info() method to display her information.
# Promote Anna to the next grade level using the promote() method, then use get_info() to display her updated information.
# Your task is to write Python code to implement the above lab. Focus on class definition, constructor, methods, and object instantiation.


class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_info(self):
        return (f"My name is {self.name}.I am {self.age} years old and I am in {self.grade} th grade.\n")

    def promote(self):
        self.grade = self.grade+1
        print("Afetr Promotion--")
        return self.grade

s1 = Student("Anna",15,9)
print("Before promotion:--")
print(s1.get_info())

s1.promote()
print(s1.get_info())