

import turtle
from main import game
from main2 import gameloop
from main4 import flappybird

wn = turtle.Screen()
wn.bgcolor("purple")
wn.title("PLAY GAME")

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("SELECT THE GAME", align="center", font=("Courier", 24, "normal"))


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300 , -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

pencil1 = turtle.Turtle()
pencil1.hideturtle()
pencil1.penup()
pencil1.goto(-50 , -5)
pencil1.fillcolor('yellow')
pencil1.begin_fill()
pencil1.forward(100)
pencil1.left(90)
pencil1.forward(35)
pencil1.left(90)
pencil1.forward(100)
pencil1.left(90)
pencil1.forward(35)
pencil1.left(90)
pencil1.end_fill()
pencil1.pendown()


pencil2 = turtle.Turtle()
pencil2.hideturtle()
pencil2.penup()
pencil2.goto(-50 , 75)
pencil2.fillcolor('yellow')
pencil2.begin_fill()
pencil2.forward(100)
pencil2.left(90)
pencil2.forward(35)
pencil2.left(90)
pencil2.forward(100)
pencil2.left(90)
pencil2.forward(35)
pencil2.left(90)
pencil2.end_fill()
pencil2.pendown()


pencil3 = turtle.Turtle()
pencil3.hideturtle()
pencil3.penup()
pencil3.goto(-80 , -85)
pencil3.fillcolor('yellow')
pencil3.begin_fill()
pencil3.forward(160)
pencil3.left(90)
pencil3.forward(35)
pencil3.left(90)
pencil3.forward(160)
pencil3.left(90)
pencil3.forward(35)
pencil3.left(90)
pencil3.end_fill()
pencil3.pendown()


pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.penup()
pen2.color("green")
pen2.goto(0 , 0)
pen2.write("SNAKE", align="center", font=("Courier", 24, "normal"))

pen3 = turtle.Turtle()
pen3.penup()
pen3.hideturtle()
pen3.color("blue")
pen3.goto(0 , 80)
pen3.write("PONG", align="center", font=("Courier", 24, "normal"))

pen4 = turtle.Turtle()
pen4.penup()
pen4.hideturtle()
pen4.color("red")
pen4.goto(0 , -80)
pen4.write("FLAPPY BIRD", align="center", font=("Courier", 24, "normal"))


def btnclick1(x , y) :
    if x>-30 and x<60 and y>-10 and y<30 :
        pen.clear()
        pen2.clear()
        pen3.clear()
        pen4.clear()
        pencil1.clear()
        pencil2.clear()
        pencil3.clear()
        game()
    elif x>-30 and x<60 and y>80 and y<130 :
        pen.clear()
        pen2.clear()
        pen3.clear()
        pen4.clear()
        pencil1.clear()
        pencil2.clear()
        pencil3.clear()
        gameloop()

    elif x>-30 and x<60 and y>-110 and y<-60 :
        pen.clear()
        pen2.clear()
        pen3.clear()
        pen4.clear()
        pencil1.clear()
        pencil2.clear()
        pencil3.clear()
        flappybird()

wn.onclick(btnclick1 , 1)
wn.listen()
turtle.done()


