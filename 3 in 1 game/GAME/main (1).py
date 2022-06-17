# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import turtle
import time
import random

def game():
    # Score
    score = 0
    high_score = 0

    delay = 0.1

    # set up the screen
    wn = turtle.Screen()
    wn.title("SNAKE GAME")
    wn.bgcolor("green")
    wn.setup(width=600, height=600)
    wn.tracer(0)  # stops the window from updating so we manually update

    # Head
    head = turtle.Turtle()
    head.shape("square")
    head.color("black")
    head.speed(0)
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    # Food
    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.speed(0)
    food.penup()
    food.goto(0, 100)

    segments = []

    # Pen
    pen = turtle.Turtle()
    pen.color("white")
    pen.shape("square")
    pen.speed(0)
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0    High Score: 0", align="center", font=("Courier", 24, "normal"))


    # Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"


    def go_down():
        if head.direction != "up":
            head.direction = "down"


    def go_right():
        if head.direction != "left":
            head.direction = "right"


    def go_left():
        if head.direction != "right":
            head.direction = "left"


    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)


    # keyboard
    wn.listen()
    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_right, "Right")
    wn.onkeypress(go_left, "Left")

    while True:
        wn.update()
        # check for collision with wall
        if head.ycor() > 290 or head.ycor() < -290 or head.xcor() > 290 or head.xcor() < -290:
            time.sleep(0.7)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}    High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

        # check for collision with food
        if head.distance(food) < 20:
            # Move the food to random place
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.color("grey")
            new_segment.speed(0)
            new_segment.shape("circle")
            new_segment.penup()
            segments.append(new_segment)

            # shorten the delay
            delay -= 0.001

            # increase the score
            score += 10
            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score: {}    High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

        # move the end segments first in reverse order
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        # move segment 0 to where head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        # Check for head collisions with body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"

                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # Clear the segment list
                segments.clear()

                # Reset the score
                score = 0

                # Reset the delay
                delay = 0.1

                pen.clear()
                pen.write("Score: {}    High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 24, "normal"))

        time.sleep(delay)

    wn.mainloop()