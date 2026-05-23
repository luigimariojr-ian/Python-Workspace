import turtle
import random
snake = turtle.Turtle()
screen = turtle.Screen()
snake.color("#FFFFFF")
screen.bgcolor("#000000")
snake.shape("square")
apple = turtle.Turtle()
apple.shape("circle")
apple.color("#FFFFFF")


snake.up()
apple.up()

snake.goto(0, 0)
apple.goto(200, 0)

def left():
    snake.setheading(180)

def right():
    snake.setheading(0)

def up():
    snake.setheading(90)

def down():
    snake.setheading(-90)

score = 0
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.color("#FFFFFF")
scoreboard.up()
scoreboard.goto(-30, 350)
scoreboard.write("Score: " + str(score), font=("Arial", 15, "normal"))

screen.listen()
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(up, "Up")
screen.onkey(down, "Down")

while True:
    snake.forward(3)
    if snake.xcor() < -450 or snake.xcor() > 450:
        result = turtle.Turtle()
        result.hideturtle()
        result.color("#FFFFFF")
        result.up()
        result.goto(-30, -350)
        result.write("Game Over!", font=("Arial", 15, "normal"))
        break
    if snake.ycor() < -400 or snake.ycor() > 400:
        result = turtle.Turtle()
        result.hideturtle()
        result.color("#FFFFFF")
        result.up()
        result.goto(-30, -350)
        result.write("Game Over!", font=("Arial", 15, "normal"))
        break
    if snake.distance(apple) < 15:
        score = score + 1
        scoreboard.clear()
        scoreboard.write("Score: " + str(score), font=("Arial", 15, "normal"))
        x = random.randint(-400, 400)
        y = random.randint(-350, 350)
        apple.goto(x, y)


screen.mainloop()