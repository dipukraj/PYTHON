from turtle import *
speed(0)
setposition(-40, 35)
bgcolor("black")
hideturtle()
for i in range(160):
    for c in range(5):
        color("orange")
        circle(160-i, 100)
        left(90)
        circle(160-i, 100)
        right(61)
done()