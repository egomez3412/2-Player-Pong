import turtle
import time
import math
import winsound

win = turtle.Screen()
win.bgcolor("black")
win.title("Timer")

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.setx(-75)

box = turtle.Turtle()
box.hideturtle()
box.color("white")
box.pensize(5)
box.penup()
box.setx(-50)
box.sety(-50)
box.pendown()
box.forward(250)
box.left(90)
box.forward(150)
box.left(90)
box.forward(300)
box.left(90)
box.forward(150)
box.left(90)
box.forward(150)

num = math.floor(win.numinput("Timer", "Enter the seconds", minval=0, maxval=59))
minute = math.floor(win.numinput("Timer", "Enter the minutes number: ", minval=0, maxval=59))
hours = math.floor(win.numinput("Timer", "Enter the hours number: ", minval=0, maxval=59))
stop = False

while True:
    pen.sety(0)
    pen.write(str(hours)+":"+str(minute)+":"+str(num), font=("Arial", 50))
    pen.sety(100)
    pen.write("Time Left:", font=("Arial", 15))
    num -= 1
    time.sleep(1)
    pen.clear()
    if num <= 0 and minute <= 0 and hours <= 0:
        pen.clear()
        box.clear()
        pen.setx(-100)
        pen.write("Time Over", font=("Arial", 50))
        winsound.PlaySound("E:\\Nirma\\ChillingMusic.wav", winsound.SND_ASYNC)
        time.sleep(5)
        pen.clear()
        break
    if num == 0 and minute >= 1 and stop is not True:
        num = 60
        minute -= 1
    if num == 0 and minute == 0 and hours >= 1 and stop is not True:
        minute = 60
        hours -= 1
    print(num)
    win.update()

print("Time Has Ended!!")


import turtle

if_paused = False
game_state = "splash"

def start_game():
    global game_state
    game_state = "game"

    #Reset the Game

def end_game():
    global game_state
    game_state = "gameover"

    #Game Over Timer

def toggle_pause():
    global if_paused
    if if_paused == True:
        if_paused = False
    else:
        if_paused = True
def test():
    wn = turtle.Screen()
    wn.title("test")
    wn.bgcolor("black")

    bob = turtle.Turtle()
    bob.speed(0)
    bob.color("yellow")
    bob.shape("triangle")
    bob.penup()



    wn.listen()
    wn.onkeypress(toggle_pause, "p")
    wn.onkeypress(start_game, " ")
    wn.onkeypress(end_game, "q")
    
    if not if_paused:
        bob.fd(1)
        bob.lt(1)
    

    while True:
        bob.clear()
        if game_state == "splash":
            wn.bgpic("splash.gif")
        elif game_state == "game":
            wn.bgpic("main.gif")
        elif game_state == "gameover":
            wn.bgpic("game_over.gif")

        wn.update()

test()
"""
import tkinter
root = tkinter.Tk()
#root.geometry("500x450")
root.title("Concatinate Strings!")

#Create Functions
def concatStr():
    first = label_first_word.get()
    second = label_second_word.get()
    concat = first + second
    label_result['text'] = f"Result: {concat}"

#Create GUI


#Create Labels
label_first_word = tkinter.Label(root, text="Field One: ")
label_first_word.grid(column=0, row=0)
#label_first_word.pack()

label_first_word = tkinter.Entry(root)
label_first_word.grid(column=1, row=0)
#label_first_word.pack()

label_second_word = tkinter.Label(root, text="Field Two: ")
label_second_word.grid(column=0, row=1)
#label_second_word.pack()

label_second_word = tkinter.Entry(root)
label_second_word.grid(column=1, row=1)
#label_second_word.pack()

button_concat = tkinter.Button(root, text="Concatinate!", command=concatStr)
button_concat.grid(column=0, row=2)
#button_concat.pack()

label_result = tkinter.Label(root, text = "Result: ")
label_result.grid(column=1, row=2)
#label_result.pack()

#Execute Form
root.mainloop()
"""

time_limit = 5
    start_time = time.time()

while (time.time() - start_time) < time_limit:
    # timeCounter.clear()
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