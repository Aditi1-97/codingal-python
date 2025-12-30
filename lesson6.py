# importing the library
import turtle

sc = turtle.Screen()
# creating canvas
sc.bgcolor("Orange")
sc.setup(800, 600)
# turtle object creation
board = turtle.Turtle()
board.speed("slowest")

# creating a square
for i in range(4):
    board.forward(100)
    board.left(90)

# keep window open
turtle.done    