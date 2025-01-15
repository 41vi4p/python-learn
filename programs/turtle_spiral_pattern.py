import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Colorful Spiral Pattern")
screen.bgcolor("black")
screen.setup(800, 800)

# Create and configure turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.pensize(2)
t.hideturtle()

# Color list for gradient effect
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def colourChange():
    colors2 = random.choice(colors)
    print(colors2)
    return colors2

# Draw spiral
for i in range(360):
    # Change color
    t.pencolor(colourChange())
    
    # Move forward with increasing distance
    t.forward(i)
    
    # Turn right by 30 degrees
    t.right(30)
    
    # Add slight curve to create spiral
    t.right(1)

# Keep window open
screen.mainloop()