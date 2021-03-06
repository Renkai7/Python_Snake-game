from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.snake_list[1:]:
        if segment in snake.snake_list:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            screen.clear()
            snake.reset()
    # If head collides with any segment in the tail:
        # trigger game_over
screen.exitonclick()
