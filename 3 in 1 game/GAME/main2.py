import turtle
import time

def gameloop():
    win = turtle.Screen()
    win.setup(800, 600)
    win.title('Pong Python 3 and Turtle using classes')
    win.bgcolor('green')
    win.tracer(0)  # Stops animation until win.update()
    win.listen()  # Listen to keypresses

    class Paddle(turtle.Turtle):
        def __init__(self, xpos):  # xpos will tell if paddle should be left -350 or right 350
            super().__init__(shape='square')
            self.up()
            self.shapesize(5, 1)
            self.color('yellow')
            self.xpos = xpos
            self.goto(xpos, 0)

        def move_up(self):
            if self.ycor() < 250:
                self.goto(self.xcor(), self.ycor() + 30)

        def move_down(self):
            if self.ycor() > -250:
                self.goto(self.xcor(), self.ycor() - 30)

    class Ball1(turtle.Turtle):
        def __init__(self, paddle1, paddle2):
            super().__init__(shape='circle')
            self.up()
            self.color('blue')
            self.dx, self.dy = 2.75, -2.75
            self.paddle1 = paddle1
            self.paddle2 = paddle2

        def move(self):
            self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

            # Score player 2
            if self.xcor() < -395:
                ##self.goto(0, 0)
                self.dx *= -1

            # Score player 1
            if self.xcor() > 395:
                ##self.goto(0, 0)
                self.dx *= -1

            # Boundary check
            if self.ycor() < -280 or self.ycor() > 280:
                self.dy *= -1

        def bounce_paddle(self):

            # Paddle2
            if self.xcor() + 10 >= 340 and self.xcor() + 10 <= 350 and self.dx > 0:
                if self.ycor() + 10 >= self.paddle2.ycor() - 50 and self.ycor() - 10 <= self.paddle2.ycor() + 50:
                    self.dx *= -1

            # Paddle1 - ball towards paddle (dx negative or < 0),
            # between left (xcor()+10) side and middle (xcor()) of paddle,
            # between top (ycor()+50) and bottom (ycor()-50)
            if self.xcor() - 10 <= paddle1.xcor() + 10 and self.xcor() - 10 >= paddle1.xcor() and self.dx < 0:
                if self.ycor() + 10 >= self.paddle1.ycor() - 50 and self.ycor() - 10 <= self.paddle1.ycor() + 50:
                    self.dx *= -1

    class Ball2(turtle.Turtle):
        def __init__(self, paddle1, paddle2):
            super().__init__(shape='circle')
            self.up()
            self.color('red')
            self.dx, self.dy = -3.5, 3.5
            self.paddle1 = paddle1
            self.paddle2 = paddle2

        def move(self):
            self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

            # Score player 2
            if self.xcor() < -395:
                ##self.goto(0, 0)
                self.dx *= -1

            # Score player 1
            if self.xcor() > 395:
                ##self.goto(0, 0)
                self.dx *= -1

            # Boundary check
            if self.ycor() < -280 or self.ycor() > 280:
                self.dy *= -1

        def bounce_paddle(self):

            # Paddle2
            if self.xcor() + 10 >= 340 and self.xcor() + 10 <= 350 and self.dx > 0:
                if self.ycor() + 10 >= self.paddle2.ycor() - 50 and self.ycor() - 10 <= self.paddle2.ycor() + 50:
                    self.dx *= -1

            # Paddle1 - ball towards paddle (dx negative or < 0),
            # between left (xcor()+10) side and middle (xcor()) of paddle,
            # between top (ycor()+50) and bottom (ycor()-50)
            if self.xcor() - 10 <= paddle1.xcor() + 10 and self.xcor() - 10 >= paddle1.xcor() and self.dx < 0:
                if self.ycor() + 10 >= self.paddle1.ycor() - 50 and self.ycor() - 10 <= self.paddle1.ycor() + 50:
                    self.dx *= -1

    class Ball3(turtle.Turtle):
        def __init__(self, paddle1, paddle2):
            super().__init__(shape='circle')
            self.up()
            self.color('white')
            self.dx, self.dy = -3.15, -3.15
            self.paddle1 = paddle1
            self.paddle2 = paddle2

        def move(self):
            self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

            # Score player 2
            if self.xcor() < -395:
                ##self.goto(0, 0)
                self.dx *= -1

            # Score player 1
            if self.xcor() > 395:
                ##self.goto(0, 0)
                self.dx *= -1

            # Boundary check
            if self.ycor() < -280 or self.ycor() > 280:
                self.dy *= -1

        def bounce_paddle(self):

            # Paddle2
            if self.xcor() + 10 >= 340 and self.xcor() + 10 <= 350 and self.dx > 0:
                if self.ycor() + 10 >= self.paddle2.ycor() - 50 and self.ycor() - 10 <= self.paddle2.ycor() + 50:
                    self.dx *= -1

            # Paddle1 - ball towards paddle (dx negative or < 0),
            # between left (xcor()+10) side and middle (xcor()) of paddle,
            # between top (ycor()+50) and bottom (ycor()-50)
            if self.xcor() - 10 <= paddle1.xcor() + 10 and self.xcor() - 10 >= paddle1.xcor() and self.dx < 0:
                if self.ycor() + 10 >= self.paddle1.ycor() - 50 and self.ycor() - 10 <= self.paddle1.ycor() + 50:
                    self.dx *= -1

    # Score
    score_a = 0
    score_b = 0

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))

    paddle1 = Paddle(-350)
    paddle2 = Paddle(350)
    ball1 = Ball1(paddle1, paddle2)
    ball2 = Ball2(paddle1, paddle2)
    ball3 = Ball3(paddle1, paddle2)

    win.onkey(paddle2.move_up, 'w')
    win.onkey(paddle2.move_down, 's')
    win.onkey(paddle1.move_up, 'Up')
    win.onkey(paddle1.move_down, 'Down')

    while True:
        # time.sleep(0.017) #windows?
        balls = [ball1, ball2, ball3]
        for ball in balls:
            win.update()
            ball.move()
            ball.bounce_paddle()
            ball.move()
            ball.bounce_paddle()
            ball.move()
            ball.bounce_paddle()

            if ball.xcor() > 390:
                score_a += 1
                pen.clear()
                pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                          font=("Courier", 24, "normal"))
                if score_a >= 5:
                    pen2 = turtle.Turtle()
                    pen2.speed(0)
                    pen2.color("red")
                    pen2.penup()
                    pen2.hideturtle()
                    pen2.goto(0, 0)
                    score_a = 0
                    score_b = 0
                    pen2.write("GAME OVER!!", align="center", font=("Courier", 34, "normal"))
                    time.sleep(4)
                    pen2.clear()
                    pen.clear()
                    ball1.goto(0, 0)
                    ball2.goto(0, 0)
                    ball3.goto(0, 0)
                    pen.write("NEW GAME".format(score_a, score_b), align="center",
                                  font=("Courier", 24, "normal"))
                    pen.color("red")
                    time.sleep(4)

                    pen.clear()
                    pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                              font=("Courier", 24, "normal"))

            if ball.xcor() < -390:
                score_b += 1
                pen.clear()
                pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                          font=("Courier", 24, "normal"))
                if score_b >= 5:
                    pen1 = turtle.Turtle()
                    pen1.speed(0)
                    pen1.color("red")
                    pen1.penup()
                    pen1.hideturtle()
                    pen1.goto(0, 0)
                    score_a= 0
                    score_b = 0
                    pen1.write("GAME OVER!!", align="center", font=("Courier", 34, "normal"))
                    time.sleep(4)
                    pen1.clear()
                    pen.clear()
                    ball1.goto(0, 0)
                    ball2.goto(0, 0)
                    ball3.goto(0, 0)
                    pen.write("NEW GAME".format(score_a, score_b), align="center",
                                  font=("Courier", 24, "normal"))
                    pen.color("red")
                    time.sleep(4)
                    pen.clear()
                    pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                              font=("Courier", 24, "normal"))



                    # paddle1 - drag with mouse
            # paddle1.ondrag(paddle1.goto)

            # AI Player

            closest_ball = balls[0]
            for ball in balls:
                if ball.xcor() > closest_ball.xcor():
                    closest_ball = ball

                if paddle2.ycor() < closest_ball.ycor() and (abs(closest_ball.ycor() - paddle2.ycor()) > 20):
                    paddle2.move_up()

                elif paddle2.ycor() > closest_ball.ycor() and (abs(closest_ball.ycor() - paddle2.ycor()) > 20):
                    paddle2.move_down()

