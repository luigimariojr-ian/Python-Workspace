import time
import turtle
import random

star = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor(0, 0, 0)
startime = time.time()
star.hideturtle()
star.speed(0)
dtime = 1

for i in range (0, 50):
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    star.up()
    star.goto(x, y)
    star.down()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    size = random.randint(50, 150)
    star.color(r,g,b)
    star.fillcolor(r,g,b)
    star.begin_fill()
    for i in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()
    time.sleep(dtime)
    star.clear()
    dtime -= 0.05
    dtime = max(dtime, 0.02)

fintime = time.time()
totaltime = round(fintime - startime, 2)

ttime = turtle.Turtle()
ttime.color(255, 255, 255)
ttime.hideturtle()
ttime.up()
ttime.write("Total time : " + str(totaltime), font=("Arial", 25)) 

screen.mainloop()