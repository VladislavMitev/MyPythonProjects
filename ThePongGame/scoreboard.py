from turtle import Turtle

FONT = ("Courier", 70, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.x_val = 60
        self.y_val = 200
        self.update_score()

    def update_score(self):
        self.clear()
        if self.l_score >= 10 or self.r_score >= 10:
            self.x_val = 85
        self.goto(-self.x_val, self.y_val)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(0, self.y_val)
        self.write("-", align="center", font=FONT)
        self.goto(self.x_val, self.y_val)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

