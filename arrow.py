from turtle import Turtle
from random import randint
import randomcolor

SIDE = 300


class Arrow(Turtle):
    def __init__(self):
        super().__init__()
        self.side = randint(1, 4)
        self.setup()
        self.setup()

    def setup(self):
        self.shape('arrow')
        rand_color = randomcolor.RandomColor()
        self.color(rand_color.generate())
        self.shapesize(1, 1)
        self.penup()
        random = randint(-SIDE, SIDE)
        if self.side == 1:
            self.goto(random, SIDE)
            self.setheading(270)
        elif self.side == 2:
            self.goto(SIDE, random)
            self.setheading(180)

        elif self.side == 3:
            self.goto(random, -SIDE)
            self.setheading(90)

        elif self.side == 4:
            self.goto(-SIDE, random)
            self.setheading(0)
