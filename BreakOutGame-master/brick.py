from turtle import Turtle


class Brick(Turtle):
    """
        A class representing bricks in the game.
        Bricks are objects that the ball can collide with to break them.
    """
    def __init__(self, position):
        super().__init__()
        self.color("brown")
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=0.75)
        self.penup()
        self.goto(position)