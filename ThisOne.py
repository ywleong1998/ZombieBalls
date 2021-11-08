from tkinter import *
from tkinter import Tk, Label, Button
from menupage import*

class SuiBian:
    cincai = False
    def __init__(self, master):
        self.master = master
        master.title("Zombie Balls")
        master.geometry("1920x1080")
        self.label = Label(master, text="This is my projectile ball game applying collision detection for Mini Project")
        self.label.pack()
        self.greet_button = Button(master, text="Enter my game", command=self.byebye)
        self.greet_button.place(width=200, height=50, x=665, y=250)
        self.close_button = Button(master, text="Close because this is too simple", command=master.quit)
        self.close_button.place(width=200, height=50, x=665, y=550)
    def byebye(self):
        root.destroy()
        SuiBian.cincai = True
root = Tk()
canvas = Canvas(root, width = 19290, height = 1080)
canvas.pack()
img = PhotoImage(file="background1.png")
canvas.create_image(20,20, anchor=NW, image=img)
my_game = SuiBian(root)
root.mainloop()
if SuiBian.cincai:
    GG = MenuGame()
    GG.Menuing()