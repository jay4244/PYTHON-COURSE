from tkinter import *

screen = Tk()

screen.geometry("500x500")
screen.title("Dexter")
screen.configure(bg="#b39ddb")

lbl = Label(
    screen,
    text="Welcome to my app",
    font=("Arial", 26, "bold"),
    fg="white",
    bg="#b39ddb"
)
lbl.pack()

screen.mainloop()
