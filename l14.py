# ==========================================
# Activity 1: Draw a Hexagon Using Turtle
# Objective: Draw a hexagon using the Turtle graphics library.
# ==========================================

import turtle

screen = turtle.Screen()
screen.bgcolor("orange")
screen.setup(600, 600)

shape = turtle.Turtle()
shape.speed(3)

num_sides = 6
side_length = 70
angle = 360 / num_sides

for i in range(num_sides):
    shape.forward(side_length)
    shape.right(angle)

shape.clear()


# ==========================================
# Activity 2: Draw a Star Using Turtle
# Objective: Draw a star shape using the Turtle graphics library.
# ==========================================

for i in range(5):
    shape.forward(150)
    shape.right(144)

shape.clear()


# ==========================================
# Activity 3: Draw a Spiral Pattern Using Turtle
# Objective: Draw a spiral pattern using the Turtle graphics library.
# ==========================================

shape.speed(0)

for i in range(100):
    shape.forward(i * 5)
    shape.right(91)

turtle.done()