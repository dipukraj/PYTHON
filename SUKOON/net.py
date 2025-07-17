from turtle import *
from colorsys import *
tracer(10)
bgcolor("black")
R = 0
goto(270, -5)

for i in range(150):
    R += 0.0019
    circle(i, 190)
    color(hsv_to_rgb(R, 1, 1))
    forward(65)

    circle(220, 90)
done()

