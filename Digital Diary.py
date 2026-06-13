print("Welcome to Digital Diary")

while True:

    print("""
    1. Add something about your day
    2. Read the diary
    3. Exit
          """)
    
    option = int(input("Selct an option from 1 - 3: "))#

    if option == 1:
        file = open("Diary.txt", "a")
        addtext = input("Add something about your day here: ")

        file.write(addtext)
        file.write("\n")
        
        file.close()
    
    if option == 2:
        file = open("Diary.txt", "r")

        diarycontent = file.read()
        print(diarycontent)
        
        file.close()
    
    if option == 3:
        print("Goodbye!")
        break