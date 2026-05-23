import turtle
import random
screen = turtle.Screen()
t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("#FF0000")
player = turtle.Turtle()
player.shape("turtle")
player.color("#FFD000")
t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("#2600FF")
flag = turtle.Turtle()
flag.shape("triangle")
flag.color("#1F9C25")

t1.up()
player.up()
t2.up()
flag.up()

t1.goto(400, -350)
player.goto(0, -350)
t2.goto(-400, -350)
flag.goto(0, 350)

t1.left(90)
player.left(90)
t2.left(90)
flag.right(90)

t1.down()
player.down()
t2.down()

def playerup():
    player.forward(10)

screen.listen()
screen.onkey(playerup, "space")
screen.onkey(playerup, "Up")
screen.onkey(playerup, "w")

opponents = [t1, t2]

result = turtle.Turtle()
result.up()
result.goto(0, 0)
result.hideturtle()

while True:
    for i in opponents:
        i.forward(random.randint(2, 4))
    if t1.ycor() > 350:
        result .write("Red Turtle Wins!", font=("Arial", 20, "normal"))
        break 
    if t2.ycor() > 350:
        result.write("Blue Turtle Wins!", font=("Arial", 20, "normal"))
        break
    if player.ycor() > 350:
        result.write("Yellow Turtle Wins!", font=("Arial", 20, "normal"))
        break


screen.mainloop()