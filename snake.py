import turtle
from turtle import Turtle

MOVE_DISTANCE = 20
MOVE_EAST = 0
MOVE_NORTH = 90
MOVE_WEST = 180
MOVE_SOUTH = 270


class Snake:

    def __init__(self):
        self.x_index = 0
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):

        for snake_index in range(3):
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(x=self.x_index, y=0)
            self.x_index -= MOVE_DISTANCE
            self.snake_list.append(new_snake)

    def move(self):
        for seg_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[seg_num - 1].xcor()
            new_y = self.snake_list[seg_num - 1].ycor()
            self.snake_list[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_east(self):
        if self.head.heading() != MOVE_WEST:
            self.head.setheading(MOVE_EAST)

    def move_north(self):
        if self.head.heading() != MOVE_SOUTH:
            self.head.setheading(MOVE_NORTH)

    def move_west(self):
        if self.head.heading() != MOVE_EAST:
            self.head.setheading(MOVE_WEST)

    def move_south(self):
        if self.head.heading() != MOVE_NORTH:
            self.head.setheading(MOVE_SOUTH)
