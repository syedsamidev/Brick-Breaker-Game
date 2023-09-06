from tkinter import *

help = Tk()
help.title("Brick Breaker Game")
help.iconbitmap("icon.ico")
help.geometry("700x500")



canvas = Canvas(help,width=700,height=500)
bg = PhotoImage(file="brown.png")
canvas.create_image(350,250,image=bg)

text = canvas.create_text(170,30,text="Instructions :",font=("Times 40 Bold",35),fill="blue")

txt1 = canvas.create_text(390,80,text="Don't let the ball hit the boundary below the",font = ("Times 20 Bold",18),fill="white")

txt2 = canvas.create_text(340,120,text="paddle otherwise you'll lose the game,Try to break as",font = ("Times 20 Bold",18),fill="white")

txt3 = canvas.create_text(336,170,text="much bricks as you can to Score High. When all the",font = ("Times 20 Bold",18),fill="white")

txt4 = canvas.create_text(340,220,text=" bricks on the screen are finished, you'll win the game!",font = ("Times 20 Bold",18),fill="white")

txt5 = canvas.create_text(355,270,text="There are different difficulty levels,which you can choose",font = ("Times 20 Bold",18),fill="white")

txt6 = canvas.create_text(340,320,text="according to the experience you have with the game.",font = ("Times 20 Bold",18),fill="white")

txt7 = canvas.create_text(135,360,text="Cheats :",font = ("Times 40 Bold",35),fill="blue")

txt8 = canvas.create_text(275,410,text="Press "+"'"+"I"+"'"+" button to make the ball solid." ,font = ("Times 20 Bold",18),fill="white")

txt9 = canvas.create_text(340,440,text="Press "+"'"+"O"+"'"+" button to make shield under the paddle." ,font = ("Times 20 Bold",18),fill="white")

txt10 = canvas.create_text(265,470,text="Press "+"'"+"P"+"'"+" button to undo the cheats." ,font = ("Times 20 Bold",18),fill="white")


canvas.pack()

mainloop()


