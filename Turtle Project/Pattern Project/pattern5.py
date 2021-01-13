# SPIRAL HELIX PATTERN

import turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.color("white")
 
for i in range(100):
    t.circle(5*i)
    t.circle(-5*i)
    t.left(i)
 
