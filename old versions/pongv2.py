# Pong by Mahdi Sabbouri
# November 7 2019

import turtle
import time
import winsound

if_paused = False
running = True
game_state = "splash"

def start_game():
    global game_state
    game_state = "game"

def toggle_pause():
    global if_paused
    if if_paused == True:
        if_paused = False
    else:
        if_paused = True

def end_game():
    global game_state
    game_state = "gameover"
    quit()

def quit():
    global running
    running = False

def main_menu():
    #close_menu = True
    ww = turtle.Screen()
    ww.title("Main Menu")
    ww.bgcolor("white")
    ww.setup(width=800, height=600)
    ww.tracer(5)

    # Pen
    temp = turtle.Turtle()
    temp.speed(0)
    temp.color("black")
    temp.penup()
    temp.hideturtle()
    temp.goto(0, 0)
    temp.write("2-Player Pong", align="center", font=("Bit5x3", 48, "bold"))

    while True:
        ww.update()

def press_space_write(pen):
    pen.clear()
    pen.goto(100, 200)
    pen.write("PRESS SPACE TO PAUSE THE GAME", align="center",
              font=("Bit5x5", 24, "normal"))


menuStart = True

def onMenu():
    global menuStart
    if menuStart == True:
        menuStart = False

def splash_Screen(wn):
    global running
    wn = turtle.Screen()
    wn.title("Pong by Team 1")
    wn.bgcolor("black")
    wn.bgpic("splash_pong.gif")
    wn.setup(width=800, height=600)
    wn.tracer(1)
    wn.listen()

    splash_timer = time.time()
    time_limit = 30

    while running:
        elapsed_time = time.time() - splash_timer
        print(time_limit - int(elapsed_time))
        if elapsed_time > time_limit:
            exit()
        if game_state == "splash":
            wn.onkeypress(start_game, "e")
        elif game_state == "game":
            running = False
        elif game_state == "gameover":
            quit()
            exit()

def main():
    wn = turtle.Screen()
    splash_Screen(wn)
    wn.clear()
    wn.bgcolor("black")
    # test

    # Score
    score_a = 0
    score_b = 0

    # Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # can do an array of balls from user select...(how many balls? )

    # Ball
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 2
    ball.dy = 2

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0     Player B: 0", align="center",
              font=("Bit5x5", 24, "normal"))
    pen.goto(0, -260)
    pen.write("PRESS SPACE TO PAUSE THE GAME", align="center",
              font=("Bit5x5", 12, "normal"))

    # Functions
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

    # Keyboard binding
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")
    #wn.onkeypress(toggle_pause, " ")
    wn.onkeypress(quit, "q")
    #wn.onkeypress(start_game, "s")

    time_limit = 999
    start_time = time.time()

    # Main game loop
    while running:
        if if_paused:
            start_time = time.time() - elapsed_time
            wn.update()
        else:
            elapsed_time = time.time() - start_time
            print(time_limit - int(elapsed_time))
            if elapsed_time > time_limit:
                print("GAME OVER") #need to print on screen!
                exit()
            # Move the ball
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # Border checking
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

            if ball.xcor() > 390:
                ball.goto(0, 0)
                ball.dx *= -1
                score_a += 1
                pen.clear()
                pen.goto(0, 260)
                pen.write("Player A: {}     Player B: {}".format(score_a, score_b), align="center",
                          font=("Bit5x5", 24, "normal"))

            if ball.xcor() < -390:
                ball.goto(0, 0)
                ball.dx *= -1
                score_b += 1
                pen.clear()
                pen.goto(0, 260)
                pen.write("Player A: {}     Player B: {}".format(score_a, score_b), align="center",
                          font=("Bit5x5", 24, "normal"))

            # Paddle and ball collisions
            if (ball.xcor() > 340 and ball.xcor() < 350) and (
                    ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
                ball.setx(340)
                ball.dx *= -1
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

            if (ball.xcor() < -340 and ball.xcor() > -350) and (
                    ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
                ball.setx(-340)
                ball.dx *= -1
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            #press_space_write(pen)
            #AI Player
            if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
                paddle_b_up()
            elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
                paddle_b_down()


def menu():
    print("Would you like to play? [y/n]")
    choice = input("> ")
    if (choice.upper() == "Y"):
        main()
    elif (choice.upper() == "N"):
        print("Exiting...")
    else:
        print("Error")


# =========#=========#=========#=========#=========#=========#=========#
if __name__ == "__main__":
    #main_menu()
    main()

# =========#=========#=========#=========#=========#=========#=========#