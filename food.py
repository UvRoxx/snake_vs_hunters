from turtle import Turtle
import randomcolor
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.setup()

    def reset(self):
        self.clear()
        self.setup()

    def setup(self):
        rand_color = randomcolor.RandomColor()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.color(rand_color.generate())
        self.penup()
        self.goto(randint(-150, 150), randint(-150, 150))
