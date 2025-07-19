from turtle import *
tracer(50)
setposition(0, 25)
bgcolor("black")
colors = ["yellow", "red", "yellow", "red"]
hideturtle()
for i in range(80):
    for c in colors:
        color(c)
        circle(175-i, 100)
        left(90)
        circle(175-i, 100)
        right(60)
done()
