from turtle import Turtle

INITIAL_SCORE = 0
INITIAL_HIGHSCORE = 4
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
        with open("data.txt",mode='r') as file:
            self.highscore = int(file.read())
        self.score = INITIAL_SCORE
        self.update_write()

    def update_write(self):
        self.write(arg=f"Score : {self.score} || Highscore : {self.highscore}", align=ALIGN, font=TEXT_FORMAT)

    def update_score(self):
        self.clear()
        self.update_write()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode='w') as file:
                file.write(f"{self.highscore}")
        self.score = INITIAL_SCORE
        self.update_score()

    def game_over(self):
        self.fillcolor('black')
        self.hideturtle()
        self.pencolor(COLOR)
        self.penup()
        self.speed('fastest')
        self.goto(x=X_REPORT, y=Y_REPORT)
        self.write(arg=f"GAME OVER", align=ALIGN, font=TEXT_FORMAT)
