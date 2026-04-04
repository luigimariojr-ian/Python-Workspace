fruits = ["apple", "strawberry", "pear", "plum", "avocado"]
print(fruits)
fruits.append("orange")
print(fruits)
fruits.append("watermelon")
print(fruits)
fruits.insert(3, "tangerine")
print(fruits)
fruits.insert(6, "muskmelon")
print(fruits)
fruits.remove("plum")
print(fruits)
del fruits[2]
print(fruits)
print(len(fruits))

for i in fruits:
    print(i)