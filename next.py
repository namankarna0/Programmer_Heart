import turtle
import math
import time

screen = turtle.Screen()
screen.bgcolor('black')
screen.title("❤️")

t = turtle.Turtle()
t.hideturtle()
t.width(2)
t.speed(1)

# Heart function (with control)
def heart(scale, color, show_text=False):
    t.color(color)
    t.begin_fill()

    for i in range(360):
        x = scale * 16 * math.sin(math.radians(i)) ** 3
        y = scale * (13 * math.cos(math.radians(i)) -
                     5 * math.cos(math.radians(2 * i)) -
                     2 * math.cos(math.radians(3 * i)) -
                     math.cos(math.radians(4 * i)))

        t.goto(x, y)

        # 🔥 Show text halfway through drawing
        if show_text and i == 180:
            t.penup()
            t.goto(0, -260)
            t.color("#ff4d6d")
            t.write("When you fall for a programmer",
                    align="center",
                    font=("Arial", 18   , "bold"))
            t.goto(x, y)
            t.pendown()

        time.sleep(0.002)

    t.end_fill()

# Start drawing
t.penup()
t.goto(0, 0)
t.pendown()

# Draw main heart and show text during drawing
heart(15, "#ff4d6d", show_text=True)

# Outline layers (faster)
for s in range(12, 9, -1):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    heart(s, "#330000")

turtle.done()
