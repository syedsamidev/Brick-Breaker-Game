from tkinter import *
import os
from winsound import PlaySound,SND_LOOP,SND_ASYNC


PlaySound("bgm.wav",SND_LOOP|SND_ASYNC)

def run():
    root1.destroy()
    os.system('python menu2.py')

def help1():
    
    os.system('python help.py')

root1 = Tk()
root1.title("Brick Breaker Game")
root1.iconbitmap("icon.ico")
root1.geometry("700x500")
bg = PhotoImage(file="7.png")
lbl = Label(root1,image=bg)
lbl.place(x=0, y=0, relwidth=1, relheight=1)



text1 = Label(root1,text="Brick Breaker Game", font=("Italian Bold",40),fg="white",bg="black")
text1.pack(pady=20)

btn_image = PhotoImage(file="play btn.png")
btn = Button(root1,image=btn_image, borderwidth=0, command=run)
btn.pack(pady=100)
btn_helpimg = PhotoImage(file="helpp.png")
btn_help = Button(root1,image=btn_helpimg,borderwidth=0,command=help1)
btn_help.place(x=650,y=457)



mainloop()
