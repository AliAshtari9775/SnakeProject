from turtle import Turtle

INITIAL_SCORE = 0
X_COR = 0
Y_COR = 270
X_REPORT = 0
Y_REPORT = 30
COLOR = 'white'
TEXT_FORMAT = ("Arial", 18, "normal")
ALIGN = 'center'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.fillcolor('black')
        self.hideturtle()
        self.pencolor(COLOR)
        self.penup()
        self.speed('fastest')
        self.setpos(x=X_COR, y=Y_COR)
        self.score = INITIAL_SCORE
        self.update_write()

    def update_write(self):
        self.write(arg=f"Score : {self.score}", align=ALIGN, font=TEXT_FORMAT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_write()

    def game_over(self):
        self.fillcolor('black')
        self.hideturtle()
        self.pencolor(COLOR)
        self.penup()
        self.speed('fastest')
        self.goto(x=X_REPORT, y=Y_REPORT)
        self.write(arg=f"You lost with Score : {self.score}", align=ALIGN, font=TEXT_FORMAT)
