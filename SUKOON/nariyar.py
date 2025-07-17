from turtle import *
from colorsys import *

speed(0)
bgcolor("black")
R = 0
for i in range(180):
    R += 0.0019
    color(hsv_to_rgb(R, 1, 1))
    circle(3 - i, 80)
    rt(160)
    circle(i, 80)
    lt(80)
    hideturtle()
done()
    