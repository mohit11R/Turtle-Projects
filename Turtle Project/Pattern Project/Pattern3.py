# INSIDE OUT SQUARES

import turtle

pattern=turtle.Screen()
pattern.bgcolor("light grey")
shape = turtle.Turtle()
shape.color("blue")
shape.width(5)
def shapeOFSquare(size):
    for _ in range(4):
        shape.forward(size)
        shape.left(90)
        size = size +5


shapeOFSquare(6)
shapeOFSquare(26)
shapeOFSquare(46)
shapeOFSquare(66)
shapeOFSquare(86)
shapeOFSquare(106)
shapeOFSquare(126)
shapeOFSquare(146)