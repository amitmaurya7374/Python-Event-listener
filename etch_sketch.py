"""This file will draw a etch a sketch"""
import turtle as turtle_module


class Sketch:
    """Help you to draw a skecth using keyboards keys\n
       W : for move forward
       S: for backward
       A: for move counter_colckwise
       D:for move clockwise
    """

    # Constructor
    # def __init__(self, key, fun):
    #     self.key = key
    #     self.func = fun

    jerry_turtle = turtle_module.Turtle()
    screen = turtle_module.Screen()
    screen.listen()  # this will start listener

    def move_forward(self):
        """Move 50 steps forward"""
        self.jerry_turtle.forward(50)

    def move_backward(self):
        """Move 50 steps backwards"""
        self.jerry_turtle.back(50)

    def move_counter_clockwise(self):
        """Move counter colckwise"""
        self.jerry_turtle.right(20)

    def move_clockwise(self):
        """Move clockwise and forward"""
        self.jerry_turtle.forward(50)
        self.jerry_turtle.right(20)

    screen.exitonclick()  # hold a screen for us
