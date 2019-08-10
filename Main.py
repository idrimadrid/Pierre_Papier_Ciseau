from tkinter import *
from tkinter import messagebox
from random import randrange


def action(action):
    global player
    if (action == "papier"):
        player.config(text="p", image=papier, height=150, width=150)
    elif (action == "pierre"):
        player.config(text="r", image=pierre, height=150, width=150)
    else:
        player.config(text="s", image=ciseau, height=150, width=150)
    genaction()


def genaction():
    global cpu
    i = randrange(1, 3)
    if (i == 1):
        cpu.config(text="p", image=papier, height=150, width=150)
    elif (i == 2):
        cpu.config(text="r", image=pierre, height=150, width=150)
    else:
        cpu.config(text="s", image=ciseau, height=150, width=150)
    winner()


def winner():
    global player_score
    global cpu_score
    global player
    global cpu
    if (player.cget("text") == cpu.cget("text")):
        result = "Tie"
    elif (player.cget("text") == "p" and cpu.cget("text") == "r" or player.cget(
            "text") == "s" and cpu.cget("text") == "p" or player.cget("text") == "r" and cpu.cget(
        "text") == "s"):
        player_score += 1
        result = "You Won"
    else:
        cpu_score += 1
        result = "CPU Won"
    update_score()
    messagebox.showinfo("finish", str(result))


def update_score():
    global cpu_score
    global player_score
    global footer
    global header
    header.config(text="\nCPU : " + str(cpu_score))
    footer.config(text="Player : " + str(player_score) + "\n\nChoose One Move :\n")


base = Tk()
base.title("Pierre - Papier - Ciseau")
base.geometry("550x550")
base.resizable(0, 0)
# images import
pierre = PhotoImage(file="Pierre.png")
papier = PhotoImage(file="Papier.png")
ciseau = PhotoImage(file="Ciseau.png")
cpu_score = 0
player_score = 0
top_frame = Frame(base)
top_frame.pack(side=TOP)
mid_frame = Frame(base)
mid_frame.pack()
bot_frame = Frame(base)
bot_frame.pack(side=BOTTOM)

header = Label(top_frame, text="\nCPU : " + str(cpu_score))
header.pack()
cpu = Label(mid_frame)
cpu.pack(side=TOP)
player = Label(mid_frame)
player.pack(side=BOTTOM)
footer = Label(bot_frame, text="Player : " + str(player_score) + "\n\nChoose One Move :\n")
footer.pack(side=TOP)
Pa = Button(bot_frame, image=papier, height=95, width=95, command=lambda: action("papier"))
# Pa.bind('<Button-1>', winner)
Pa.pack(side=LEFT)
Ro = Button(bot_frame, image=pierre, height=95, width=95, command=lambda: action("pierre"))
# Ro.bind('<Button-1>', winner)
Ro.pack(side=LEFT)
Sc = Button(bot_frame, image=ciseau, height=95, width=95, command=lambda: action("ciseau"))
# Sc.bind('<Button-1>', winner)
Sc.pack(side=LEFT)

base.mainloop()
