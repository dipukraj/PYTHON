from turtle import *
from colorsys import *
speed(0)
bgcolor("black")
h = 1
for i in range(140):
    h -= 0.0015
    color(hsv_to_rgb(h, 1, 1))
    right(70)
    forward(i*2)
    circle(i*2, -10)
    left(100)
    up()
    forward(i)
    down()
    circle(i*2, -90)
    right(230)
done()
         