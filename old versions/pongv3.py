# Pong by Mahdi Sabbouri
# November 7 2019

import turtle
import time
import winsound

if_paused = False
running = True
game_state = "splash"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
wn = turtle.Screen()
sn = turtle.Screen()
go = turtle.Screen()
paddle_a = turtle.Turtle()
paddle_b = turtle.Turtle()
ball = turtle.Turtle()
pen = turtle.Turtle()
timeCounter = turtle.Turtle()
quitText = turtle.Turtle()

def start_game():
    global game_state
    game_state = "game"

def start_game_ai():
    global game_state
    game_state = "game-with-ai"

def end_game():
    global game_state
    game_state = "gameover"

main_running = True

def quit():
    global main_running
    main_running = False

def gameover_window():
    global go
    wn.title("Pong by Team 1")
    wn.bgcolor("black")
    wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    wn.tracer(2)

    time_limit = 5
    start_time = time.time()

    # Main game loop
    while (time.time() - start_time) < time_limit:
        elapsed_time = time.time() - start_time
        start_time = time.time() - elapsed_time
        wn.update()
    return True


def splash_Screen():
    global sn, running
    sn.title("Pong by Team 1")

    wn.bgcolor("black")
    sn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    sn.tracer(2)
    sn.listen()
    sn.onkeypress(start_game, " ")
    sn.onkeypress(start_game_ai, "a")
    sn.onkeypress(quit, "q")
    while running:
        sn.update()
        if game_state == "splash":
            sn.bgpic("splash_pong.gif")
        elif game_state == "game":
            sn.bgpic("game_background.gif")
            done = main(0)
            if done:
                sn.bgpic("gameover.gif")
                if gameover_window():
                    running = False
        elif game_state == "game-with-ai":
            sn.bgpic("game_background.gif")
            done = main(1)
            if done:
                sn.bgpic("gameover.gif")
                if gameover_window():
                    running = False
        elif game_state == "gameover":
            if gameover_window():
                running = False

#Two timers means two threads?



def toggle_pause():
    global if_paused
    if if_paused == True:
        if_paused = False
    else:
        if_paused = True

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

def main(ifAI):
    #global Turtles and Screen
    global wn, paddle_a, paddle_b, ball, pen, timeCounter, quitText, main_running

    # Score
    score_a = 0
    score_b = 0

    # window creation
    wn.title("Pong by Team 1")
    wn.bgcolor("black")
    wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    wn.tracer(2)

    # Paddle A
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Paddle B
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # can do an array of balls from user select...(how many balls? )

    # Ball
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)

    #change so that the ball doesn't go as fast with tracer 2 on screen (for timer)
    ball.dx = .4
    ball.dy = .4

    # Pen (Score)
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0     Player B: 0", align="center",
              font=("Bit5x5", 24, "normal"))

    # timeCounter (Timer)
    timeCounter.speed(0)
    timeCounter.color("white")
    timeCounter.penup()
    timeCounter.hideturtle()
    timeCounter.goto(20 - SCREEN_WIDTH/2, 20 - SCREEN_HEIGHT/2)
    timeCounter.write("TIME: ", align="left",
              font=("Bit5x5", 24, "normal"))

    # quit Text
    quitText.speed(0)
    quitText.color("white")
    quitText.penup()
    quitText.hideturtle()
    quitText.goto(0, 220)
    quitText.write("press Q to quit game...", align="center",
                      font=("Bit5x5", 16, "normal"))

    # Keyboard binding
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")
    wn.onkeypress(toggle_pause, "p")
    wn.onkeypress(quit, "q")

    # added capslock buttons
    wn.onkeypress(paddle_a_up, "W")
    wn.onkeypress(paddle_a_down, "S")
    wn.onkeypress(quit, "Q")
    wn.onkeypress(toggle_pause, "P")

    time_limit = 50
    start_time = time.time()

    # Main game loop
    while (time.time() - start_time) < time_limit and main_running:
        #timeCounter.clear()
        if score_a == 4 or score_b == 4:
            quitText.clear()
        if if_paused:
            start_time = time.time() - elapsed_time
            wn.update()
        else:
            elapsed_time = time.time() - start_time
            countDown = time_limit - int(elapsed_time)
            timeCounter.clear()
            timeCounter.goto(20 - SCREEN_WIDTH/2, 20 - SCREEN_HEIGHT/2)
            timeCounter.write("TIME: {}".format(countDown), align="left", font=("Bit5x5", 24, "normal"))
            if elapsed_time >= time_limit:
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
            if ifAI == 1:
                #AI Player
                if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
                    paddle_b_up()
                elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
                    paddle_b_down()
    wn.clear()
    #wn.ontimer(main(True), 100)
    return True

splash_Screen()