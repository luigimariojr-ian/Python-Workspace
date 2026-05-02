import turtle
import random
pen = turtle.Turtle()
paper = turtle.Screen()
paper.colormode(255)
paper.bgcolor(0,0,0)
pen.speed(100)

for i in range(0, 11):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pen.color(r,g,b)
    pen.fillcolor(r,g,b)
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.begin_fill()
    for l in range(0, 31):
        size = random.randint(50, 70)
        pen.forward(size)
        pen.backward(size)
        pen.left(12)
    pen.end_fill()


paper.mainloop()

