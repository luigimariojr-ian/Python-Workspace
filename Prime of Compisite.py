n = int(input("Put your number here: "))

flag = True
for i in range(2, n):
    if n % i == 0:
        flag = False
        print("Your number is a composite number!")
        break
if flag == True:
    print("Your number is prime!")