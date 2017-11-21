'''
This part of the program is called the program docstring. Any file you hand in
should start with a docstring. The docstring should describe the program and
also contain key information about who you are and when it was done.
 
# Name: Shahir Taj
# Section: A
# Date: 09/29/2017
 
This program draws a picture of a starry night using turtle graphics.
'''

import turtle

HEXAGRAM_EXTERNAL_ANGLE = 120 # external angle of a hexagon
HEXAGRAM_INTERNAL_ANGLE = -60 # internal angle of a hexagon
PENTAGON_INTERNAL_ANGLE = 72 # interal angle of a pentagon
TRIANGLE_INTERNAL_ANGLE_SUM = 180 # sum of internal angles of a triangle
CIRCLE_CURVE = 6 # curve of a circle
RECTANGLE_INTERNAL_ANGLE = 90 # internal angle of a rectangle

def starry_night():
    '''With apologies to Van Gogh - draws a picture of a starry night
    using turtle graphics'''
    
    # Clear the screen
    turtle.clear()

    # Create 3 green stars in the shape of hexagrams
    draw_hexagram('green', 50, 150, 0, 5)
    draw_hexagram('green', -170, 20, 230, 5)
    draw_hexagram('green', 150, -50, -205, 5)    

    # Create 3 green stars in the shape of pentagons
    draw_pentagon('green', -230, -40, -10, 8)
    draw_pentagon('green', 50, 60, -10, 8)
    draw_pentagon('green', 230, 30, -70, 8)    

    # Create 2 magenta 6-point stars
    draw_hexagram('magenta', -30, -40, 15, 5)
    draw_hexagram('magenta', 110, 20, 40, 5)    

    # Create 3 magenta stars in the shape of pentagons
    draw_pentagon('magenta', -80, 80, 10, 8)
    draw_pentagon('magenta', 250, 120, 10, 8)
    draw_pentagon('magenta', -320, 0, 10, 8)    

    # Create 3 blue stars in the shape of triangles
    draw_triangle('blue', -160, 130, -90, 10, 10, 10, 60, 60)
    draw_triangle('blue', -50, 10, 0, 10, 10, 10, 60, 60)
    draw_triangle('blue', 180, 90, 90, 10, 10, 10, 60, 60)    

    # You can stop here. You don't need to remove anymore code if you don't
    # want to.

    # Create gray moon
    draw_circle('gray', -300, 100, 0, 5) 

    # Create 3-layer red brick wall at the bottom of the screen


    # Top layer

    # Move to left side of screen at the height of a 3-layer wall made of
    # 60 x 24 unit bricks with 6 unit brick spacing (479 - 3*24 - 2*6 = 395)
    draw_rectangle('red', -350, -195, 0, 60, 24)
    draw_rectangle('red', -284, -195, 0, 60, 24)
    draw_rectangle('red', -218, -195, 0, 60, 24)
    draw_rectangle('red', -152, -195, 0, 60, 24)
    draw_rectangle('red', -86, -195, 0, 60, 24)
    draw_rectangle('red', -20, -195, 0, 60, 24)
    draw_rectangle('red', 46, -195, 0, 60, 24)
    draw_rectangle('red', 112, -195, 0, 60, 24)
    draw_rectangle('red', 178, -195, 0, 60, 24)
    draw_rectangle('red', 244, -195, 0, 45, 24) # partial brick


    # Second layer

    # Move to left side of screen at the height of the second layer of bricks
    # (395 + 24 + 6 = 425)
    draw_rectangle('red', -350, -225, 0, 27, 24) # top side of length brick
    draw_rectangle('red', -317, -225, 0, 60, 24) # width/2 - brick spacing/2 =
    draw_rectangle('red', -251, -225, 0, 60, 24) # 30 - 3 = 27
    draw_rectangle('red', -185, -225, 0, 60, 24)
    draw_rectangle('red', -119, -225, 0, 60, 24)
    draw_rectangle('red', -53, -225, 0, 60, 24)
    draw_rectangle('red', 13, -225, 0, 60, 24)
    draw_rectangle('red', 79, -225, 0, 60, 24)
    draw_rectangle('red', 145, -225, 0, 60, 24)
    draw_rectangle('red', 211, -225, 0, 60, 24)
    draw_rectangle('red', 277, -225, 0, 12, 24) # partial brick

    # Bottom layer

    # Move to left side of screen at the height of the bottom layer of bricks
    # (425 + 24 + 6 = 455)
    draw_rectangle('red', -350, -255, 0, 60, 24)
    draw_rectangle('red', -284, -255, 0, 60, 24)
    draw_rectangle('red', -218, -255, 0, 60, 24)
    draw_rectangle('red', -152, -255, 0, 60, 24)
    draw_rectangle('red', -86, -255, 0, 60, 24)
    draw_rectangle('red', -20, -255, 0, 60, 24)
    draw_rectangle('red', 46, -255, 0, 60, 24)
    draw_rectangle('red', 112, -255, 0, 60, 24)
    draw_rectangle('red', 178, -255, 0, 60, 24)
    draw_rectangle('red', 244, -255, 0, 45, 24) # partial brick

    # remove turtle from final picture
    turtle.hideturtle()
    
    # end of starry_night function definition
    
def custom_picture():
    """Draws a picture of a fish using turtle graphics."""
    
    # Clear the screen
    turtle.clear()
    
    # Create fish fins
    turtle.begin_fill() # top fin
    draw_triangle('red', -100, 57.243, 50, 93.343, 71.505, 60, 40, 90)
    turtle.end_fill()    
    turtle.begin_fill() # bottom fin
    draw_triangle('red', -100, -57.243, 0, 60, 71.505, 93.343, 90, 40)
    turtle.end_fill()      
    
    # Create fish body
    turtle.begin_fill() # left half
    draw_semicircle('cyan', -100, -95.405, -180, 10)
    turtle.end_fill()    
    turtle.begin_fill() # right half
    draw_semicircle('purple', -100, 95.405, 0, 10)
    turtle.end_fill()
        
    # Create fish eye
    turtle.begin_fill()
    draw_circle('white', -175, 19.08, 0, 2) # sclera
    turtle.end_fill()
    turtle.begin_fill()
    draw_circle('purple', -175, 7.155, 0, 0.75) # iris
    turtle.end_fill()    
    turtle.begin_fill()
    draw_circle('red', -175, 4.77, 0, 0.5) # pupil
    turtle.end_fill()
    
    # Create fish scales
    
    
    # First layer   
    turtle.begin_fill()
    draw_triangle('green', -100, 95.05, -30, 38.162, 38.162, 38.162, 60, 60)
    turtle.end_fill()
    turtle.begin_fill()
    draw_triangle('green', -100, 57.243, -30, 38.162, 38.162, 38.162, 60, 60)
    turtle.end_fill()
    turtle.begin_fill()
    draw_triangle('green', -100, 19.081, -30, 38.162, 38.162, 38.162, 60, 60)
    turtle.end_fill()
    turtle.begin_fill()
    draw_triangle('green', -100, -19.081, -30, 38.162, 38.162, 38.162, 60, 60)
    turtle.end_fill()
    turtle.begin_fill()
    draw_triangle('green', -100, -57.243, -30, 38.162, 38.162, 38.162, 60, 60)
    turtle.end_fill()
    
    # Second layer
    turtle.begin_fill()
    draw_triangle('green', -66.951, 75.969, -30, 38.162, 38.162, 38.162, 60, 60)
    turtle.end_fill()
    turtle.begin_fill()
    draw_triangle('green', -66.951, 37.807, -30, 38.162, 38.162, 38.162, 60, 60)
    turtle.end_fill()
    turtle.begin_fill()
    draw_triangle('green', -66.951, -0.355, -30, 38.162, 38.162, 38.162, 60, 60)
    turtle.end_fill()
    turtle.begin_fill()
    draw_triangle('green', -66.951, -38.517, -30, 38.162, 38.162, 38.162, 60, 
                  60)
    turtle.end_fill()
    
    #Third Layer
    turtle.begin_fill()
    draw_triangle('green', -33.902, 56.888, -36, 31.541, 31.541, 38.162, 74.452, 
                  52.774)
    turtle.end_fill()
    turtle.begin_fill()
    draw_triangle('green', -33.902, 18.726, -30, 38.162, 38.162, 38.162, 60, 60)
    turtle.end_fill()
    turtle.begin_fill()
    draw_triangle('green', -33.902, -19.4, -36, 31.541, 31.541, 38.162, 74.452, 
                  52.774)
    turtle.end_fill()  
    
    # Create fish tail
    turtle.begin_fill()
    draw_triangle('red', 0, 0, 19.471, 225, 150, 225, 70.529, 70.529)
    turtle.end_fill()
 
    # remove turtle from final picture
    turtle.hideturtle()
    
    # end of custom_picture function definition
    
def draw_hexagram(color, x_coord, y_coord, theta, side_length):
    """ (string, int/float, int/float, int/float, int/float) -> hexagram
    
    Draw hexagram in specified color at (x_coord, y_coord) with an angle of 
    inclination theta and side lengths side_length.
    
    Precondition: side_length > 0
    
    >>> draw_hexagram('red', 30.5, 50, 90, 10)
    >>> draw_hexagram('blue', -50, 100, -60.7, 25)
    >>> draw_hexagram('green', -125, -200, 45, 5.9)
    """
    
    # Move to new location without showing trail, set orientation and move to
    # top of hexgram then show trail again    
    turtle.color(color)
    turtle.up()
    turtle.goto(x_coord, y_coord)
    turtle.setheading(theta)
    turtle.down()

    turtle.right(HEXAGRAM_EXTERNAL_ANGLE) # right half of top point
    turtle.forward(side_length)
    turtle.right(HEXAGRAM_INTERNAL_ANGLE)  # top right point
    turtle.forward(side_length)
    turtle.right(HEXAGRAM_EXTERNAL_ANGLE)
    turtle.forward(side_length)
    turtle.right(HEXAGRAM_INTERNAL_ANGLE)  # bottom right point
    turtle.forward(side_length)
    turtle.right(HEXAGRAM_EXTERNAL_ANGLE)
    turtle.forward(side_length)
    turtle.right(HEXAGRAM_INTERNAL_ANGLE)  # bottom point
    turtle.forward(side_length)
    turtle.right(HEXAGRAM_EXTERNAL_ANGLE)
    turtle.forward(side_length)
    turtle.right(HEXAGRAM_INTERNAL_ANGLE)  # bottom left point
    turtle.forward(side_length)
    turtle.right(HEXAGRAM_EXTERNAL_ANGLE)
    turtle.forward(side_length)
    turtle.right(HEXAGRAM_INTERNAL_ANGLE)  # top left point
    turtle.forward(side_length)
    turtle.right(HEXAGRAM_EXTERNAL_ANGLE)
    turtle.forward(side_length)
    turtle.right(HEXAGRAM_INTERNAL_ANGLE)  # left half of top point
    turtle.forward(side_length)
    
    # end of draw_hexagram function definition    
    
def draw_pentagon(color, x_coord, y_coord, theta, side_length):
    """ (string, int/float, int/float, int/float, int/float) -> pentagon
    
    Draw pentagon in specified color at (x_coord, y_coord) with an angle of 
    inclination theta and side lengths side_length.
    
    Precondition: side_length > 0
    
    >>> draw_pentagon('gray', -60, 100, 180, 18.8)
    >>> draw_pentagon('magenta', 75, -10, 0.6, 10)
    >>> draw_pentagon('yellow', 200, 200.3, -100, 25)
    """
    
    # Move to new location without showing trail, set orientation and move to
    # top of pentagon then show trail again   
    turtle.color(color)
    turtle.up()
    turtle.goto(x_coord, y_coord)
    turtle.setheading(theta)
    turtle.down()

    turtle.right(PENTAGON_INTERNAL_ANGLE) # top left side
    turtle.forward(side_length)
    turtle.right(PENTAGON_INTERNAL_ANGLE) # top right side
    turtle.forward(side_length)
    turtle.right(PENTAGON_INTERNAL_ANGLE) # bottom right side
    turtle.forward(side_length)
    turtle.right(PENTAGON_INTERNAL_ANGLE) # bottom side
    turtle.forward(side_length)
    turtle.right(PENTAGON_INTERNAL_ANGLE) # bottom left side
    turtle.forward(side_length)
    
    # end of draw_pentagon function definition
    
def draw_triangle(color, x_coord, y_coord, theta, side1_length, side2_length, 
                  side3_length, angle12, angle23):
    """ (string, int/float, int/float, int/float, int/float, int/float, 
    int/float, int/float, int/float) -> triangle
    
    Draw triangle in specified color at (x_coord, y_coord), with an angle of 
    inclination theta, side lengths side1_length, side2_length and
    side3_length and interior angles angle12, angle23, and 180 - (angle12 + 
    angle23).
    
    Preconditions: sidex_length > 0 and anglexy > 0
    
    >>> draw_triangle('blue', -60.7, 50, 75, 5, 5, 5, 60, 60)
    >>> draw_triangle('magenta', 50, 100, -20, 5.4, 4, 5.4, 68.2, 68.2)
    >>> draw_triangle('green', -125, -200, 45, 12.586, 15, 19.581, 90, 40)
    """
    
    # Move to new location without showing trail, set orientation and move to
    # top of triangle then show trail again    
    turtle.color(color)
    turtle.up()
    turtle.goto(x_coord, y_coord)
    turtle.setheading(theta)
    turtle.down()
    
    turtle.forward(side1_length)  # side one
    turtle.right(TRIANGLE_INTERNAL_ANGLE_SUM - angle12)
    turtle.forward(side2_length)  # side two
    turtle.right(TRIANGLE_INTERNAL_ANGLE_SUM - angle23)
    turtle.forward(side3_length) # side three
    
    # end of draw_triangle function definition

def draw_circle(color, x_coord, y_coord, theta, edge):
    """ (string, int/float, int/float, int/float, int/float) -> circle
    
    Draw circle in specified color at (x_coord, y_coord) with an angle of 
    inclination theta and edge lengths edge.
    
    Precondition: edge > 0
    
    >>> draw_circle('gray', -60, 100, 180, 18.8)
    >>> draw_circle('magenta', 75, -10, 0.6, 10)
    >>> draw_circle('yellow', 200, 200.3, -100, 25)
    """   
    
    # Move to new location without showing trail, set orientation then show 
    # trail again    
    turtle.color(color)
    turtle.up()
    turtle.goto(x_coord, y_coord)
    turtle.setheading(theta)
    turtle.down()
    
    # Repeatedly draw a fixed-length short line and turn a fixed small angle,
    # until the figure looks approximately like a circle.
    for count in range(60):
        turtle.forward(edge)
        turtle.right(CIRCLE_CURVE)
        
    # end of draw_circle function definition
    
def draw_rectangle(color, x_coord, y_coord, theta, side1_length, side2_length):
    """ (string, int/float, int/float, int/float, int/float, int2/float) -> 
    rectangle
    
    Draw rectangle in specified color at (x_coord, y_coord) with an angle of 
    inclination theta and side lengths side1_length and side2_length.
    
    Precondition: sidex_length > 0
    
    >>> draw_rectangle('purple', 25, 200, -180, 18.8, 12.2)
    >>> draw_rectangle('red', 23, -15, 10, 10)
    >>> draw_rectangle('white', 200, 191.3, -100, 25, 68)
    """
    
    # Move to new location without showing trail, set orientation and move to
    # top of rectangle then show trail again      
    turtle.color(color)
    turtle.up()
    turtle.goto(x_coord, y_coord)
    turtle.setheading(theta)
    turtle.down()

    turtle.forward(side1_length)  # top side
    turtle.right(RECTANGLE_INTERNAL_ANGLE)
    turtle.forward(side2_length)  # right side
    turtle.right(RECTANGLE_INTERNAL_ANGLE)
    turtle.forward(side1_length)  # bottom side
    turtle.right(RECTANGLE_INTERNAL_ANGLE)
    turtle.forward(side2_length)  # left side
    turtle.right(RECTANGLE_INTERNAL_ANGLE)
    
     # end of draw_rectangle function definition
    
def draw_semicircle(color, x_coord, y_coord, theta, edge):
    """ (string, int/float, int/float, int/float, int/float) -> semicircle
    
    Draw semicircle in specified color at (x_coord, y_coord) with an angle of 
    inclination theta and edge lengths edge.
    
    Precondition: edge > 0
    
    >>> draw_semicircle('gray', -60, 100, 180, 18.8)
    >>> draw_semicircle('magenta', 75, -10, 0.6, 10)
    >>> draw_semicircle('yellow', 200, 200.3, -100, 25)
    """
    
    # Move to new location without showing trail, set orientation then show 
    # trail again    
    turtle.color(color)
    turtle.up()
    turtle.goto(x_coord, y_coord)
    turtle.setheading(theta)
    turtle.down()
    
    # Repeatedly draw a fixed-length short line and turn a fixed small angle,
    # until the figure looks approximately like a semicircle.    
    for count in range(31):
        turtle.forward(edge)
        turtle.right(CIRCLE_CURVE)
    turtle.goto(x_coord, y_coord) # connects the two ends of the arc
    
    # end of draw_semicircle function definition
    