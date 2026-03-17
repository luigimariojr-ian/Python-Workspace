method = str(input("Add, subtract, multiply or divide (only small letters and spell correctly):"))
num1 = float(input("Put your first number here:"))
num2 = float(input("Put your second number here:"))
adding = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

if method == "add":
    print("Your answer is: " + str(adding))
elif method == "subtract":
    print("Your answer is: " + str(sub))
elif method == "multiply":
    print("Your answer is: " + str(mul))
elif method == "divide":
    print("Your answer is: " + str(div))
else:
    print("Invalid :(")
