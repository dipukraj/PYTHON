from turtle import *
speed(0)
bgcolor("black")
color("#00ff00")
for i in range(135):
    forward(i)
    right(240)

    for j in range(3):
        forward(i)
        left(30)
        circle(40, 30)
    hideturtle()
done()