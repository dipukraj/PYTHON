from turtle import *
from colorsys import *
setposition(70, 20)
speed(0)
bgcolor("black")
h = 0

for i in range(100):
    c = hsv_to_rgb(h, 1, 1)
    pencolor(c)
    h += 0.005
    fd(170)
    lt(140)
    circle(150-i, 80)
    fd(150)
done()