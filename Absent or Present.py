Tasks = ["Jack", "Jessica", "Clyden", "Stacey", "Sophia", "Harry", "Ian", "Mattias", "Tanish", "Cyrus", "Summer"]

for i in Tasks:
    mark = int(input("Absent - 1 or Present - 2: "))
    currentitem = i
    index = Tasks.index(currentitem)
    currentitem = currentitem + " - " + str(mark)
    Tasks[index] = currentitem

print("2 = Present, 1 = Absent")
print(Tasks)