import turtle
pen = turtle.Turtle()
paper = turtle.Screen()
paper.bgcolor("#C0EDFF")

def square(size, color):
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()

def triangle(size, color):
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

def rectangle(sizex, sizey, color):
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(sizex)
        pen.left(90)
        pen.forward(sizey)
        pen.left(90)
    pen.end_fill()


square(200, "#52361b")
triangle(200, "#1b2852")
pen.up()
pen.goto(60, -200)
pen.down()
rectangle(50, 100, "#1b1c0e")
pen.up()
pen.goto(120, -40)
pen.down()
square(50, "#c9faff")
pen.up()
pen.goto(20, -40)
pen.down()
square(50, "#c9faff")
pen.up()
pen.goto(-300, 300)
pen.down()
triangle(80, "#ffa600")
pen.up()
pen.goto(-220, 340)
pen.down()
pen.right(180)
triangle(80, "#ffa600")

paper.mainloop()
