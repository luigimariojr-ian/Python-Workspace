import turtle
import random
import time

player = turtle.Turtle()
screen = turtle.Screen()
player.color("#000000", "#2CFFAE")
screen.bgcolor("#47BBFF")
player.shape("square")
player.shapesize(1.6, 1, 3)
player.speed(0)
player.up()
player.goto(0, 50)

p1 = turtle.Turtle()
p2 = turtle.Turtle()
p3 = turtle.Turtle()
p4 = turtle.Turtle()
p5 = turtle.Turtle()
p6 = turtle.Turtle()

platforms = [p1, p2, p3, p4, p5, p6]

for i in platforms:
    i.speed(0)
    i.color("#000000", "#3B2511")
    i.shape("square")
    i.shapesize(1.3, 6, 3)
    i.up()
    i.goto(random.randint(-350, 350), random.randint(-350, 350))

c1 = turtle.Turtle()
c2 = turtle.Turtle()
c3 = turtle.Turtle()
c4 = turtle.Turtle()
c5 = turtle.Turtle()
c6 = turtle.Turtle()

coins = [c1, c2, c3, c4, c5, c6]

for i in coins:
    i.speed(0)
    i.color("#000000", "#FFFC3C")
    i.shape("circle")
    i.shapesize(1, 1, 3)
    i.up()
    index = coins.index(i)
    platform = platforms[index]
    i.goto(platform.xcor(), platform.ycor() + 35)

grr = turtle.Turtle()
grr.speed(0)
grr.color("#000000", "#E62727")
grr.shape("square")
grr.shapesize(1.5, 3, 3)
grr.up()

wee = turtle.Turtle()
wee.speed(0)
wee.color("#000000", "#0CFF03")
wee.shape("arrow")
wee.shapesize(1.7, 2.6, 3)
wee.up()
wee.goto(200000000000000, 200000000000000)

grr.seth(random.randint(-360, 360))

score = 0
scoreboard = turtle.Turtle()
scoreboard.up()
scoreboard.hideturtle()
scoreboard.color("#343D11")
scoreboard.goto(-41, 370)
scoreboard.write("Score = " + str(score), font=(25))

xvel = 40
yvel = 40
lives = 3

livesboard = turtle.Turtle()
livesboard.up()
livesboard.hideturtle()
livesboard.color("#343D11")
livesboard.goto(-41, 330)
livesboard.write("Lives = " + str(lives), font=(25))


def up():
    player.sety(yvel + player.ycor())
    coin_collect()

def down():
    player.sety(player.ycor() - yvel)
    coin_collect()

def left():
    player.setx(player.xcor() - xvel)
    coin_collect()

def right():
    player.setx(xvel + player.xcor())
    coin_collect()

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

def coin_collect():
    global score
    for i in coins:
        if player.distance(i) < 30:
            i.hideturtle()
            score += 1
            scoreboard.clear()
            scoreboard.write("Score = " + str(score), font=(25))
            i.goto(200000000000000, 200000000000000)


while True:
    grr.forward(13)

    if grr.xcor() > 400 or grr.ycor() > 400:
        grr.seth(random.randint(180, 360)) #180 to 360

    if grr.xcor() < -400 or grr.ycor() < -400:
        grr.seth(random.randint(-360, -180)) #180 to 360

    if grr.xcor() < -420 or grr.ycor() < -420 or grr.xcor() > 420 or grr.ycor() > 420:
        grr.goto(0, 0)
        grr.seth(random.randint(-360, 360))

    if score == 6:
        wee.goto(400, 350)

    if player.distance(wee) < 30:
        won = turtle.Turtle()
        won.up()
        won.hideturtle()
        won.color("#D2FC29")
        won.goto(-41, 0)
        won.write("YOU WIN!! :]", font=(100))
        xvel = 0
        yvel = 0
        break

    if player.distance(grr) < 30:
        lives -= 1
        livesboard.clear()
        livesboard.write("Lives = " + str(lives), font=(25))
        player.goto(0, 50)
    
    if lives == 0:
        won = turtle.Turtle()
        won.up()
        won.hideturtle()
        won.color("#FC2929")
        won.goto(-41, 0)
        won.write("YOU LOSE... :[", font=(100))
        xvel = 0
        yvel = 0
        break


screen.mainloop()