import turtle
import random
pen = turtle.Turtle()
paper = turtle.Screen()
paper.colormode(255)
paper.bgcolor(0, 0, 0)
pen.speed(0)

for i in range(0, 21):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pen.color((r, g, b))
    pen.fillcolor((r, g, b))
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    pen.up()
    pen.goto(x, y)
    pen.down()
    size = random.randint(20, 40)
    pen.begin_fill()
    for s in range(0, 6):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()


paper.mainloop()