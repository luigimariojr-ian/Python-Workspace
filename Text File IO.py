type1 = input("What Type? ")

file = open("Txt IO.txt", type1)

addtext = input("Enter what you want to add in the file: ")

file.write(addtext)
file.write("\n")
file.close()

file = open("Txt IO.txt", "r")

filecontent = file.read()

print(filecontent)