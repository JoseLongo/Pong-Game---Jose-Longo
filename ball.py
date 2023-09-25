from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.start_x_speed = 3
        self.ball_x_speed = self.start_x_speed
        self.ball_y_speed = 3

    def move(self, r_paddle, l_paddle):
        current_x = self.xcor()
        current_y = self.ycor()
        new_pos = (current_x + self.ball_x_speed, current_y + self.ball_y_speed)
        self.goto(new_pos)

        if current_y > 270:
            if self.ball_y_speed > 0:
                self.ball_y_speed = -self.ball_y_speed
        elif current_y < -270:
            if self.ball_y_speed < 0:
                self.ball_y_speed = -self.ball_y_speed

        if self.distance(r_paddle) < 50 and self.xcor() > 320:
            if self.ball_x_speed > 0:
                self.ball_x_speed += 0.3
                self.ball_x_speed = -self.ball_x_speed
        elif self.distance(l_paddle) < 50 and self.xcor() < -320:
            if self.ball_x_speed < 0:
                self.ball_x_speed -= 0.3
                self.ball_x_speed = -self.ball_x_speed

    def reset(self):
        self.goto(0, 0)
        self.start_x_speed = -self.start_x_speed
        self.ball_x_speed = self.start_x_speed


