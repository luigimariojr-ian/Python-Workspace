import random
num = random.randint(0, 10)

print(num)
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
color = random.choice(colors)
print(color)
random.shuffle(colors)
print(colors)
samplelist = random.sample(colors, k = 3)
print(samplelist)