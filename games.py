from tkinter import *
from time import sleep
import os


colour=["yellow", "#FF8C00", "red", "black"]

solids=False
sheild=False


def retry():
    if pause==True:
        pausewindow.destroy()
    elif Lose==True:
        losewindow.destroy()
    root.destroy()
    os.system('python main.py')


def exit():
    if pause==True:
        pausewindow.destroy()
    elif Lose==True:
        losewindow.destroy()
    root.destroy()


def continuegame():
    global pause
    pausewindow.destroy()
    pause = False


def undo(e):
    global sheild,solids,s,ball
    solids=False
    sheild=False
    canvas.itemconfig(ball,fill="red")
    canvas.delete(s)

def sheilds(e):
    global sheild,canvas,s
    sheild=True
    s=canvas.create_rectangle(0,490,700,500,fill="blue")

def solid(e):
    global solids,ball
    canvas.itemconfig(ball,fill="white")
    solids=True


def left(event):
    if canvas.bbox(rectangle)[0] > 0:
        x = -10
        y = 0
        canvas.move(rectangle,x,y)

        global start,end
        start=canvas.bbox(rectangle)[0]
        end=canvas.bbox(rectangle)[2]


def right(event):
    if canvas.bbox(rectangle)[2] < 700:
        x = 10
        y = 0
        canvas.move(rectangle, x, y)

        global start, end
        start = canvas.bbox(rectangle)[0]
        end = canvas.bbox(rectangle)[2]


def breakbrick():
    global yvelocity, score, cheats
    for i in bricklist1:
        posbrick = canvas.coords(i)
        if posball[1] < posbrick[3] and int((posball[0] + posball[2]) / 2) in range(int(posbrick[0]),
                                                                                    int(posbrick[2])) and colour[
            0] == "yellow":
            if solids == True:
                yvelocity = yvelocity
            else:
                yvelocity = -yvelocity
            canvas.itemconfig(i, fill=colour[3])
            bricklist1.remove(i)
            score += 10
    for i in bricklist2:
        posbrick = canvas.coords(i)
        if posball[1] < posbrick[3] and int((posball[0] + posball[2]) / 2) in range(int(posbrick[0]),
                                                                                    int(posbrick[2])) and colour[
            1] == "#FF8C00":
            if solids == True:
                yvelocity = yvelocity
            else:
                yvelocity = -yvelocity
            canvas.itemconfig(i, fill=colour[3])
            bricklist2.remove(i)
            score += 10
    for i in bricklist3:
        posbrick = canvas.coords(i)
        if posball[1] < posbrick[3] and int((posball[0] + posball[2]) / 2) in range(int(posbrick[0]),
                                                                                    int(posbrick[2])) and colour[
            2] == "red":
            if solids == True:
                yvelocity = yvelocity
            else:
                yvelocity = -yvelocity
            canvas.itemconfig(i, fill=colour[3])
            bricklist3.remove(i)
            score += 10
    check_win()


def ballmove():
    global posball, yvelocity, xvelocity
    if posball[1] < 0:
        yvelocity = -yvelocity
    if posball[0] < 0 or posball[2] > 700:
        xvelocity = -xvelocity
    if posball[3] > posbar[1] and int((posball[0] + posball[2]) / 2) in range(int(start), int(end)):
        yvelocity = -yvelocity
    canvas.move(ball, xvelocity, yvelocity)
    posball = canvas.coords(ball)
    breakbrick()
    update_score()
    Live_lost()
    root.update()
    sleep(0.01)

def update_score():
    Score_txt = ("Score: " + str(score))
    canvas.itemconfigure(Score_text, text=Score_txt)

def Live_lost():
    global Lives, yvelocity, xvelocity,sheild
    if posball[3]>500:
        if sheild == True:
                yvelocity = -yvelocity
        else:
            Lives-=1
            livelost=canvas.create_text(150, 12, text="Live lost", font="Times 18 bold", fill="Red")
            root.update()
            Lives_txt=("Lives: "+str(Lives))
            sleep(1)
            canvas.delete(livelost)
            canvas.itemconfigure(Lives_text, text=Lives_txt)
            canvas.coords(ball,30,90,50,110)
            xvelocity=6
    check_lose()

def pause_game():
    global pause, pausewindow
    if pause is False:
        pause= True
        pausewindow=Toplevel()
        pausewindow.geometry("700x500")
        canvas2 = Canvas(pausewindow, width=700, height=500)
        pbg = PhotoImage(file="3d.png")
        canvas2.create_image(350, 250, image=pbg)
        canvas2.create_text(350, 100, font=("Times 80 bold", 50), text='GAME PAUSED', fill='white')

        img = PhotoImage(file="retry.png")
        pbtn = Button(canvas2, image=img, command=retry, borderwidth=0)
        pbtn.place(x=150, y=300)

        img2 = PhotoImage(file="exit.png")
        pbtn2 = Button(canvas2,image=img2, command=exit, borderwidth=0)
        pbtn2.place(x=368, y=305)

        img3=PhotoImage(file="continue.png")
        pbtn3=Button(canvas2, image=img3, command=continuegame, borderwidth=0)
        pbtn3.place(x=150, y=160)

        canvas2.pack()
        pausewindow.up()


def check_win():
    global win
    if bricklist1 == [] and bricklist2 == [] and bricklist3 == []:
        win = True

def check_lose():

    global Lose
    if Lives == 0:
        Lose = True

def bosskey(event):
    os.system('notepad game.txt')



root = Tk()
root.title("Brick Breaker")
root.iconbitmap("icon.ico")
root.geometry('700x500')
w=700
h=500
x=190
y=460
score=0
Score_txt=("Score: "+str(score))
Lives=3
Lives_txt=("Lives: "+str(Lives))
win=False
Lose=False
pause=False

canvas=Canvas(root,width=w,height=h,bg="black")
bg = PhotoImage(file="black2.png")
canvas.create_image(350,250,image=bg)
Score_text=canvas.create_text(w/2,12,font="Times 18 bold", text=Score_txt, fill="white")
Lives_text=canvas.create_text(45,12,font="Times 18 bold", text=Lives_txt, fill="white")
canvas.pack()

brick1=canvas.create_rectangle(0,80,70,100,fill=colour[0])
brick2=canvas.create_rectangle(70,80,140,100,fill=colour[0])
brick3=canvas.create_rectangle(140,80,210,100,fill=colour[0])
brick4=canvas.create_rectangle(210,80,280,100,fill=colour[0])
brick5=canvas.create_rectangle(280,80,350,100,fill=colour[0])
brick6=canvas.create_rectangle(350,80,420,100,fill=colour[0])
brick7=canvas.create_rectangle(420,80,490,100,fill=colour[0])
brick8=canvas.create_rectangle(490,80,560,100,fill=colour[0])
brick9=canvas.create_rectangle(560,80,630,100,fill=colour[0])
brick10=canvas.create_rectangle(630,80,700,100,fill=colour[0])
brick11=canvas.create_rectangle(0,40,70,60,fill=colour[1])
brick12=canvas.create_rectangle(70,40,140,60,fill=colour[1])
brick13=canvas.create_rectangle(140,40,210,60,fill=colour[1])
brick14=canvas.create_rectangle(210,40,280,60,fill=colour[1])
brick15=canvas.create_rectangle(280,40,350,60,fill=colour[1])
brick16=canvas.create_rectangle(350,40,420,60,fill=colour[1])
brick17=canvas.create_rectangle(420,40,490,60,fill=colour[1])
brick18=canvas.create_rectangle(490,40,560,60,fill=colour[1])
brick19=canvas.create_rectangle(560,40,630,60,fill=colour[1])
brick20=canvas.create_rectangle(630,40,700,60,fill=colour[1])
brick21=canvas.create_rectangle(0,60,70,80,fill=colour[2])
brick22=canvas.create_rectangle(70,60,140,80,fill=colour[2])
brick23=canvas.create_rectangle(140,60,210,80,fill=colour[2])
brick24=canvas.create_rectangle(210,60,280,80,fill=colour[2])
brick25=canvas.create_rectangle(280,60,350,80,fill=colour[2])
brick26=canvas.create_rectangle(350,60,420,80,fill=colour[2])
brick27=canvas.create_rectangle(420,60,490,80,fill=colour[2])
brick28=canvas.create_rectangle(490,60,560,80,fill=colour[2])
brick29=canvas.create_rectangle(560,60,630,80,fill=colour[2])
brick30=canvas.create_rectangle(630,60,700,80,fill=colour[2])

bricklist1=[brick10,brick9,brick8,brick7,brick6,brick5,brick4,brick3,brick2,brick1]
bricklist2=[brick11,brick12,brick13,brick14,brick15,brick16,brick17,brick18,brick19,brick20]
bricklist3=[brick30,brick29,brick28,brick27,brick26,brick25,brick24,brick23,brick22,brick21]

img = PhotoImage(file="paddle.png")
rectangle = canvas.create_image(x+134.5,y,image=img)
paddle = canvas.bbox(rectangle)


start = paddle[0]
end = paddle[2]
Pause_txt=None
ball = canvas.create_oval(30, 150, 50, 170, fill="red")
xvelocity = 6
yvelocity = 6

posball=canvas.coords(ball)
posbar=paddle
pic = PhotoImage(file="pause.png")

pause_button=Button(root,image=pic,command=pause_game)
pause_button.place(x=650, y=0)
while win is False:
    while Lose is False and win is False:
        root.bind("<Left>", left)
        root.bind("<Right>", right)
        root.bind("<i>",solid)
        root.bind("<o>",sheilds)
        root.bind("<p>",undo)
        root.bind('<b>',bosskey)
        if pause is False:
            ballmove()
        else:
            root.update()

    if Lose is True:
        losewindow = Toplevel()
        losewindow.geometry("500x350")
        losecanvas = Canvas(losewindow, width=700, height=500)
        lbg = PhotoImage(file="3d.png")
        losecanvas.create_image(250,175, image=lbg)
        losecanvas.create_text(250, 100, text="You Lost.", font="Times 70 bold", fill="white")

        retrybuttonimg=PhotoImage(file="retry.png")
        retrybutton_l= Button(losewindow, image=retrybuttonimg, borderwidth=0, command=retry)
        retrybutton_l.place(x=65, y=250)

        exitbuttonimg=PhotoImage(file="exit.png")
        exitbutton_l=Button(losecanvas, image= exitbuttonimg, borderwidth=0, command=exit)
        exitbutton_l.place(x=275, y=250)
        losecanvas.pack()
        while Lose is True:
            root.update()
if win is True:
    winwindow = Toplevel()
    winwindow.geometry("500x350")
    wincanvas = Canvas(winwindow, width=700, height=500)
    wbg = PhotoImage(file="brown.png")
    wincanvas.create_image(250, 175, image=wbg)
    wincanvas.create_text(250, 100, text="You Finished The Game!", font="Times 30 bold", fill="white")

    replaybuttonimg = PhotoImage(file="replay.png")
    replaybutton = Button(winwindow, image=replaybuttonimg, borderwidth=0, command=retry)
    replaybutton.place(x=45, y=245)

    exitbuttonimg = PhotoImage(file="exit.png")
    exitbutton = Button(wincanvas, image=exitbuttonimg, borderwidth=0, command=exit)
    exitbutton.place(x=275, y=250)
    wincanvas.pack()
    while win is True:
        root.update()