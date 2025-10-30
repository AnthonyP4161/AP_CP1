#AP 1st period, Turtle Race
import random
import turtle

#Set the screen size and title
screen = turtle.Screen()
screen.setup(1500,1000)
screen.title("Turtle Race")

#make all the turtle with their colors and starting positions
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

#make the finish line
line = turtle.Turtle()
line.penup()
line.speed(67)
line.goto(700,700)
line.pendown()
line.goto(700,-1000)

#make a loop for the turtles to move
for x in range(1,10000):
    #make the turtles move forward a random amount
    t1.forward(random.randint(10,50))
    #check if the turle has crossed the finish line and use a turtle to write if one has for all of them, before breaking the loop
    if t1.xcor() >= 700:
        text = turtle.Turtle()
        text.color("red")
        text.hideturtle()
        text.penup()
        text.goto(0,300)
        text.pendown()
        text.write("Red Wins", align = "center",font=("arial",80,"normal"))
        break
    t2.forward(random.randint(10,50))
    if t2.xcor() >= 700:
        text = turtle.Turtle()
        text.color("blue")
        text.hideturtle()
        text.penup()
        text.goto(0,300)
        text.pendown()
        text.write("Blue Wins", align = "center",font=("arial",80,"normal"))
        break
    t3.forward(random.randint(10,50))
    if t3.xcor() >= 700:
        text = turtle.Turtle()
        text.color("yellow")
        text.hideturtle()
        text.penup()
        text.goto(0,300)
        text.pendown()
        text.write("Yellow Wins", align = "center",font=("arial",80,"normal"))
        break
    t4.forward(random.randint(10,50))
    if t4.xcor() >= 700:
        text = turtle.Turtle()
        text.color("green")
        text.hideturtle()
        text.penup()
        text.goto(0,300)
        text.pendown()
        text.write("Green Wins", align = "center",font=("arial",80,"normal"))
        break
    t5.forward(random.randint(10,50))
    if t5.xcor() >= 700:
        text = turtle.Turtle()
        text.color("purple")
        text.hideturtle()
        text.penup()
        text.goto(0,300)
        text.pendown()
        text.write("Purple Wins", align = "center",font=("arial",80,"normal"))
        break

#makes it so the screen closes when you click it
screen.exitonclick()