from turtle import *

# ---------- Screen setup ----------
bgcolor("#101010")
pensize(2)
speed(0)          # optional – drawing jaldi hoga
hideturtle()      # pehle se hi hide kar diya

# ---------- Initial positioning ----------
penup()
left(90)
forward(200)
pendown()
right(90)

# ---------- Flower base ----------
# (aapka base red tha, but aapne fill nahi kiya; yahaan red circle banaya gaya)
fillcolor("red")
begin_fill()
circle(0, 0)      # dummy call se pehle setheading zaroori hai
setheading(-83)
# simple red disc as flower-center
penup()
goto(0, -20)      # thoda neeche taaki center seedha rahe
pendown()
circle(20)
end_fill()

# ---------- Leaves ----------
# Leaf-1 (left side)
penup()
goto(0, 0)        # origin pe wapas
setheading(-83)
pendown()
pencolor("green")

forward(30)
left(90)
forward(25)
left(45)

fillcolor("green")
begin_fill()
circle(-80, 90)   # anticlockwise 90° arc
right(90)
circle(-80, 90)
end_fill()

# stem continue
right(135)
forward(60)
left(180)
forward(85)       # yahan aapka raw “25” theek se forward(25) likh diya
left(90)
forward(80)
right(90)

# Leaf-2 (right side)
right(45)
begin_fill()
circle(80, 90)    # clockwise 90° arc
left(90)
circle(80, 90)
end_fill()

left(135)
forward(60)
left(180)
forward(60)
right(90)

# extra decorative arc below
circle(200, 60)

# ---------- Text ----------
penup()
goto(-80, -220)
pendown()
color("white")
style = ("Arial", 30, "bold")
write("I Love You", font=style)

done()