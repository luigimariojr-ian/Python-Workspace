print("Welcome to Note Saver")

while True:

    print("""
    1. Add notes
    2. Read all notes
    3. Close Notes
          """)
    
    option = int(input("Selct an option from 1 - 3: "))#

    if option == 1:
        file = open("Notes.txt", "a")
        addtext = input("Add something about your day here: ")

        file.write(addtext)
        file.write("\n")
        
        file.close()
    
    if option == 2:
        file = open("Notes.txt", "r")

        diarycontent = file.read()
        print(diarycontent)
        
        file.close()
    
    if option == 3:
        print("Goodbye!")
        break