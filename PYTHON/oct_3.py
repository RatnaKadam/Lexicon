#1st Question
#Given a List of integers return True if sequence is  [1,2,3]
def check():
    arryCheck = list(map(int, input("Enter numbers separated by spaces: ").split()))

    for item in range(len(arryCheck)-2):
        if (arryCheck[item] == 1 and arryCheck[item+1] ==2 and arryCheck[item+2] ==3):
            return True
        else:
            return False
        
answer1 = check()
print(answer1)

#2nd Question
def alter_string():
    given_string = input("Enter your string : ")
    new_string = given_string[::2]
    return new_string
answer2 = alter_string()
print(answer2)

#3rd Question
def double_string():
    given_string = input("Enter string: ")
    new_string = ""
    for every_char in given_string:
        new_string = new_string+(every_char*2)
    return (new_string)
answer3 = double_string()
print(answer3)

#4th Question
def findEvenNum():
    given_list = list(map(int, input("enter the elements in list: ").split()))
    count = 0
    for every_num in given_list:
        if every_num%2 == 0:
            count+=1
    return count
answer4 = findEvenNum()
print(answer4)

