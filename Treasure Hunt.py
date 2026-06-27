import random

#Setup ---
iswin = False
tr = random.randint(1, 5)
tc = random.randint(1, 5)
print("Treasure Hunt Game! You have 4 attempts.")

#Grid ---
grid = []
def intialize_grid():
    global grid
    for i in range(0, 5):
        row = []
        for i in range(0, 5):
            row.append("-")
        grid.append(row)
intialize_grid()
for i in grid:
    print(i)

#Guesses & Attempts ---
for i in range(1, 5):
    gr = int(input("Enter row number (1-5): "))
    gc = int(input("Enter coloumn number (1-5): "))

    if gr > tr:
        print("Go Up")
    elif gr < tr:
        print("Go Down")
    else:
        if gc > tc:
            print("Go Left")
        elif gc < tc:
            print("Go Right")
        else:
            print("Congrats! The treasure was found!")
            print("Your attempt number is: " + str(i))
            iswin = True
            break

#Losing ---
if iswin == False:
    print("You lose... :( Better luck next time!")