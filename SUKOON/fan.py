from turtle import *
from colorsys import *
tracer(20)
bgcolor("black")
h = 0
pensize(2)

for i in range(120):
    h += 0.0015
    color(hsv_to_rgb(h, 1, 1))
    goto(0, 0)
    circle(100, 180)
    fd(i+2)
    rt(40)
    for j in range(2):
        rt(70)
        fd(60)
        rt(80)
    hideturtle()
done()