from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

# listen for keystrokes
screen.listen()
screen.update()
time.sleep(0.8)

screen.onkey(key="d", fun=snake.move_east)
screen.onkey(key="w", fun=snake.move_north)
screen.onkey(key="a", fun=snake.move_west)
screen.onkey(key="s", fun=snake.move_south)

# start game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()




screen.exitonclick()
