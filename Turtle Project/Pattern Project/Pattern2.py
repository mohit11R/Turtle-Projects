# OUTSIDE IN SQUARES
import turtle

pattern = turtle.Screen()
pattern.bgcolor("light grey")
pattern.title("Turtle")
shape = turtle.Turtle()
shape.color("blue")
shape.width(5)
 
def shapeOFSquare(size):
    for i in range(4):
        shape.fd(size)
        shape.left(90)
        size = size-5
 
shapeOFSquare(146)
shapeOFSquare(126)
shapeOFSquare(106)
shapeOFSquare(86)
shapeOFSquare(66)
shapeOFSquare(46)
shapeOFSquare(26)
# shapeOFSquare(6)

