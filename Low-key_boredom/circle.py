import turtle
turt = turtle.Turtle()
turt.speed(1000000)
for x in range(1,100000):
    turt.penup()
    turt.goto(400,0)
    turt.pendown()
    turt.forward(50)
    turt.left(.5)
turtle.exitonclick()