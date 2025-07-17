import turtle

# Screen setup
s = turtle.Screen()
s.setup(630, 700, startx=400, starty=0)
s.bgcolor("black")

# Turtle setup
t = turtle.Turtle()
t.pencolor("red")
t.speed(0)
t.penup()
t.goto(0, 150)
t.pendown()

# Drawing spiral
a = 0
b = 0
while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 204:
        break

t.hideturtle()
turtle.done()
