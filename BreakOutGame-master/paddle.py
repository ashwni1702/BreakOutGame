from turtle import Turtle

HORIZONTAL_LIMIT = 720


class Paddle(Turtle):
    """
        A class representing the paddle in the game.
        The paddle is controlled by the player to bounce the ball and prevent it from falling.
    """
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("#EBBEAC")
        self.shapesize(stretch_len=6, stretch_wid=0.2)
        self.penup()
        self.goto(position)

    def move_left(self):
        """
        Move the paddle to the left.

        This method is called when the left arrow key is pressed.
        """
        if self.xcor() > -HORIZONTAL_LIMIT:
            new_x = self.xcor() - 40
            self.goto((new_x, self.ycor()))

    def move_right(self):
        """
           Move the paddle to the left.

           This method is called when the left arrow key is pressed.
        """
        if self.xcor() < HORIZONTAL_LIMIT:
            new_x = self.xcor() + 40
            self.goto((new_x, self.ycor()))