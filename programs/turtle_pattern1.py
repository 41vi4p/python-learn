
import turtle
import time

def draw_square(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def draw_row(t, size, start_white=True):
    for i in range(8):
        color = "green" if (i + start_white) % 2 == 0 else "blue"
        draw_square(t, size, color)
        t.forward(size)

def draw_board(t, size):
    for i in range(8):
        # Position for each row
        t.penup()
        t.goto(-4*size, (3.5-i)*size)  # Center the board
        t.pendown()
        draw_row(t, size, start_white=(i % 2 == 0))


screen = turtle.Screen()
screen.title("Colour Pattern")
screen.bgcolor("black")
screen.setup(800, 800)

# Create and configure turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed is 0 
t.hideturtle()

# Draw the board
square_size = 50  # Size of each square
draw_board(t, square_size)

# Keep window open
screen.mainloop()