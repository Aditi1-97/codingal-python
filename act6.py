import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("beige")

t = turtle.Turtle()
t.speed("slowest")


def draw_triangle():
    t.color("black", "skyblue")
    t.begin_fill()
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()


def draw_rectangle():
    t.color("black", "lightgreen")
    t.begin_fill()
    for _ in range(2):
        t.forward(150)
        t.left(90)
        t.forward(80)
        t.left(90)
    t.end_fill()


def draw_hexagon():
    t.color("black", "navy blue")
    t.begin_fill()
    for _ in range(6):
        t.forward(80)
        t.left(60)
    t.end_fill()

# Draw triangle
draw_triangle()

# Move to new position
t.penup()
t.goto(-200, -150)
t.pendown()


draw_rectangle()

# Move to new position
t.penup()
t.goto(150, -150)
t.pendown()


draw_hexagon()

t.hideturtle()

turtle.done()
