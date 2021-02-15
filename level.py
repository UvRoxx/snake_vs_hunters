from turtle import Turtle
import randomcolor


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.setup()

    def setup(self):
        rand_color = randomcolor.RandomColor()
        self.color(rand_color.generate())
        self.penup()
        self.hideturtle()
        self.goto(0, 300)
        self.write(f"Level - {self.level}", align="center", font=("Comic Sans", 20, "bold"))

    def level_up(self):
        self.clear()
        self.level += 1
        self.setup()

    def game_over(self):
        self.clear()
        self.setup()
        self.goto(0, 0)
        self.write("Game Over",align="center", font=("Comic Sans", 40, "bold"))

    def get_ready(self):
        self.clear()
        self.write("Get Ready!!!", align="center", font=("Comic Sans", 20, "bold"))
    def reset(self):
        self.level = 0
        self.setup()


