import time
from turtle import Screen

import food
import snake
from scoreboard import ScoreBoard

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
WINDOW_POSITION = 800


def finish_game():
    # seg_list = my_snake.segments_list
    # for i in range(my_snake.segments):
    #     seg_list[i].setposition(x=(i - 1) * 40, y=0)
    my_scoreboard.game_over()
    global game_not_finished
    game_not_finished = False
    screen.update()
    time.sleep(3)
    screen.bye()


screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, startx=WINDOW_POSITION)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

my_snake = snake.Snake()
my_food = food.Food()
my_scoreboard = ScoreBoard()

screen.listen()

screen.onkey(key='Right', fun=my_snake.right)
screen.onkey(key='Up', fun=my_snake.up)
screen.onkey(key='Down', fun=my_snake.down)
screen.onkey(key='Left', fun=my_snake.left)
screen.onkey(key='q', fun=finish_game)

game_not_finished = True
while game_not_finished:
    my_snake.move()
    screen.update()

    # Detect Collision with food
    distance_to_food = my_food.distance(my_snake.head)
    if distance_to_food <= my_food.smallest_distance:
        my_food.change_food_location()
        my_scoreboard.update_score()
        my_snake.extend()
    # Detect Collision with wall
    if my_snake.wall_collision():
        print("You hit the wall!")
        finish_game()
    print(my_snake.segments)
    # Detect Collision with tail
    for segment in my_snake.segments_list[1:]:
        if my_snake.head.distance(segment) < 5:
            print("You hit your tail")
            finish_game()
