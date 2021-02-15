# Imported Libraries
from turtle import Turtle
import randomcolor

# CONSTANTS
SNAKE_SPEED = 20
WALL_DISTANCE = 380


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for index in range(4):
            block = self.make_block()
            position = index * -30
            block.setx(position)
            block.setheading(90)
            self.snake.append(block)

    def move(self):
        for index in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[index - 1].xcor()
            new_y = self.snake[index - 1].ycor()
            self.snake[index].goto(new_x, new_y)
        self.snake[0].forward(SNAKE_SPEED)

    def grow_snake(self):
        new_block = self.make_block()
        new_x = self.snake[-1].xcor() + 1
        new_y = self.snake[-1].ycor() + 1
        new_block.goto(new_x, new_y)
        self.snake.append(new_block)

    def make_block(self):
        rand_color = randomcolor.RandomColor()
        block = Turtle("square")
        block.color(rand_color.generate())
        block.shapesize(1, 1)
        block.penup()

        return block

    def up(self):
        self.snake[0].setheading(90)

    def down(self):
        self.snake[0].setheading(270)

    def right(self):
        self.snake[0].setheading(0)

    def left(self):
        self.snake[0].setheading(180)

    def hit_wall(self):
        if self.snake[0].xcor() >= WALL_DISTANCE or self.snake[0].xcor() <= -WALL_DISTANCE or self.snake[
            0].ycor() >= WALL_DISTANCE or self.snake[0].ycor() <= -WALL_DISTANCE:
            return True
        else:
            return False

    def reset_snake(self):
        for segments in self.snake:
            segments.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.snake[0].goto(0, 0)
