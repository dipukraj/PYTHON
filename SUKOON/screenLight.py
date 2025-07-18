import turtle
import colorsys

t = turtle.Turtle()

# 1. screen() → Screen() (capital ‘S’)
scr = turtle.Screen()
scr.bgcolor("black")

t.speed(0)
t.pensize(2)
n = 38
h = 0

for i in range(80):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1/n
    t.pencolor(c)
    for j in range(5):
        # 2. Negative “i-3” pe turtle piche chal jaata hai, isliye max(i-3,0)
        t.forward(max(i - 3, 0))
        t.right(9 * 5)
        t.left(8)
    t.right(115)

turtle.done()