import turtle

# Set up the canvas / screen
screen = turtle.Screen()
screen.title("Square on Canvas")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Create a turtle to draw
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("black")
pen.speed(3)

# Draw a square
side_length = 100
for _ in range(4):
    pen.forward(side_length)
    pen.right(90)

# Keep the canvas window open until closed by user
turtle.done()

