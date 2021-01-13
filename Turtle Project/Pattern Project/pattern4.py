# RAINBOW BENZENE

import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
pattern=turtle.Screen()
pattern.bgcolor("black")
t = turtle.Turtle()
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)

