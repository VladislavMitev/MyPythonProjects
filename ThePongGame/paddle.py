from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_position)

    def move_up(self):
        if self.ycor() < 240:
            self.goto(x=self.xcor(), y=self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.goto(x=self.xcor(), y=self.ycor() - 20)

