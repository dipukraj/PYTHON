from turtle import *
from colorsys import *
import random

speed(0)
bgcolor("black")
pensize(2)

def draw_rotating_design():
    h = random.random()  # random color starting point
    angle_shift = random.randint(10, 30)  # how much it rotates each time
    radius = 150  # FIXED radius now

    for i in range(100):
        r, g, b = hsv_to_rgb(h, 1, 1)
        color(r, g, b)
        h += 0.01  # color change
        circle(radius, 80)  # fixed-size circle
        left(90 + angle_shift)
        circle(radius, 80)
        left(angle_shift)

    clear()  # clear after one design

while True:
    draw_rotating_design()
