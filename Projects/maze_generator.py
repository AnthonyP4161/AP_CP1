#AP 1st Period, Turtle Maze Generator
import turtle
import random

#generate the maze
def generate():
    maze = turtle.Turtle()
    maze.hideturtle()
    maze.speed(0)
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
#check if the turtle is at the end
def is_solvable(row_grid,col_grid):
    size = len(row_grid)-1
    visited = set()
    stack = [(0,0)]
    while stack:
        x,y = stack.pop()

        if x == size-1 and y == size-1:
            return True
        if (x,y) in visited:
            continue
        visited.add((x,y))
        
        if x<size-1 and col_grid[y][x+1] == 0:
            stack.append((x+1,y))
        if y<size-1 and row_grid[y+1][x] == 0:
            stack.append((x,y+1))
        if x>0 and col_grid[y][x] == 0:
            stack.append((x-1,y))
        if y>0 and row_grid[y][x] == 0:
            stack.append((x,y-1))
    return False

generate()
turtle.exitonclick()