from turtle import *
from colorsys import *
bgcolor("black")
tracer(5)
pensize(1.5)
def square(x):
    for i in range(40):
        forward(x)
        left(100)
    forward(x)
n = 30
for i in range(16):
    color(hls_to_rgb(20, 1-i/n, 1))
    for j in range(5):
        square(5+(i*7))
    hideturtle()
done()
                
    