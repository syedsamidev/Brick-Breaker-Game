from tkinter import *
import os
from winsound import PlaySound, SND_LOOP, SND_ASYNC


root2 = Tk()
root2.title("The Brick Breaker Game")
root2.iconbitmap("icon.ico")
root2.geometry("700x500")
canvas = Canvas(root2,width=700,height=500)
bg = PhotoImage(file="stars.png")
canvas.create_image(350,250,image=bg)
canvas.create_text(350,100,text="Select The Difficulty Level",font=("Times 80 Bold",35),fill="white")

def open():
    root2.destroy()
    os.system('python games.py')
def open1():
    root2.destroy()
    os.system('python gameseasy.py')

def open2():
    root2.destroy()
    os.system('python gamesnormal.py')
    PlaySound("bgm.wav", SND_LOOP | SND_ASYNC)


btn1 = PhotoImage(file="easy btn.png")
button_1 = Button(canvas,image=btn1,borderwidth=0,command=open1)
button_1.place(x=100,y=300)
btn2 = PhotoImage(file="normal btn.png")
button_2 = Button(canvas,image=btn2,borderwidth=0,command=open2)
button_2.place(x=300,y=300)
btn3 = PhotoImage(file="hard btn.png")
button_3 = Button(canvas,image=btn3,borderwidth=0,command=open)
button_3.place(x=500,y=300)

canvas.pack()

mainloop()
