import turtle
pen = turtle.Turtle()
paper = turtle.Screen()
paper.bgcolor("#969696")
pen.color("#000000")

for i in range(0, 4):
    pen.forward(70)
    pen.left(90)

pen.up()
pen.goto(-100, 100)
pen.down()

for i in range(0, 3):
    pen.forward(70)
    pen.left(120)

pen.up()
pen.goto(100, 100)
pen.down()

for i in range(0, 5):
    pen.forward(70)
    pen.left(72)

pen.up()
pen.goto(-350, -350)
pen.down()

for i in range(0, 6):
    pen.forward(70)
    pen.left(60)


pen.up()
pen.goto(-70, 100)
pen.down()

pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(100)

pen.up()
pen.goto(-250, 250)
pen.down()

for i in range(0, 8):
    pen.forward(70)
    pen.left(45)

pen.up()
pen.goto(250, -250)
pen.down()

for i in range(0, 9):
    pen.forward(70)
    pen.left(40)

pen.up()
pen.goto(350, 250)
pen.down()

for i in range(0, 10):
    pen.forward(70)
    pen.left(36)

paper.mainloop()