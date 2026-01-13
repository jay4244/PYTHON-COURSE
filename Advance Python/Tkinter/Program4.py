from tkinter import *

screen = Tk()
screen.geometry("500x500")
screen.configure(bg="#b39ddb")
screen.title("Rock Paper Scissor Game")

def mychoice(userchoice):
    print(userchoice)

title = Label(screen,text="ROCK PAPER SCISSOR GAME",font=('Arial', 14, 'bold'),bg="#b39ddb")
title.pack()

btnRock = Button(screen,text="ROCK",bg="#2196f3",fg="white",width=10,height=2,font=('Arial', 10, 'bold'), command=lambda: mychoice("Rock"))
btnRock.place(x=10,y=50)

btnPaper = Button(screen,text="PAPER",bg="#2196f3",fg="white",width=10,height=2,font=('Arial', 10, 'bold'),command=lambda: mychoice("Paper"))
btnPaper.place(x=180,y=50)

btnScissor = Button(screen,text="SCISSOR",bg="#2196f3",fg="white",width=10,height=2,font=('Arial', 10, 'bold'),command=lambda: mychoice("Scissor"))
btnScissor.place(x=350,y=50)

screen.mainloop()
