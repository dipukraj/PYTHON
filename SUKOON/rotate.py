from turtle import *
from colorsys import *
tracer(20)
bgcolor('black')
h = 0
for i in range(145):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.008
    rt(i)
    width(2)
    circle(170,i)
    width(1)
    fd(i)
    rt(90)
    hideturtle()
down()