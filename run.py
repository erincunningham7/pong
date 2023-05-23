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
# By default the paddle shape is 20x20 pixels, stretch the shape using the shapesize method
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# Turtles by definition draw a line as they are moving, we dont need to draw lines
paddle_a.penup()
# I want the paddle to start at minus 350 as an x coordinate and 0 vertically centred in the screen
paddle_a.goto(-350, 0)


# Paddle B
# Assigning paddle_b a turtle object
paddle_b = turtle.Turtle()
# Paddle animation speed set to maximum possible speed otherwise things would be too slow
paddle_b.speed(0)
# Built in shape chose square
paddle_b.shape("square")
paddle_b.color("white")
# By default the paddle shape is 20x20 pixels, stretch the shape using the shapesize method
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
# Turtles by definition draw a line as they are moving, we dont need to draw lines
paddle_b.penup()
# I want the paddle to start at plus 350 as an x coordinate and 0 vertically centred in the screen, opposite of paddle a
paddle_b.goto(+350, 0)


# Ball
# Assigning ball a turtle object
ball = turtle.Turtle()
# Paddle animation speed set to maximum possible speed otherwise things would be too slow
ball.speed(0)
# Built in shape chose square
ball.shape("square")
ball.color("white")
# Turtles by definition draw a line as they are moving, we dont need to draw lines
ball.penup()
# Ball needs to start in middle of the screen
ball.goto(0, 0)

# Main game loop
while True:
    # Every time the loop runs it updates the screen
    wn.update()
