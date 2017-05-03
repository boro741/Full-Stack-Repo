# 2. Draw Graphics using Classes & Objects



import turtle

#def draw_square(some_turtle):
#    for i in range(0,4):
#        some_turtle.forward(100)
#        some_turtle.right(90)

def draw_tri(some_tri):
    for i in range(0,3):
        some_tri.right(120)
        some_tri.forward(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("gray")

 #   brad = turtle.Turtle()
#    brad.shape("turtle")
#    brad.color("yellow")
#    for i in range(0,20):
#        draw_square(brad)
#        brad.right(18)

    angie = turtle.Turtle()
    angie.shape("circle")
    angie.color("blue")
    for i in range(0,20):
        angie.circle(40)
        angie.right(18)
        
    jul = turtle.Turtle()
    jul.shape("arrow")
    jul.color("white")
    
    for i in range(0,20):
        draw_tri(jul)
        jul.right(18)

    jul.forward(200)
    
    window.exitonclick()

draw_art()
