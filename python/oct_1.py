# Oct 1, 2024 - LAB

# 1st question- Python
given_string = "Python"
print(given_string[4])
print(given_string[:4])
print(given_string[1:4])
print(given_string[-1::-1])

#2nd question
l = [3,7,[1,4,"hello"]]
l[2][2] = "goodbye"
print(l)

#3rd question
d1 = {"simple_key":"hello"}
answer1 = d1["simple_key"]

d2 = {"k1":{"k2":"hello"}}
answer2 = d2["k1"]["k2"]
print(answer2)

d3 = {"k1":[{"nest_key":["this_deep",["hello"]]}]}
answer3 = d3["k1"][0]["nest_key"][1]
print(str(answer3))

#4th question
my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3]
new = set(my_list)
print(new)

#5th question
name = "Sammy"
age = 4
print(f"Hello my dog's name is {name} and he is {age} years old.")