#AP 1st period, Turtle Race
import random
import turtle

screen = turtle.Screen()
screen.setup(1500,1000)
screen.title("Turtle Race")

t1 = turtle.Turtle()
t1.color("red")
t1.shape("turtle")
t1.penup()
t1.speed(1000)
t1.goto(-700,200)
t1.pendown()
t1.speed(random.randint(1,5))

t2 = turtle.Turtle()
t2.color("blue")
t2.shape("turtle")
t2.penup()
t2.speed(1000)
t2.goto(-700,100)
t2.pendown()
t2.speed(random.randint(1,5))

t3 = turtle.Turtle()
t3.color("yellow")
t3.shape("turtle")
t3.penup()
t3.speed(1000)
t3.goto(-700,0)
t3.pendown()
t3.speed(random.randint(1,5))

t4 = turtle.Turtle()
t4.color("green")
t4.shape("turtle")
t4.penup()
t4.speed(1000)
t4.goto(-700,-100)
t4.pendown()
t4.speed(random.randint(1,5))

t5 = turtle.Turtle()
t5.color("purple")
t5.shape("turtle")
t5.penup()
t5.speed(1000)
t5.goto(-700,-200)
t5.pendown()
t5.speed(random.randint(1,5))

line = turtle.Turtle()
line.penup()
line.goto(700,700)
line.pendown()
line.goto(700,0)

for x in range(1,10000):
    t1.forward(random.randint(10,50))
    if t1.xcor() >= 1000:
        break
    t2.forward(random.randint(10,50))
    if t2.xcor() >= 1400:
        break
    t3.forward(random.randint(10,50))
    if t3.xcor() >= 1400:
        break
    t4.forward(random.randint(10,50))
    if t4.xcor() >= 1400:
        break
    t5.forward(random.randint(10,50))
    if t5.xcor() >= 1400:
        break

turtle.done()