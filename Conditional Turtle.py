import turtle
pen = turtle.Turtle()
paper = turtle.Screen()

paper.bgcolor("#000000")
pen.color("#ffffff")

print("""
1. Draw a square.
2. Draw a circle.
3. Draw a triangle.
      """)

option = int(input("Enter number from 1 to 3: "))

if option == 1:
    for i in range(0, 4):
        pen.forward(70)
        pen.left(90)

elif option == 2:
    for i in range(0, 36):
        pen.forward(7)
        pen.left(10)

elif option == 3:
    for i in range(0, 3):
        pen.forward(70)
        pen.left(120)

paper.mainloop()