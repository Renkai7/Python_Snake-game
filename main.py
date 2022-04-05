from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

all_turtles = []
x_index = 0

# initialize snake
for turtle_index in range(3):
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.goto(x=x_index, y=0)
    x_index += -20
    all_turtles.append(new_turtle)


screen.exitonclick()
