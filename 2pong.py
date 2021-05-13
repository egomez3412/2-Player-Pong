import turtle
import time

import winsound

time_limit = 45
score_limit = 10
score_a = 0
score_b = 0

ball_speed_x = .4
ball_speed_y = .4

ifTwoBalls = False
ifThreeBalls = False

if_paused = False
running = True
game_state = "splash"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
wn = turtle.Screen()  # window screen
sn = turtle.Screen()  # start screen
go = turtle.Screen()  # gameover screen
ss = turtle.Screen()  # settings screen object
# paddle_a = turtle.Turtle()
# paddle_b = turtle.Turtle()
# ball = turtle.Turtle()
# ball2 = turtle.Turtle()
# ball3 = turtle.Turtle()

settings_select = turtle.Turtle()
settings_select2 = turtle.Turtle()
settings_select3 = turtle.Turtle()
settings_select4 = turtle.Turtle()

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


def settings():
    global game_state
    game_state = "settings"

restart = False

def reset():
    global restart
    restart = True

def splash():
    global game_state
    game_state = "splash"


def gameover_window():
    global wn, sn, go, ss, paddle_a
    global paddle_b
    global settings_select, settings_select2, settings_select3, settings_select4
    global ball, ball2, ball3, pen, timeCounter, quitText
    global running,restart, main_running
    restart = False
    go.title("Gameover")
    go.bgcolor("black")
    go.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    go.tracer(2)
    go.listen()
    go.onkeypress(reset, "r")  # after gave over gives user option to play again.

    time_limit = 10
    start_time = time.time()
    pen.goto(0, -50)
    scores = 'Player A: ' + str(score_a) + '     Player B: ' + str(score_b)
    pen.write(scores, align="center", font=("Bit5x5", 24, "normal"))
    pen.goto(0, -200)

    pen.color("yellow")
    res = 'Press R to restart...'
    pen.write(res, align="center", font=("Bit5x5", 18, "normal"))

    pen.color("light green")
    if (score_a > score_b):
        pen.goto(0, -100)
        scores = 'Player A is the winner!'
        pen.write(scores, align="center", font=("Bit5x5", 32, "normal"))
    elif (score_a < score_b):
        pen.goto(0, -100)
        scores = 'Player B is the winner!'
        pen.write(scores, align="center", font=("Bit5x5", 32, "normal"))
    else:
        pen.goto(0, -100)
        scores = 'Tie!'
        pen.write(scores, align="center", font=("Bit5x5", 32, "normal"))

    timeCounter.color("white")
    timeCounter.goto(20 - SCREEN_WIDTH / 2, 20 - SCREEN_HEIGHT / 2)
    timeCounter.write("TIME: ", align="left",
                      font=("Bit5x5", 24, "normal"))
    go.update()
    go.reset()

    while (time.time() - start_time) < time_limit and not restart:
        elapsed_time = time.time() - start_time
        start_time = time.time() - elapsed_time
        timeCounter.clear()
        countDown = time_limit - int(elapsed_time)
        timeCounter.write("TIME: {}".format(countDown), align="left",
                          font=("Bit5x5", 24, "normal"))
    pen.clear()
    timeCounter.clear()
    if restart:
        main_running = True
        running = True
        splash()
        splash_Screen()
        return False
    return True

def settings_clicked(x, y):
    global ss, sn
    # while running:
    while game_state == "splash":
        if (x >= -14.0 and x <= 14.0 and y >= -255.0 and y <= -229.0):  # gear icon / settings icon
            # print("x = ",x,", y = ",y)
            settings_screen()
            # ss.bgpic("settings.gif")
        else:
            sn.update()
            # print("x = ",x,", y = ",y)

def settings_screen():
    # settings_select = turtle.Turtle()
    # settings_select2 = turtle.Turtle()
    # settings_select3 = turtle.Turtle()
    # settings_select4 = turtle.Turtle()
    def save_clicked(x, y):
        global settings_select, settings_select2, settings_select3, settings_select4

        # settings_select.shape("square")
        # settings_select.color("light green")
        # settings_select.shapesize(stretch_wid=0.5, stretch_len=0.5)
        # settings_select.goto(SCREEN_WIDTH - 1, SCREEN_HEIGHT - 1)
        # settings_select.penup()
        # settings_select.clear()
        #
        # settings_select2.shape("square")
        # settings_select2.color("light green")
        # settings_select2.shapesize(stretch_wid=0.5, stretch_len=0.5)
        # settings_select2.goto(SCREEN_WIDTH - 1, SCREEN_HEIGHT - 1)
        # settings_select2.penup()
        # settings_select2.clear()
        #
        # settings_select3.shape("square")
        # settings_select3.color("light green")
        # settings_select3.shapesize(stretch_wid=0.5, stretch_len=0.5)
        # settings_select3.goto(SCREEN_WIDTH - 1, SCREEN_HEIGHT - 1)
        # settings_select3.penup()
        # settings_select3.clear()
        #
        # settings_select4.shape("square")
        # settings_select4.color("light green")
        # settings_select4.shapesize(stretch_wid=0.5, stretch_len=0.5)
        # settings_select4.goto(SCREEN_WIDTH-1,SCREEN_HEIGHT-1)
        # settings_select4.penup()
        # settings_select4.clear()


        settings_select.shape("square")
        settings_select.color("light green")
        settings_select.shapesize(stretch_wid=2.7, stretch_len=2.7)
        settings_select.penup()
        settings_select.clear()

        settings_select2.shape("square")
        settings_select2.color("light green")
        settings_select2.shapesize(stretch_wid=2.9, stretch_len=2.7)
        settings_select2.penup()
        settings_select2.clear()

        settings_select3.shape("square")
        settings_select3.color("light green")
        settings_select3.shapesize(stretch_wid=2.7, stretch_len=5.5)
        settings_select3.penup()
        settings_select3.clear()

        settings_select4.shape("square")
        settings_select4.color("light green")
        settings_select4.shapesize(stretch_wid=2.8, stretch_len=5.5)
        settings_select4.penup()
        settings_select4.clear()

        global time_limit, score_limit, ball_speed_x, ball_speed_y #use this in a different func if needed
        global ifTwoBalls, ifThreeBalls
        """
        if game_state == "settings": #test coordinates
            print("x = ",x,", y = ",y) #to check coordinates

            #seconds
            if (x >= 1.0 and x <= 56.0 and y >= 21.0 and y <= 76.0):
                print("you selected 10 seconds.")
            elif (x >= 57.0 and x <= 111.0 and y >= 21.0 and y <= 76.0):
                print("you selected 20 seconds.")
            elif (x >= 112.0 and x <= 168.0 and y >= 21.0 and y <= 76.0):
                print("you selected 30 seconds.")
            elif (x >= 169.0 and x <= 225.0 and y >= 21.0 and y <= 76.0):
                print("you selected 40 seconds.")
            elif (x >= 226.0 and x <= 281.0 and y >= 21.0 and y <= 76.0):
                print("you selected 45 seconds.")
            elif (x >= 282.0 and x <= 337.0 and y >= 21.0 and y <= 76.0):
                print("you selected 60 seconds.")
            
            #score limit
            elif (x >= 1.0 and x <= 56.0 and y >= -39.0 and y <= 20.0):
                print("you selected 5 point limit.")
            elif (x >= 57.0 and x <= 111.0 and y >= -39.0 and y <= 20.0):
                print("you selected 10 point limit.")
            elif (x >= 112.0 and x <= 168.0 and y >= -39.0 and y <= 20.0):
                print("you selected 25 point limit.")
            elif (x >= 169.0 and x <= 225.0 and y >= -39.0 and y <= 20.0):
                print("you selected 50 point limit.")
            elif (x >= 226.0 and x <= 281.0 and y >= -39.0 and y <= 20.0):
                print("you selected 75 point limit.")
            elif (x >= 282.0 and x <= 337.0 and y >= -39.0 and y <= 20.0):
                print("you selected 99 point limit.")
            
            #Number of Balls
            elif (x >= 1.0 and x <= 111.0 and y >= -94.0 and y <= -41.0):
                print("you selected 1 ball.")
            elif (x >= 112.0 and x <= 225.0 and y >= -94.0 and y <= -41.0):
                print("you selected 2 balls.")
            elif (x >= 226.0 and x <= 337.0 and y >= -94.0 and y <= -41.0):
                print("you selected 3 balls.")
            
            #Ball Speed
            elif (x >= 1.0 and x <= 111.0 and y >= -153.0 and y <= -97.0):
                print("you selected 1x speed.")
            elif (x >= 112.0 and x <= 225.0 and y >= -153.0 and y <= -97.0):
                print("you selected 2x speed.")
            elif (x >= 226.0 and x <= 337.0 and y >= -153.0 and y <= -97.0):
                print("you selected 3x speed.")
        """
        if game_state == "settings": #settings logic
            #seconds
            if (x >= 1.0 and x <= 56.0 and y >= 21.0 and y <= 76.0):
                print("you selected 10 seconds.")
                # pen.goto(x,y)
                # pen.color('red')
                # pen.write(str(x)+","+str(y))
                settings_select.clear()
                settings_select.color("light green")
                settings_select.shapesize(stretch_wid=2.7, stretch_len=2.7)
                # settings_select2.reset()
                # settings_select3.reset()
                # settings_select4.reset()
                settings_select.goto(28, 51)
                time_limit = 10
            elif (x >= 57.0 and x <= 111.0 and y >= 21.0 and y <= 76.0):
                print("you selected 20 seconds.")
                settings_select.clear()
                settings_select.color("light green")
                settings_select.shapesize(stretch_wid=2.7, stretch_len=2.7)
                settings_select.goto(84, 51)
                time_limit = 20
            elif (x >= 112.0 and x <= 168.0 and y >= 21.0 and y <= 76.0):
                print("you selected 30 seconds.")
                settings_select.clear()
                settings_select.color("light green")
                settings_select.shapesize(stretch_wid=2.7, stretch_len=2.7)
                settings_select.goto(140, 51)
                time_limit = 30
            elif (x >= 169.0 and x <= 225.0 and y >= 21.0 and y <= 76.0):
                print("you selected 40 seconds.")
                settings_select.clear()
                settings_select.color("light green")
                settings_select.shapesize(stretch_wid=2.7, stretch_len=2.7)
                settings_select.goto(196, 51)
                time_limit = 40
            elif (x >= 226.0 and x <= 281.0 and y >= 21.0 and y <= 76.0):
                print("you selected 45 seconds.")
                settings_select.clear()
                settings_select.color("light green")
                settings_select.shapesize(stretch_wid=2.7, stretch_len=2.7)
                settings_select.goto(252, 51)
                time_limit = 45
            elif (x >= 282.0 and x <= 337.0 and y >= 21.0 and y <= 76.0):
                print("you selected 60 seconds.")
                settings_select.clear()
                settings_select.color("light green")
                settings_select.shapesize(stretch_wid=2.7, stretch_len=2.7)
                settings_select.goto(308, 51)
                time_limit = 60
            #score limit
            if  (x >= 1.0 and x <= 56.0 and y >= -39.0 and y <= 20.0):
                print("you selected 5 point limit.")
                # pen.goto(x,y)
                # pen.color('red')
                # pen.write(str(x)+","+str(y))
                settings_select2.clear()
                settings_select2.color("light green")
                settings_select2.shapesize(stretch_wid=2.9, stretch_len=2.7)
                settings_select2.goto(28, -7)
                score_limit = 5
            elif (x >= 57.0 and x <= 111.0 and y >= -39.0 and y <= 20.0):
                print("you selected 10 point limit.")
                settings_select2.clear()
                settings_select2.color("light green")
                settings_select2.shapesize(stretch_wid=2.9, stretch_len=2.7)
                settings_select2.goto(84, -7)
                score_limit = 10
            elif (x >= 112.0 and x <= 168.0 and y >= -39.0 and y <= 20.0):
                print("you selected 25 point limit.")
                settings_select2.clear()
                settings_select2.color("light green")
                settings_select2.shapesize(stretch_wid=2.9, stretch_len=2.7)
                settings_select2.goto(140, -7)
                score_limit = 25
            elif (x >= 169.0 and x <= 225.0 and y >= -39.0 and y <= 20.0):
                print("you selected 50 point limit.")
                settings_select2.clear()
                settings_select2.color("light green")
                settings_select2.shapesize(stretch_wid=2.9, stretch_len=2.7)
                settings_select2.goto(196, -7)
                score_limit = 50
            elif (x >= 226.0 and x <= 281.0 and y >= -39.0 and y <= 20.0):
                print("you selected 75 point limit.")
                settings_select2.clear()
                settings_select2.color("light green")
                settings_select2.shapesize(stretch_wid=2.9, stretch_len=2.7)
                settings_select2.goto(252, -7)
                score_limit = 75
            elif (x >= 282.0 and x <= 337.0 and y >= -39.0 and y <= 20.0):
                print("you selected 99 point limit.")
                settings_select2.clear()
                settings_select2.color("light green")
                settings_select2.shapesize(stretch_wid=2.9, stretch_len=2.7)
                settings_select2.goto(308, -7)
                score_limit = 99
            #***NUMBER OF BALLS CODE HERE***
            elif (x >= 1.0 and x <= 111.0 and y >= -94.0 and y <= -41.0):
                print("you selected 1 ball.")
                ifTwoBalls = False
                ifThreeBalls = False
                # pen.goto(x,y)
                # pen.color('red')
                # pen.write(str(x)+","+str(y))
                settings_select3.clear()
                settings_select3.color("light green")
                settings_select3.shapesize(stretch_wid=2.7, stretch_len=5.5)
                settings_select3.goto(56, -65)
            elif (x >= 112.0 and x <= 225.0 and y >= -94.0 and y <= -41.0):
                print("you selected 2 balls.")
                settings_select3.clear()
                settings_select3.color("light green")
                settings_select3.shapesize(stretch_wid=2.7, stretch_len=5.5)
                settings_select3.goto(168, -65)
                ifTwoBalls = True
                ifThreeBalls = False
            elif (x >= 226.0 and x <= 337.0 and y >= -94.0 and y <= -41.0):
                print("you selected 3 balls.")
                settings_select3.clear()
                settings_select3.color("light green")
                settings_select3.shapesize(stretch_wid=2.7, stretch_len=5.5)
                settings_select3.goto(280, -65)
                ifTwoBalls = True
                ifThreeBalls = True
            #Ball Speed
            if (x >= 1.0 and x <= 111.0 and y >= -153.0 and y <= -97.0):
                print("you selected 1x speed.")
                # pen.goto(x,y)
                # pen.color('red')
                # pen.write(str(x)+","+str(y))
                settings_select4.clear()
                settings_select4.color("light green")
                settings_select4.shapesize(stretch_wid=2.8, stretch_len=5.5)
                settings_select4.goto(56, -122)
                ball_speed_x = .4
                ball_speed_y = .4
            elif (x >= 112.0 and x <= 225.0 and y >= -153.0 and y <= -97.0):
                print("you selected 2x speed.")
                settings_select4.clear()
                settings_select4.color("light green")
                settings_select4.shapesize(stretch_wid=2.8, stretch_len=5.5)
                settings_select4.goto(168, -122)
                ball_speed_x = .8
                ball_speed_y = .8
            elif (x >= 226.0 and x <= 337.0 and y >= -153.0 and y <= -97.0):
                print("you selected 3x speed.")
                settings_select4.clear()
                settings_select4.color("light green")
                settings_select4.shapesize(stretch_wid=2.8, stretch_len=5.5)
                settings_select4.goto(280, -122)
                ball_speed_x = 1.2 #real 3x = 1.2
                ball_speed_y = 1.2 #real 3x = 1.2
            if (x >= -47.0 and x <= 44.0 and y >= -237.0 and y <= -218.0): #save button (saves user's settings)
                # game_state == "" #resert the game_state for splash?
                settings_select.reset()
                settings_select2.reset()
                settings_select3.reset()
                settings_select4.reset()
                sn.update()
                splash()
                #time_limit = 10 #update time_limit if user presses this coordinates,,, function maybe...
                #score_limit = 1 #update score_limit if user presses,,,
                # ball_speed_x = .8 #update x ball speed if user presses,,,
                # ball_speed_y = .8 #update y ball speed if user presses,,,
                #ball_speed_x = 4.0  # update x ball speed if user presses,,,
                #ball_speed_y = 4.0  # update y ball speed if user presses,,,
                # game_state == "splash"
                # print("x = ",x,", y = ",y) #used to see cordinates of clicked.
                # gameover_window() #does update screen but for a second
                # sn.bgpic("splash_pong.gif") #switches screen to splash but no other onkeypress works (disabled)
                splash_Screen()
            else:
                sn.update()
    global ss
    game_state = "settings"
    ss.title("Settings")
    ss.bgcolor("black")
    ss.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    ss.tracer(2)
    sn.listen()
    # while running: #needed?
    ss.update()
    ss.bgpic("settings.gif")
    ss.onclick(save_clicked)


# mainloop() #needed to keep listening for clicks
# return splash() #is it needed?

def splash_Screen():
    global sn, running, restart
    running = True
    sn.title("Pong by Team 1")
    wn.bgcolor("black")
    sn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    sn.tracer(2)
    sn.listen()
    sn.onkeypress(start_game, " ")
    sn.onkeypress(start_game_ai, "a")
    sn.onkeypress(quit, "q")
    # sn.onkeypress(settings, "s")
    sn.onclick(settings_clicked)

    while running:
        sn.update()
        if game_state == "splash":
            sn.bgpic("splash_pong.gif")
        elif game_state == "game":
            sn.bgpic("game_background.gif")
            done = main(0)
            if done:
                sn.bgpic("gameover.gif")
                done = gameover_window()
                if done:
                    running = False
        elif game_state == "game-with-ai":
            sn.bgpic("game_background.gif")
            done = main(1)
            if done:
                sn.bgpic("gameover.gif")
                if gameover_window():
                    running = False
        elif game_state == "gameover":
            gameover_window()
            if gameover_window():
                running = False
        elif game_state == "settings":
            settings_screen()

def toggle_pause():
    global if_paused
    if if_paused == True:
        if_paused = False
    else:
        if_paused = True

def main(ifAI):
    # global Turtles and Screen
    paddle_a = turtle.Turtle()
    paddle_b = turtle.Turtle()
    ball = turtle.Turtle()
    ball2 = turtle.Turtle()
    ball3 = turtle.Turtle()
    # global paddle_a, paddle_b, ball, ball2, ball3
    global wn, pen, timeCounter, quitText, main_running, time_limit, score_limit
    global ball_speed_x, ball_speed_y, ifTwoBalls, ifThreeBalls, running
    main_running = True
    running = True
    # Score
    global score_a
    score_a = 0
    global score_b
    socre_b = 0

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

    # window creation
    wn.title("2 Player Pong")
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
    # if(ifTWoBalls):
    #     create the other ball
    #     ball2
    # if(three):
    #     create two more balls

    # Ball
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)

    if ifTwoBalls:
        # Ball2
        ball2.shape("circle")
        ball2.color("red")
        ball2.penup()
        ball2.goto(0, 0)

    if ifThreeBalls:
        # Ball3
        ball3.shape("circle")
        ball3.color("yellow")
        ball3.penup()
        ball3.goto(0, 0)

    # change so that the ball doesn't go as fast with tracer 2 on screen (for timer)
    """
    ball.dx = .4
    ball.dy = .4
    ball2.dx = -.4
    ball2.dy = -.4
    """
    ball.dx = ball_speed_x
    ball.dy = ball_speed_y

    if ifTwoBalls:
        ball2.dx = -ball_speed_x
        ball2.dy = -ball_speed_y
    if ifThreeBalls:
        ball3.dx = ball_speed_x
        ball3.dy = -ball_speed_y

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
    timeCounter.goto(20 - SCREEN_WIDTH / 2, 20 - SCREEN_HEIGHT / 2)
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

    # time_limit = 5
    start_time = time.time()

    # Main game loop
    while (time.time() - start_time) < time_limit and main_running:
        # timeCounter.clear()
        if score_a == 4 or score_b == 4:
            quitText.clear()
        if if_paused:
            start_time = time.time() - elapsed_time
            wn.update()
        else:
            elapsed_time = time.time() - start_time
            countDown = time_limit - int(elapsed_time)
            timeCounter.clear()
            timeCounter.goto(20 - SCREEN_WIDTH / 2, 20 - SCREEN_HEIGHT / 2)
            timeCounter.write("TIME: {}".format(countDown), align="left", font=("Bit5x5", 24, "normal"))
            if elapsed_time >= time_limit:
                print("GAME OVER")  # need to print on screen!
                exit()
            if score_a == score_limit or score_b == score_limit:
                print("GAME OVER")  # need to print on screen!
                quit()
                exit()

            # Move the ball
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)
            if ifTwoBalls:
                ball2.setx(ball2.xcor() + ball2.dx)
                ball2.sety(ball2.ycor() + ball2.dy)

            if ifThreeBalls:
                ball3.setx(ball3.xcor() + ball3.dx)
                ball3.sety(ball3.ycor() + ball3.dy)

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
            if ifTwoBalls:
                if ball2.ycor() > 290:
                    ball2.sety(290)
                    ball2.dy *= -1
                    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

                if ball2.ycor() < -290:
                    ball2.sety(-290)
                    ball2.dy *= -1
                    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

                if ball2.xcor() > 390:
                    ball2.goto(0, 0)
                    ball2.dx *= -1
                    score_a += 1
                    pen.clear()
                    pen.goto(0, 260)
                    pen.write("Player A: {}     Player B: {}".format(score_a, score_b), align="center",
                              font=("Bit5x5", 24, "normal"))

                if ball2.xcor() < -390:
                    ball2.goto(0, 0)
                    ball2.dx *= -1
                    score_b += 1
                    pen.clear()
                    pen.goto(0, 260)
                    pen.write("Player A: {}     Player B: {}".format(score_a, score_b), align="center",
                              font=("Bit5x5", 24, "normal"))

            if ifThreeBalls:
                if ball3.ycor() > 290:
                    ball3.sety(290)
                    ball3.dy *= -1
                    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

                if ball3.ycor() < -290:
                    ball3.sety(-290)
                    ball3.dy *= -1
                    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

                if ball3.xcor() > 390:
                    ball3.goto(0, 0)
                    ball3.dx *= -1
                    score_a += 1
                    pen.clear()
                    pen.goto(0, 260)
                    pen.write("Player A: {}     Player B: {}".format(score_a, score_b), align="center",
                              font=("Bit5x5", 24, "normal"))

                if ball3.xcor() < -390:
                    ball3.goto(0, 0)
                    ball3.dx *= -1
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

            if ifTwoBalls:
                if (ball2.xcor() > 340 and ball2.xcor() < 350) and (
                        ball2.ycor() < paddle_b.ycor() + 40 and ball2.ycor() > paddle_b.ycor() - 40):
                    ball2.setx(340)
                    ball2.dx *= -1
                    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

                if (ball2.xcor() < -340 and ball2.xcor() > -350) and (
                        ball2.ycor() < paddle_a.ycor() + 40 and ball2.ycor() > paddle_a.ycor() - 40):
                    ball2.setx(-340)
                    ball2.dx *= -1
                    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

            if ifThreeBalls:
                if (ball3.xcor() > 340 and ball3.xcor() < 350) and (
                        ball3.ycor() < paddle_b.ycor() + 40 and ball3.ycor() > paddle_b.ycor() - 40):
                    ball3.setx(340)
                    ball3.dx *= -1
                    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

                if (ball3.xcor() < -340 and ball3.xcor() > -350) and (
                        ball3.ycor() < paddle_a.ycor() + 40 and ball3.ycor() > paddle_a.ycor() - 40):
                    ball3.setx(-340)
                    ball3.dx *= -1
                    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

            if ifAI == 1:
                # AI Player
                if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
                    paddle_b_up()
                elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
                    paddle_b_down()
                if ifTwoBalls:
                    if ball.xcor() > ball2.xcor():
                        if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
                            paddle_b_up()
                        elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
                            paddle_b_down()
                    else:
                        if paddle_b.ycor() < ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 10:
                            paddle_b_up()
                        elif paddle_b.ycor() > ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 10:
                            paddle_b_down()

                if ifThreeBalls:
                    if ball2.xcor() > ball3.xcor():
                        if paddle_b.ycor() < ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 10:
                            paddle_b_up()
                        elif paddle_b.ycor() > ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 10:
                            paddle_b_down()
                    else:
                        if paddle_b.ycor() < ball3.ycor() and abs(paddle_b.ycor() - ball3.ycor()) > 10:
                            paddle_b_up()
                        elif paddle_b.ycor() > ball3.ycor() and abs(paddle_b.ycor() - ball3.ycor()) > 10:
                            paddle_b_down()
            # if(two balls then this)
    wn.clear()
    return True


splash_Screen()
# settings_screen()
