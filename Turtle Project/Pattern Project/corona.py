import turtle as Turtle

a = 0
b = 0
pattern=Turtle.Screen()
pattern.bgcolor("black")
Turtle.speed(0)
Turtle.pencolor("green")
Turtle.penup()
Turtle.goto(0,200)
Turtle.pendown()

while True:
    Turtle.forward(a)
    Turtle.right(b)
    a+=3
    b+=1
    if b==201:
        break

Turtle.exitonclick()