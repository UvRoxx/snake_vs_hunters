from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from level import Level
from arrow import Arrow
from random import randint

# Code For Screen

screen = Screen()
screen.screensize(400, 400)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()
screen.title("Welcome To Snake Vs Hunters")

# Setup for Snake
obj_snake = Snake()
my_snake = obj_snake.snake

# Setup for Food
food = Food()

# Setup Level Board
level = Level()

# Setup and move Arrow
arrows = []


def move_arrows():
    for arrow in arrows:
        arrow.forward(10)


def did_hit():
    for arrow in arrows:
        for block in my_snake:
            if block.distance(arrow) < 10:
                return True


def go_again():
    user_input = screen.textinput("The Game is Over When You Say Its Over",
                                  "Wanna Go Again (Y/N)").title()
    if user_input == "Y" or user_input == "Yes":
        food.clear()
        food.reset()

        level.clear()
        level.reset()

        obj_snake.reset_snake()
        play_game()

    else:
        pass


def play_game():
    # Setup Bool For Gameplay Management
    game_is_on = True
    screen.listen()
    # Difficulty Parameter to Adjust
    arrow_shooting_period = 40
    game_time = 0.2

    while game_is_on:
        screen.update()
        sleep(game_time)

        # Movement Controls
        screen.onkey(obj_snake.up, "Up")
        screen.onkey(obj_snake.right, "Right")
        screen.onkey(obj_snake.down, "Down")
        screen.onkey(obj_snake.left, "Left")

        # Move Snake Ahead
        obj_snake.move()

        # Check food and Snake Collision
        if food.distance(my_snake[0]) < 14:
            food.reset()
            obj_snake.grow_snake()
            level.level_up()
            if level.level == 5:
                game_time -= 0.1
                level.get_ready()
            if level.level % 10 == 0:
                if arrow_shooting_period > 20:
                    arrow_shooting_period -= 2

        if obj_snake.hit_wall():
            level.game_over()
            game_is_on = False
            go_again()
        # Generate Arrows
        create_arrow = randint(1, arrow_shooting_period)
        if create_arrow == 1:
            arrows.append(Arrow())
        move_arrows()
        if did_hit():
            level.game_over()
            game_is_on = False
            go_again()


user_input = screen.textinput("Welcome",
                              "You Can Move Above And Beyond, Avoid Arrows and dont hit wall...Are You Ready(Yes/No)").title()

if user_input == 'Yes':
    play_game()
else:
    pass
screen.exitonclick()
