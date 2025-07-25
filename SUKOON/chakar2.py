from turtle import *
from colorsys import *
tracer(10)
bgcolor("black")
h = 0

def draw(ang,n):
    circle(5+n, 69)
    left(ang)
    circle(3+2*n, 60)

goto(0, 10)
for i in range(150):
    h += 0.007
    c = hsv_to_rgb(h, 1, 1)
    color(c)
    up()
    draw(90, i)
    draw(180, i)
    down()
    draw(1/2, i-i)
    draw(180, i/2)
    draw(120, i-i)
    hideturtle()
up()