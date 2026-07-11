# Setup ---
import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("#000000")
dart = turtle.Turtle()
dart.color("#FFFFFF")
dart.shape("triangle")
dart.speed(0)

dart.up()
dart.goto(0, -350)
dart.seth(90)

# Balloons ---
balloon1 = turtle.Turtle()
balloon1.color("#2600FF")
balloon1.shape("circle")

balloon2 = turtle.Turtle()
balloon2.color("#FF6600")
balloon2.shape("circle")

balloon3 = turtle.Turtle()
balloon3.color("#FF0000")
balloon3.shape("circle")

balloon32 = turtle.Turtle()
balloon32.color("#FF0000")
balloon32.shape("circle")

balloon4 = turtle.Turtle()
balloon4.color("#00FF0D")
balloon4.shape("circle")

balloon42 = turtle.Turtle()
balloon42.color("#00FF0D")
balloon42.shape("circle")

balloons = [balloon1, balloon2, balloon3, balloon4, balloon32, balloon42]
for i in balloons:
    i.up()
    i.goto(random.randint(-380, 380), random.randint(300, 380))
    i.seth(270)
    i.speed(0)

def l():
    x = dart.xcor()
    dart.setx(x - 20)

def r():
    x = dart.xcor()
    dart.setx(x + 20)

screen.listen()
screen.onkey(l, "Left")
screen.onkey(r, "Right")

score = 0
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.color("#FFFFFF")
scoreboard.up()
scoreboard.goto(-41 ,370)
scoreboard.write("Score = " + str(score), font=(25))

while True:
    for i in balloons:
        i.forward(random.randint(4, 20))
        if i.ycor() < -400:
            i.goto(random.randint(-380, 380), random.randint(300, 380))
    if dart.distance(balloon4) < 15:
        balloon4.goto(random.randint(-380, 380), random.randint(300, 380))
        score += 1
        scoreboard.clear()
        scoreboard.write("Score = " + str(score), font=(25))
    if dart.distance(balloon42) < 15:
        balloon42.goto(random.randint(-380, 380), random.randint(300, 380))
        score += 1
        scoreboard.clear()
        scoreboard.write("Score = " + str(score), font=(25))
    if dart.distance(balloon3) < 15:
        balloon3.goto(random.randint(-380, 380), random.randint(300, 380))
        score -= 1
        scoreboard.clear()
        scoreboard.write("Score = " + str(score), font=(25))
    if dart.distance(balloon32) < 15:
        balloon32.goto(random.randint(-380, 380), random.randint(300, 380))
        score -= 1
        scoreboard.clear()
        scoreboard.write("Score = " + str(score), font=(25))
    if dart.distance(balloon1) < 15:
        balloon1.goto(random.randint(-380, 380), random.randint(300, 380))
        score *= 2
        scoreboard.clear()
        scoreboard.write("Score = " + str(score), font=(25))
    if dart.distance(balloon2) < 15:
        balloon2.goto(random.randint(-380, 380), random.randint(300, 380))
        score /= 2
        scoreboard.clear()
        scoreboard.write("Score = " + str(score), font=(25))

screen.mainloop()