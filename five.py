import turtle

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_spokes(x, y, radius, num_spokes):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("navy")
    angle = 360 / num_spokes
    for _ in range(num_spokes):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(radius)
        turtle.backward(radius)
        turtle.right(angle)

def draw_ashoka_chakra(x, y, radius):
    draw_circle("navy", x, y, radius)
    draw_circle("white", x, y, radius - 2)
    draw_spokes(x, y, radius, 24)

def draw_indian_flag():
    turtle.speed(5)
    
    # Drawing the orange rectangle
    draw_rectangle("orange", -150, 100, 300, 66.66)
    
    # Drawing the white rectangle
    draw_rectangle("white", -150, 33.33, 300, 66.66)
    
    # Drawing the green rectangle
    draw_rectangle("green", -150, -33.33, 300, 66.66)
    
    # Drawing the Ashoka Chakra
    draw_ashoka_chakra(0, 33.33, 20)

    # Hiding the turtle and completing the drawing
    turtle.hideturtle()
    turtle.done()

# Set up the screen
turtle.setup(500, 300)
draw_indian_flag()
