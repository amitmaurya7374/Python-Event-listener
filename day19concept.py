"""In this project will learn about Event Listener and Higher order function"""

from turtle import Turtle, Screen

jerry = Turtle()  # created an object
screen = Screen()  # created a screen Object


def move_forward():
    """Object move forward to 100"""
    jerry.forward(100)


def higher_order_function(num1, num2, func):
    """FUnction take another function as an input.\n
        In higher order function we only pass the name of another
        function without a paranthesis.
    """
    return func(num1, num2)


def add_number(num1, num2):
    """Adding a two numbers"""
    return num1 + num2


# calling a higher order function
result = higher_order_function(2, 3, add_number)
print(result)
"""This is a Event Listener Examples"""
screen.listen()  # this will start a listener
""" this method take which key has to listion and takes a function what happen when
this key is pressed.This is an Example of Higher Order Function.means function take another function as an input."""
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()  # This will hold a screen for us.
