from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()
ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)


game_is_on = True
while game_is_on:
    ball.move(r_paddle=r_paddle, l_paddle=l_paddle)

    if ball.xcor() > 400:
        ball.reset()
        l_paddle.reset()
        r_paddle.reset()
        scoreboard.l_point()
    elif ball.xcor() < -400:
        ball.reset()
        l_paddle.reset()
        r_paddle.reset()
        scoreboard.r_point()
    screen.update()
    
screen.exitonclick()