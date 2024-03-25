import turtle

# Create a turtle object
t = turtle.Turtle()

# Write some text with default font
t.write("Hello, world!")

# Write text with a specific font
t.write("This is bold text!", font=("Arial", 30, "bold"))

# Write centered text
t.penup()  # Lift the pen to avoid drawing a line before writing
t.goto(0, 100)  # Move the turtle to a new position
t.pendown()  # Put the pen down to start drawing again
t.write("Centered text", align="center")

# Write text without moving the turtle
t.write("Text stays here", move=False)

# Keep the window open until closed manually
turtle.done()