import turtle
import math
import random

turtle.screensize(canvwidth=1000, canvheight=750)
turtle.hideturtle()
turtle.left(90)
turtle.penup()
turtle.backward(250)
turtle.right(90)
turtle.pendown()

turtle.bgcolor('LemonChiffon3')
turtle.color('dim grey')
turtle.pensize(1.3)
turtle.hideturtle()
turtle.speed(0)
turtle.delay(0)


def qiguai(a,b):
    if a > 2:
        turtle.width(b)
        turtle.fd(a)
        turtle.left(90)
        turtle.fd(a)
        turtle.left(90)
        turtle.fd(a)
        turtle.left(90)
        turtle.fd(a)
        turtle.left(180)
        turtle.fd(a)
        turtle.left(45)
        turtle.penup()
        turtle.fd(a/10)
        turtle.right(90)
        turtle.down()
        qiguai(a/math.sqrt(2)*random.choice([1,1.05]), b/math.sqrt(2))
        turtle.up()
        turtle.right(90)
        turtle.fd(a/10)
        turtle.left(45)
        turtle.fd(a)
        turtle.left(45)
        turtle.fd(a/10)
        turtle.left(90)
        turtle.fd(a / math.sqrt(2))
        turtle.left(180)
        turtle.down()
        qiguai(a / math.sqrt(2)*random.choice([1,1,1.1]), b / math.sqrt(2))
        turtle.up()
        turtle.fd(a / math.sqrt(2))
        turtle.left(90)
        turtle.bk(a / 10)
        turtle.bk(a * math.sqrt(2))
        turtle.right(45)
        turtle.down()


turtle.tracer(0)
qiguai(100,5)
turtle.update()
turtle.mainloop()