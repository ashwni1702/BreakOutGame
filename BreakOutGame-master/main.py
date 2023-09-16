from turtle import Screen, tracer, update
from brick import Brick
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
# GAME CONSTANTS
VERTICAL_LIMIT = 385
HORIZONTAL_LIMIT = 720
INITIAL_PADDLE_POSITION = (0, -320)
INITIAL_BALL_POSITION = (0, -305)


screen = Screen()
screen.title("Break Out")
screen.bgcolor("black")
screen.setup(width=1400, height=750)
tracer(0, 0)

scoreboard = ScoreBoard()

brick_x_axis = -HORIZONTAL_LIMIT
brick_y_axis = 330
bricks = []
for i in range(7):
    for j in range(23):
        brick = Brick((brick_x_axis, brick_y_axis))
        bricks.append(brick)
        brick_x_axis += 65
    brick_x_axis = -HORIZONTAL_LIMIT
    brick_y_axis -= 20
ball = Ball(INITIAL_BALL_POSITION)
paddle = Paddle(INITIAL_PADDLE_POSITION)
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

is_game_on = True
while is_game_on:
    time.sleep(ball.get_speed())
    screen.update()
    ball.move()
    # Detect Collision with ceiling
    if ball.ycor() > VERTICAL_LIMIT:
        ball.bounce_y()
    # Detect Collision with side walls
    if ball.xcor() > HORIZONTAL_LIMIT+20 or ball.xcor() < -HORIZONTAL_LIMIT-20:
        ball.bounce_x()
    # Detect collision with paddle
    if ball.distance(paddle) < 45 and ball.ycor() < 290:
        ball.bounce_y()
    # Detect collision with brick
    for brick in bricks:
        if ball.distance(brick) < 30:
            brick.hideturtle()
            x_axis_difference = ball.xcor() - brick.xcor()
            y_axis_difference = ball.ycor() - brick.ycor()
            if abs(x_axis_difference) > abs(y_axis_difference):
                # If the ball ditches at the side of the brick then ball's x-axis will be switched.
                ball.bounce_x()
            else:
                # If the ball ditches on the top or bottom of the brick then ball's y-axis will be switched.
                ball.bounce_y()
            bricks.remove(brick)
            scoreboard.increase_score()
            if scoreboard.get_score() % 8 == 0:
                ball.increase_speed()
            break

    # Detect paddle miss
    if ball.ycor() < -VERTICAL_LIMIT:
        is_game_on = False
    if not bricks:
        is_game_on = False

update()
screen.exitonclick()
