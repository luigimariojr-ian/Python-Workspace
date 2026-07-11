import turtle

screen = turtle.Screen()
screen.bgcolor("#000000")
ball = turtle.Turtle()
ball.color("#FFFFFF")
ball.shape("circle")
paddle = turtle.Turtle()
paddle.color("#FFFFFF")
paddle.shape("square")

ball.up()
paddle.up()
paddle.goto(0,-340)

def paddleleft():

    x = paddle.xcor()
    x -= 40
    paddle.setx(x)

def paddleright():

    x = paddle.xcor()
    x += 40
    paddle.setx(x)

screen.listen()
screen.onkey(paddleleft, "Left")
screen.onkey(paddleright, "Right")

score = 0
scoreboard = turtle.Turtle()
scoreboard.up()
scoreboard.hideturtle()
scoreboard.color("#FFFFFF")
scoreboard.goto(-41, 370)
scoreboard.write("Score = " + str(score), font=(25))

for i in range(0, 3):
    for j in range(0, 7):
        screenx = -303 + j * 100
        screeny = 340 - i * 50
        brick = turtle.Turtle()
        brick.color("#FFFFFF")
        brick.shape("square")
        brick.speed(0)
        brick.up()
        brick.goto(screenx, screeny)

bx = -6
by = 6

while True:
    ball.setx(bx + ball.xcor())
    ball.sety(by + ball.ycor())

    if ball.xcor() > 450 or ball.xcor() < -450:
        bx *= -1
    
    if ball.ycor() > 400:
        by *= -1
    
    if ball.distance(paddle) < 15:
        by *= -1

screen.mainloop()