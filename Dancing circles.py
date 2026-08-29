import turtle
import random
import time

pen = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor(0, 0, 0)
pen.speed(0)
delay = 1
starttime = time.time()
pen.hideturtle()

for i in range(0, 50):
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    pen.up()
    pen.goto(x, y)
    pen.down()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pen.color(r, g, b)
    pen.fillcolor(r, g , b)
    pen.begin_fill()
    pen.circle(random.randint(50, 150))
    pen.end_fill()
    time.sleep(delay)
    pen.clear()
    delay -= 0.05
    delay = max(delay, 0.02)

endtime = time.time()
elapsedtime = round(endtime - starttime, 2)

etime = turtle.Turtle()
etime.color(255, 255, 255)
etime.hideturtle()
etime.up()
etime.write("Animation time : " + str(elapsedtime), font=("Arial", 25) ) 

screen.mainloop()