from turtle import Turtle


class Ball(Turtle):
    """
        A class representing the ball in the game.
        The ball moves around the screen and interacts with bricks and the paddle.
    """
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("#7CFC00")
        self.penup()
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.05

    def move(self):
        """
        :return: Moves the ball to new positions
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def bounce_x(self):
        """
            Bounce the ball along the x-axis.

            This method changes the direction of the ball's movement horizontally.
        """
        self.x_move *= -1

    def bounce_y(self):
        """
            Bounce the ball along the y-axis.

            This method changes the direction of the ball's movement vertically.
        """
        self.y_move *= -1

    def increase_speed(self):
        """
            Increase the speed of the ball.

            This method increases the ball's movement speed.
        """
        self.speed *= 0.9

    def get_speed(self):
        return self.speed
