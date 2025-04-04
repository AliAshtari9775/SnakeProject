from turtle import Turtle
import random

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600
WIGGLE_ROOM = 20
SIZE = 0.5
SHAPE = 'circle'
COLOR = 'red'
DISTANCE = 15


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(SIZE)
        self.color(COLOR)
        random_x = random.randint(-CANVAS_WIDTH // 2 + WIGGLE_ROOM, CANVAS_WIDTH // 2 - WIGGLE_ROOM)
        random_y = random.randint(-CANVAS_HEIGHT // 2 + WIGGLE_ROOM, CANVAS_HEIGHT // 2 - WIGGLE_ROOM)
        self.setpos(x=random_x, y=random_y)
        self.speed('fastest')
        self.smallest_distance = DISTANCE
        # self.smallest_distance = 3 * math.sqrt(2) * (10 * self.shapesize()[0])

    def change_food_location(self):
        random_x = random.randint(-CANVAS_WIDTH // 2 + WIGGLE_ROOM, CANVAS_WIDTH // 2 - WIGGLE_ROOM)
        random_y = random.randint(-CANVAS_HEIGHT // 2 + WIGGLE_ROOM, CANVAS_HEIGHT // 2 - WIGGLE_ROOM)
        self.setpos(x=random_x, y=random_y)
