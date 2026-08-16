import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("❤️")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
screen.tracer(0)
t.width(2)


def heart(scale, color):
    t.color(color)
    t.begin_fill()

    for i in range(360):
        x = scale * 16 * math.sin(math.radians(i)) ** 3

        y = scale * (
            13 * math.cos(math.radians(i))
            - 5 * math.cos(math.radians(2 * i))
            - 2 * math.cos(math.radians(3 * i))
            - math.cos(math.radians(4 * i))
        )

        t.goto(x, y)

    t.end_fill()

    t.penup()
    t.goto(0, -10)
    t.pendown()


# Main heart
heart(15, "#ff4d6d")


# Dark outline layers
for s in range(18, 13, -1):
    t.penup()
    t.goto(0, -10)
    t.pendown()

    t.width(2)
    heart(s, "#330000")


# Inner heart
t.penup()
t.goto(0, -10)
t.pendown()

t.width(2)
heart(14, "#ff6a8a")


# Text
t.penup()
t.goto(0, -170)
t.color("#ff4d6d")

t.write(
    "When you fall for a programmer",
    align="center",
    font=("Arial", 24, "bold")
)

screen.update()

turtle.done()