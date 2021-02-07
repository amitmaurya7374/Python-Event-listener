import turtle as turtle_module

"""Help you to draw a skecth using keyboards keys\n
       W : for move forward
       S: for backward
       A: for move counter_colckwise
       D:for move clockwise
    """
jerry_turtle = turtle_module.Turtle()
screen = turtle_module.Screen()
screen.listen()  # this will start listener


def move_forward():
    """Move 50 steps forward"""
    jerry_turtle.forward(50)


def move_backward():
    """Move 50 steps backwards"""
    jerry_turtle.back(50)


def move_counter_clockwise():
    """Move counter colckwise"""
    jerry_turtle.right(20)


def move_clockwise():
    """Move clockwise and forward"""
    jerry_turtle.forward(50)
    jerry_turtle.right(20)


def clear_screen():
    """This will clear a screen"""
    jerry_turtle.clear()
    jerry_turtle.penup()
    jerry_turtle.home()
    jerry_turtle.pendown()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
