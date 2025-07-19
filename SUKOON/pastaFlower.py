from turtle import *
from colorsys import *
tracer(10)
bgcolor("black")
pensize(2)
h =0

def draw(int, t):
    circle(5+t, 90)
    left(int)
    circle(5+t, 60)

for i in range(200):
    c = hsv_to_rgb(h, 1, 1)
    h += 0.005
    color(c)
    up()
    draw(90, i/50)
    draw(180, i/4)
    down()
    fillcolor("black")
    begin_fill()
    draw(1/2, 0)
    draw(180, i/4)
    draw(90, i/4)
    end_fill()
    draw(60, i/4)
    hideturtle()
done()


