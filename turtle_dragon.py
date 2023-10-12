import turtle

def draw_dragon():
    # Set up the turtle
    t = turtle.Turtle()
    t = 0
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-100, 0)
    t.pendown()

    # Draw the Drexel "D"
    t.pensize(10)
    t.color("blue")
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)

    # Draw the dragon head
    t.penup()
    t.goto(50, 50)
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    # Draw the dragon eyes
    t.penup()
    t.goto(30, 70)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.goto(70, 70)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Draw the dragon nostrils
    t.penup()
    t.goto(50, 50)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()
    t.goto(60, 50)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    # Draw the dragon mouth
    t.penup()
    t.goto(30, 30)
    t.pendown()
    t.color("red")
    t.pensize(5)
    t.right(45)
    t.forward(30)
    t.right(90)
    t.forward(30)

    # Write the text "DREXEL" next to the dragon
    t.penup()
    t.goto(150, 50)
    t.pendown()
    t.color("black")
    t.write("DREXEL", font=("Arial", 36, "bold"))

    # Hide the turtle
    t.hideturtle()

# Call the function to draw the Drexel Dragon
draw_dragon()
