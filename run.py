# Built in turtle module lets you do basic graphics
import turtle

# Create a window
wn = turtle.Screen()
wn.title("Pong by Erin")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# Tracer stops the window from updating
wn.tracer(0)

# Paddle A
# Assigning paddle_a a turtle object
paddle_a = turtle.Turtle()
# Paddle animation speed set to maximum possible speed otherwise things would be too slow
paddle_a.speed(0)
# Built in shape chose square
paddle_a.shape("square")
paddle_a.color("white")
# Turtles by definition draw a line as they are moving, we dont need to draw lines
paddle_a.penup()
# I want the paddle to start at minus 350 as an x coordinate and 0 vertically centred in the screen
paddle_a.goto(-350, 0)


# Paddle B


# Ball


# Main game loop
while True:
    # Every time the loop runs it updates the screen
    wn.update()
