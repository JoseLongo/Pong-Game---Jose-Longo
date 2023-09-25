from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        current_pos = self.pos()
        self.goto(self.pos()[0], self.pos()[1] + 30)

    def move_down(self):
        current_pos = self.pos()
        self.goto(self.pos()[0], self.pos()[1] - 30)

    def reset(self):
        self.goto(self.xcor(), 0)
