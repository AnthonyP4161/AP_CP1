#AP 1st Period, Turtle Maze Generator
import turtle
import random

maze = turtle.Turtle()
maze.hideturtle()
maze.speed(5)
maze.penup()
maze.goto(300,300)
maze.pendown()
maze.goto(50,300)
maze.penup()
maze.goto(-50,300)
maze.pendown()
maze.goto(-300,300)
maze.goto(-300,-300)
maze.goto(-50,-300)
maze.penup()
maze.goto(50,-300)
maze.pendown()
maze.goto(300,-300)
maze.goto(300,300)
for x in range(1,6):
    ycord = maze.ycor()-100
    xcord = maze.xcor()+50
    maze.penup()
    for x in range(1,6):
        maze.goto(xcord,ycord)
    maze.pendown()
    maze.goto(300,ycord)
turtle.exitonclick()