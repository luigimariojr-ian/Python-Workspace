import random

num = random.randint(1, 20)
ans = 0
while ans != num:
    ans = int(input("Guess the number from 1 to 20: "))

    if ans == num:
        print("Congratulations! The number was: " + str(num))

    if ans < num:
        print("Go Higher!")

    if ans > num:
        print("Go Lower!")
