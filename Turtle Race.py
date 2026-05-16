import turtle
import random
player = turtle.Turtle()
player.shape("turtle")
player.color("#8c34eb")
screen = turtle.Screen()
t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("#eb3434")
t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("#34eb62")
t3 = turtle.Turtle()
t3.shape("turtle")
t3.color("#e5ff00")
t4 = turtle.Turtle()
t4.shape("turtle")
t4.color("#3734eb")
flag = turtle.Turtle()
flag.shape("triangle")
flag.color("#18642b")

player.up()
t1.up()
t2.up()
t3.up()
t4.up()
flag.up()

player.goto(-400, 300)
t1.goto(-400, 150)
t2.goto(-400, 0)
t3.goto(-400, -150)
t4.goto(-400, -300)
flag.goto(400, 0)


def forward():
    player.forward(10)

screen.listen()
screen.onkey(forward, "space")

opponents = [t1, t2, t3, t4]

result = turtle.Turtle()
result.up()
result.goto(0, 0)
result.hideturtle()

while True:
    for i in opponents:
        i.forward(random.randint(2, 5))
    if t1.xcor() > 400:
        result.write("Red Turtle Wins!")
        break
    if t2.xcor() > 400:
        result.write("Green Turtle Wins!")
        break
    if t3.xcor() > 400:
        result.write("Yellow Turtle Wins!")
        break
    if t4.xcor() > 400:
        result.write("Blue Turtle Wins!")
        break
    if player.xcor() > 400:
        result.write("Purple Turtle Wins!")
        break

screen.mainloop()