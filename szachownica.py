import turtle

turtle.speed(999)
for i in range(8):
    for i in range(8):
        for i in range(4):
            turtle.forward(30)
            turtle.left(90)
            turtle.end_fill()
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
    turtle.penup()
    turtle.left(180)
    turtle.forward(30 * 8)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.down()
turtle.penup()
turtle.right(-90)
turtle.forward(60)
turtle.pendown()
for i in range(4):
    for i in range(4):
        turtle.fillcolor('black')
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(30)
            turtle.right(90)
        turtle.penup()
        turtle.forward(60)
        turtle.pendown()
        turtle.end_fill()
    turtle.penup()
    turtle.left(180)
    turtle.forward(30 * 8)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.down()

turtle.penup()
turtle.left(180)
turtle.forward(30)
turtle.right(90)

turtle.pendown()

for i in range(4):
    for i in range(4):
        turtle.fillcolor('black')
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(30)
            turtle.right(90)
        turtle.penup()
        turtle.forward(60)
        turtle.pendown()
        turtle.end_fill()
    turtle.penup()
    turtle.left(180)
    turtle.forward(30 * 8)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.down()
turtle.pendown()


turtle.mainloop()





