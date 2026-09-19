import turtle
import time

turt = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("#000000")
turt.color("#FFFFFF")
turt.speed(0)
turt.shape("turtle")
turt.up()


maze = [
"XXXXXXXXXXXXX",    
"XX  XXXX F XX",
"X T XXX   XXX",
"X   XXXX    X",
"XX   XXX   XX",
"XXXCXXXXXX XX",
"XXX      X XX",
"XXXXXX  XXCXX",
"X C     XX XX",
"XXXXX    X XX",
"XXXXXXX     X",
"XXXXXXXXXXXXX"
]

for i in range(0, 12):
    current_y = 200 - i * 30
    for j in range(0, 13):
        current_character = maze[i][j]
        current_x = -300 + j * 30

        if current_character == "X":
            obstacle = turtle.Turtle()
            obstacle.speed(0)
            obstacle.shape("square")
            obstacle.color("#FFFFFF")
            obstacle.up()
            obstacle.goto(current_x, current_y)

        if current_character == "F":
            finish = turtle.Turtle()
            finish.speed(0)
            finish.shape("triangle")
            finish.color("#83FF98")
            finish.up()
            finish.goto(current_x, current_y)

        if current_character == "C":
            coins = turtle.Turtle()
            coins.speed(0)
            coins.shape("circle")
            coins.shapesize(1, 0.8, 0)
            coins.color("#FFFD83")
            coins.up()
            coins.goto(current_x, current_y)

        if current_character == "T":
            turt.goto(current_x, current_y)

#controls

def up():
    turt.seth(90)
    turt.forward(30)

def down():
    turt.seth(270)
    turt.forward(30)

def left():
    turt.seth(180)
    turt.forward(30)

def right():
    turt.seth(0)
    turt.forward(30)

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

score = 0
scoreboard = turtle.Turtle()
scoreboard.up()
scoreboard.hideturtle()
scoreboard.color("#FFFFFF")
scoreboard.goto(165, 50)
scoreboard.write("Score = " + str(score), font=("Arial", 30))

timer = 0
timerboard = turtle.Turtle()
timerboard.up()
timerboard.hideturtle()
timerboard.color("#FFFFFF")
timerboard.goto(165, -50)
timerboard.write("Time = " + str(timer), font=("Arial", 30))

while True:
    time.sleep(1)
    timer += 1
    timerboard.clear()
    timerboard.write("Time = " + str(timer), font=("Arial", 30))

screen.mainloop()
