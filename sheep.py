import turtle
import math


turtle.hideturtle()
turtle.left(45)
turtle.penup()
turtle.backward(350)
turtle.pendown()
turtle.right(45)
turtle.bgcolor('dark slate gray')
turtle.color('dim grey')
turtle.pensize(1.3)
turtle.hideturtle()
turtle.speed(0)
turtle.delay(0)


def qiguai(a):
    if a >0.8:
        turtle.fd(a)
        turtle.left(90)
        turtle.fd(a)
        turtle.left(90)
        turtle.fd(a)
        turtle.right(120)
        qiguai(a/2)
        turtle.fd(a/2)
        turtle.right(90)
        qiguai(math.sqrt(3)/2*a)
        turtle.right(90)
        turtle.fd(a / 2)
        turtle.left(30)
        turtle.fd(a)
        turtle.left(90)


turtle.tracer(0)
qiguai(120)
turtle.update()
turtle.mainloop()