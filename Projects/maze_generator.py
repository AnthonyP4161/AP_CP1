#AP 1st Period, Turtle Maze Generator
import turtle
import random
#make the turtle
maze = turtle.Turtle()
#generate the maze
def generate():
    maze.hideturtle()
    maze.speed(0)
    maze.penup()
    maze.goto(300,300)
    maze.pendown()
    maze.goto(0,300)
    maze.penup()
    maze.goto(-100,300)
    maze.pendown()
    maze.goto(-300,300)
    maze.goto(-300,-300)
    maze.goto(-100,-300)
    maze.penup()
    maze.goto(0,-300)
    maze.pendown()
    maze.goto(300,-300)
    maze.goto(300,300)
    maze.penup()
    maze.goto(-300,200)
    maze.penup()
    #call the function
generate()
#repeat it for every row
for i in range(1,6):
    #repeat again
    for i in range(1,7):
        #get a random integer to decide whether or not to place wall
        idk = random.randint(0,1)
        #get the y coordinates
        ycord=maze.ycor()
        #if idk was 1, it made a wall, if not it doesnt
        if idk == 1:
            maze.pendown()
            maze.forward(100)
            maze.penup()
        else:
            maze.forward(100)
    #goes down a row for next iteration
    maze.goto(-300,ycord-100)
#goes to start to set up for making columns
maze.goto(-200,300)
#same thing as making rows, just for columns now
for i in range(1,6):
    for i in range(1,7):
        idk = random.randint(0,1)
        xcord = maze.xcor()
        ycord = maze.ycor()
        if idk == 1:
            maze.pendown()
            maze.goto(xcord,ycord-100)
            maze.penup()
        else:
            maze.goto(xcord,ycord-100)
    maze.goto(xcord+100,300)
#exit the program when they click
turtle.exitonclick()