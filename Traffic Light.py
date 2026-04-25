import turtle
pen = turtle.Turtle()
paper = turtle.Screen()

def rectangle (sizex, sizey, color):
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(sizex)
        pen.left(90)
        pen.forward(sizey)
        pen.left(90)
    pen.end_fill()

def circle(radius, color):
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

rectangle(150, 320, "#000000")
pen.up()
pen.goto(70, 0)
pen.down()
circle(50, "#ff0000")
pen.up()
pen.goto(70, 104)
pen.down()
circle(50, "#ff6600")
pen.up()
pen.goto(70, 208)
pen.down()
circle(50, "#2bff00")

paper.mainloop()