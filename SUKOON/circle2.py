from turtle import *
from colorsys import *
setposition(50, -50)
speed(0)
bgcolor('black')
pensize(2)
n = 2
h = 0
for i in range(120):
    for i in range(4):
        color(hsv_to_rgb(h, 1, 1))
        forward(250)
        left(90)
        circle(40+i*5, 90)
        h += 0.003
    rt(10)
    hideturtle()
done()
