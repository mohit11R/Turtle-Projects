import turtle
import random

pattern = turtle.Turtle()
pattern.color("black")
pattern.width(5)

num_sides = 6
side_length = 100
angle = 360.0/num_sides

for i in range(num_sides):
    pattern.forward(side_length)
    pattern.right(angle)

# pattern.setpos(90,0)
turtle.done()
