from turtle import *
from colorsys import *
speed(0)
bgcolor("black")
h = 0
goto(270, -75)
for i in range(255):
    h += 0.0017
    color(hsv_to_rgb(h, 1, 1))
    lt(150)
    circle(400-i, 80)
    hideturtle()
done()