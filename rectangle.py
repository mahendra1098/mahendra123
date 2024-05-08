import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(0)

# Define the colors
colors = ["blue", "black", "red"]

# Fill the rectangle with colors
t.begin_fill()

# Draw the rectangle
for i in range(2):
    t.color(colors[i % 3])  # Cycling through the colors
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)

# End the filling
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.mainloop()