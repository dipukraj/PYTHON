import math
from turtle import *


def heart_a(n):
    return 16 * math.sin(n) ** 3



def heart_b(n):
    return 13 * math.cos(n)-5 *\
           math.cos(2*n) - 2 *\
           math.cos(3*n) - \
           math.cos(4*n)

speed(10)
bgcolor("black")
for i in range(700):
    goto(heart_a(i)*15, heart_b(i)*15)
    for j in range(1):
        color('#f73487')
    hideturtle()
done()     