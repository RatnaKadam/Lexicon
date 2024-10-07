#1. Write a program that takes two integers as input, base and exponent, and calculates the power using loops.
#2. Write a program that calculates the sum of all elements in a given tuple.
#3. Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.
#4. Write a program that merges two dictionaries into a single dictionary. If a key is common to both dictionaries, the value from the second dictionary should be used.
#5. Write a program that takes a list of integers as input and uses list comprehension to create a new list containing only the even numbers from the original list.
#6. Write a program that takes a string as input and prints its reverse.


#1st question:-
base, expnt = map(int,input("Enter base and exponent numbers:  ").split(" "))
answer = 1
for i in range(1,expnt+1):
    answer = base*answer
print(answer)
power = print(base**expnt)

#2nd question:-
my_tuple = (4,5,6,7,8,9)
sum = 0
for every_item in my_tuple:
    sum+=every_item
print(sum)

#3rd question
first_tup = (1,2,3,4,5,6,7,8,9)
new_tup = ()
for item in first_tup:
    if item%2 == 0:
        new_tup = new_tup+(item,)
print(new_tup)

#4th question
first_dict = {"a": 1,"b" : 2,"c" : 3 }
second_dict = {"x":10,"y" : 20, "c" : 30,"z" :40 }
first_dict.update(second_dict)
print(second_dict)
print(first_dict)

#5th question
first_list = [int(input(item)) for item in range(0,10)]
print(first_list)

new_list = [item for item in first_list if item%2 == 0]
print(new_list)

#6th question
given_string = input("Enter your string : ")
print(given_string[-1::-1])

def func(a,b,*aaa,name = "John",**kwargs):
    print(f"{a}")
    print(f"{b}")
    print(f"args = {aaa}")
    print(f"name = {name}")
    print(f"kwargs = {kwargs}")

func(1,2)
func(1,2,3,name = "Anna",age = 34)
