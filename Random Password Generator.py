import random
import os
i = 1

while i == 1: 
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    num1 =  random.randint(0, 9)
    num2 =  random.randint(0, 9)
    spec = [",", "#", "/", "|", "[", "]", "{", "}", "*", "&", "^", "%", "$", "£", "!", "`", "¬", "?", "."]
    lower1 = random.choice(lower)
    lower2 = random.choice(lower)
    upper1 = random.choice(upper)
    upper2 = random.choice(upper)
    spec1 = random.choice(spec)
    spec2 = random.choice(spec)
    passwordlist = [lower1, lower2, upper1, upper2, str(num1), str(num2), spec1, spec2]
    random.shuffle(passwordlist)
    password = "".join(passwordlist)

    print("Your Password Is: " + password)
    ans = input("Do You Want A New Password? Yes or No:")
    if ans == "Yes" or ans == "yes":
        os.system('cls')
    elif ans == "No" or ans == "no":
        i = 0
        print("Okay!")
    elif ans == password:
        os.system('cls')
        print("That's the same thing... I'll take it as a yes.")
    elif ans == "password" or ans == "Password":
        os.system('cls')
        print("yep")
    elif ans == "idk":
        os.system('cls')
        print("SO DO I! I'M CONTROLLED BY ALGORITHMS!")
    else:
        os.system('cls')
        print("Invalid Input, will continue")