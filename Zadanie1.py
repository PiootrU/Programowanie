import turtle

def Wpisz():
    l = input("Podaj wielkość szachownicy. Pamiętając o tym że podana liczba musi być parzysta i stworzy tablice  N x N Liczba:")
    l = int(l)
    n = l*1/2
    n = int(n)
    reszta = l % 2
    if reszta == 1:
        print("Wpisałeś nieparzystą liczbe, spróbuj jeszcze raz")
        return Wpisz()
    else:
        turtle.speed(900)
        if reszta == 0:
            for i in range(l):
                for i in range(l):
                    turtle.fillcolor('blue')
                    turtle.begin_fill()
                    for i in range(4):
                        turtle.forward(30)
                        turtle.left(90)
                    turtle.end_fill()
                    turtle.penup()
                    turtle.forward(30)
                    turtle.pendown()
                    turtle.end_fill()
                turtle.penup()
                turtle.left(180)
                turtle.forward(30 * l)
                turtle.left(90)
                turtle.forward(30)
                turtle.left(90)
                turtle.down()
            turtle.penup()
            turtle.right(-90)
            turtle.forward(60)
            turtle.pendown()
            for i in range(n):
                for i in range(n):
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
                turtle.forward(30 * l)
                turtle.left(90)
                turtle.forward(60)
                turtle.left(90)
                turtle.down()

            turtle.penup()
            turtle.left(180)
            turtle.forward(30)
            turtle.right(90)

            turtle.pendown()

            for i in range(n):
                for i in range(n):
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
                turtle.forward(30 * l)
                turtle.left(90)
                turtle.forward(60)
                turtle.left(90)
                turtle.down()
            turtle.pendown()
        else:
            print("Wpisałeś nieparzystą liczbe, Spróbuj jeszcze raz")

        turtle.mainloop()

Wpisz()
