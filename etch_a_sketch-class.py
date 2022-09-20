import turtle
from turtle import Turtle, Screen


class Game(Turtle):

    def __init__(self, up, down, lft, rght):
        super().__init__()
        self.up = str(up)
        self.down = str(down)
        self.lft = str(lft)
        self.rght = str(rght)

    def frwrd(self):
        self.forward(10)

    def bkwrd(self):
        self.backward(10)

    def l(self):
        new_heading = self.heading() + 10
        self.setheading(new_heading)

    def r(self):
        new_heading = self.heading() - 10
        self.setheading(new_heading)

    def c(self):
        self.clear()
        self.penup()
        self.home()
        self.pendown()

    def ready(self):
        screen = Screen()
        screen.listen()
        screen.onkeypress(self.frwrd, self.up)
        screen.onkeypress(self.bkwrd, self.down)
        screen.onkeypress(self.l, self.lft)
        screen.onkeypress(self.r, self.rght)
        screen.onkeypress(self.c, "c")

