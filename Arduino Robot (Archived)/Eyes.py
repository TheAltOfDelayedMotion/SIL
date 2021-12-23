import turtle
t = turtle.Turtle()
s = 20

eye_coordinate = -50

t.speed('fastest')
t.fillcolor("DarkGreen")

for x in range(0, 2):
    t.penup()
    t.goto (eye_coordinate,50)
    t.pendown()
    t.begin_fill()
    for x in range(4):
        t.forward(s)  # Forward turtle by s units
        t.left(90)  # Turn turtle by 90 degree
    eye_coordinate = eye_coordinate + 100
    print(eye_coordinate)
    t.end_fill()
    t.penup()

turtle.Screen().exitonclick()


