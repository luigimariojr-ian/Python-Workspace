import turtle
pen = turtle.Turtle()
paper = turtle.Screen()
pen.color("#000000")
paper.bgcolor("#c4c4c4")

def clear():
    pen.clear()

def dragger(x, y):
    pen.ondrag(None)
    pen.goto(x, y)
    pen.ondrag(dragger)

def goto(x, y):
    pen.goto(x, y)

def penup():
    pen.up()

def pendown():
    pen.down()

def space():
    pen.forward(10)

def left():
    pen.setheading(180)

def right():
    pen.setheading(0)

def up():
    pen.setheading(90)

def down():
    pen.setheading(-90)

paper.listen()
paper.onkey(penup, "w")
paper.onkey(pendown, "s")
paper.onkey(space, "space")
paper.onkey(left, "Left")
paper.onkey(right, "Right")
paper.onkey(up, "Up")
paper.onkey(down, "Down")
paper.onclick(goto)
pen.ondrag(dragger)
paper.onkey(clear, "c")


paper.mainloop()