import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Triple Turtle Animation")

# Create turtles
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

# Configure turtles
for t in [t1, t2, t3]:
    t.speed(0)
    t.pensize(2)
    t.hideturtle()

# Colors
t1.color("cyan")
t2.color("magenta")
t3.color("yellow")

# First turtle - Rotating hexagons
def draw_hexagon(t, size):
    for _ in range(6):
        t.forward(size)
        t.right(60)

# Second turtle - Spiral pattern
def draw_spiral(t, size):
    for i in range(size):
        t.forward(i * 2)
        t.right(45)

# Third turtle - Flower pattern
def draw_flower(t, size):
    for _ in range(36):
        for _ in range(4):
            t.forward(size)
            t.right(90)
        t.right(10)

# Position turtles
t1.penup()
t1.goto(-150, 0)
t1.pendown()

t2.penup()
t2.goto(150, 0)
t2.pendown()

t3.penup()
t3.goto(0, -150)
t3.pendown()

# Draw patterns
for i in range(36):
    t1.begin_fill()
    draw_hexagon(t1, 50)
    t1.end_fill()
    t1.right(10)
    
    draw_spiral(t2, 10)
    t2.right(10)
    
    draw_flower(t3, 40)
    t3.right(10)

# Keep window open
screen.mainloop()