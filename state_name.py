from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class State_Name(Turtle):

    def __init__(self, state, coordinates):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.speed(0)
        self.goto(coordinates)
        self.write(f"{state}", align=ALIGNMENT, font=FONT)
