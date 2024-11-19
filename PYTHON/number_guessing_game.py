
import random

def generate_number():
    numbers = list(range(10))
    secret_number = []
    while len(secret_number) < 3:
        random.shuffle(numbers)
        secret_number = numbers[:3]
    print(f'Computer guessed number is {secret_number}')
    return secret_number

def user_number():
    user_guess_list = list(map(int,input("Enter your guess number: ")))
    print(f"User guessed number is : {user_guess_list}")
    return user_guess_list

if __name__ == "__main__":
    secret_number = generate_number()
    #print(f'Computer guessed number is {secret}')
    user_guess_list = user_number()
    #print(f"User guessed number is : {user_list}")
    user_input_not_matched = True 
    while user_input_not_matched:
        if secret_number == user_guess_list:
            print('Match. You have guessed a correct number in correct order.')
            user_input_not_matched = False
            continue
        elif set(secret_number) == set(user_guess_list):
            print('Close. You have same number but in different order.')
        else:
            print("Nope.You haven't guessed any number correctly.")
        
        user_guess_list = list(map(int,input("Enter your guess number: ")))
        