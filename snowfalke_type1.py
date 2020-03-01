import turtle
import math


turtle.hideturtle()
turtle.bgcolor('dark slate gray')
turtle.color('snow')
turtle.pensize(1.3)
turtle.left(60)
turtle.hideturtle()
turtle.speed(0)
turtle.delay(0)


def snow_flower(a):
    if a >1:
        turtle.fd(a)
        turtle.left(60)
        snow_flower((3-math.sqrt(5))/2*a)
        turtle.right(60)
        snow_flower((math.sqrt(5)- 1) / 2 * a)
        turtle.right(60)
        snow_flower((3 - math.sqrt(5)) / 2 * a)
        turtle.left(60)
        turtle.back(a)

turtle.tracer(0)
for i in range(6):
    snow_flower(150)
    turtle.left(60)

turtle.update()
turtle.mainloop()