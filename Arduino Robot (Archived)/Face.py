import turtle
s = turtle.Screen()
t = turtle.Turtle()


s.setup(500, 500)
t.speed(0)



def eyes():
    eye_coordinate = -100
    size = 20
    t.fillcolor("DarkGreen")
    for x in range(0, 2):
        t.penup()
        t.goto(eye_coordinate, 50)
        t.pendown()
        t.begin_fill()

        for x in range(4):
            t.forward(size)  # Forward turtle by s units
            t.left(90)  # Turn turtle by 90 degree
        eye_coordinate = eye_coordinate + 200
        print(eye_coordinate)
        t.end_fill()
        t.penup()


while True:
    t.clear()
    eyes()
    eye_coordinate = eye_coordinate + 10

eyes()
turtle.Screen().exitonclick()