from turtle import Turtle
import time

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
WINDOW_POSITION = 800

NUMBER_OF_SEGMENTS = 3
SIZE = 20
MOVE_DISTANCE = 20
DELAY = 0.1
INITIAL_HEADING = 90
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments_list = []
        self.segments = NUMBER_OF_SEGMENTS
        self.delay = DELAY
        self.size = SIZE
        self.heading = INITIAL_HEADING
        self.positions = INITIAL_POSITION
        self.create_snake()
        self.head = self.segments_list[0]
        self.head_angle = self.head.heading()
        self.head_position = self.head.position()

    def create_snake(self):
        for position in self.positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_square = Turtle(shape='square')
        new_square.penup()
        new_square.color('white')
        new_square.setposition(position)
        self.segments_list.append(new_square)

    def move(self):
        time.sleep(self.delay)
        prev = [segment.pos() for segment in self.segments_list]
        self.head.forward(MOVE_DISTANCE)
        for i in range(1, self.segments):
            self.segments_list[i].setpos(prev[i - 1])
            # screen.update()
        self.head_position = self.head.position()
        self.head_angle = self.head.heading()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def wall_collision(self):
        calcx = (WINDOW_WIDTH / 2 - 5) - abs(self.head.xcor())
        calcy = (WINDOW_HEIGHT / 2 - 5) - abs(self.head.ycor())
        if calcx <= 5 or calcy <= 10:
            return True
        else:
            return False

    def extend(self):
        self.segments += 1
        x_extend = self.segments_list[-1].xcor()
        y_extend = self.segments_list[-1].ycor()
        self.add_segment((x_extend, y_extend))
