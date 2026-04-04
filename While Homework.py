import turtle
pen = turtle.Turtle()
paper = turtle.Screen()
paper.bgcolor("#0E0E0E")
pen.color("#ffffff")
i = 0

while i < 4:
    pen.forward(70)
    pen.left(90)
    i += 1

paper.mainloop()