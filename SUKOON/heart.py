from turtle import *
bgcolor("black")
pencolor("white")
fillcolor("red")
pensize(5)
def heart(f, c):
    begin_fill()
    left(40)
    forward(f)
    circle(c, 200)
    rt(120)
    circle(c, 200)
    forward(f)
    end_fill()
penup()
goto(-50, -70)
pendown()
heart(140, 70)
penup()
goto(70, 70)
pendown()
left(40)
heart(100, 50)

style = ('Arial', 20, 'bold')
penup()
goto(-175, -150)
pendown()
write("I LOVE YOU", font=style, align='center')
hideturtle()
done()