import random
import os
i = 1

while i == 1: 
    name = input("What is your name? ")
    num1 =  random.randint(0, 9)
    num2 =  random.randint(0, 9)
    spec = [",", "#", "/", "|", "[", "]", "{", "}", "*", "&", "^", "%", "$", "£", "!", "`", "¬", "?", "."]
    spec1 = random.choice(spec)
    spec2 = random.choice(spec)
    userlist = [str(num1), str(num2), spec1, spec2]
    random.shuffle(userlist)
    username = "".join(userlist)
    usernametrue = name + username

    print("Your Username is Is: " + usernametrue)
    ans = input("Do You Want A New Username? Yes or No:")
    if ans == "Yes" or ans == "yes":
        os.system('cls')
    elif ans == "No" or ans == "no":
        i = 0
        print("Okay!")
    else:
        os.system('cls')
        print("Invalid Input, will continue")