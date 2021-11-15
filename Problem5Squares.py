# Leslie Bacajol
# 11/10/21
# Problem 5
# This programs produces an image of a square with more squares inside

import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

size = 20

for i in range(5):
    drawSquare(alex, size)
    size = size + 20
    alex.penup()
    alex.goto(alex.pos() + (-10, -10))
    alex.pendown()

wn.exitonclick()
