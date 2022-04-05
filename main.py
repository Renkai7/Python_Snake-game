from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

all_turtles = []
x_index = 0

# initialize snake
for turtle_index in range(3):
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=x_index, y=0)
    x_index += -20
    all_turtles.append(new_turtle)

game_is_on = True
while game_is_on:
    screen.update()
    # control movement speed
    time.sleep(0.1)

    # Snake movement
    for seg_num in range(len(all_turtles) - 1, 0, -1):
        new_x = all_turtles[seg_num - 1].xcor()
        new_y = all_turtles[seg_num - 1].ycor()
        all_turtles[seg_num].goto(new_x, new_y)

    all_turtles[0].forward(20)


screen.exitonclick()
