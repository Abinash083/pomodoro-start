from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
NoOfLoop = 0
Timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(Timer)
    title_level.config(text="Timer", fg=GREEN)
    mark_level.config(text="")
    canvas.itemconfig(time, text="00:00")
    global NoOfLoop
    NoOfLoop = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global NoOfLoop
    NoOfLoop += 1
    if NoOfLoop % 8 == 0:
        time_in_second = LONG_BREAK_MIN * 60
        title_level.config(text="BREAK", fg=RED)
    elif NoOfLoop % 2 == 1:
        time_in_second = WORK_MIN * 60
        title_level.config(text="WORK", fg=GREEN)
    elif NoOfLoop % 2 == 0:
        time_in_second = SHORT_BREAK_MIN * 60
        title_level.config(text="BREAK", fg=PINK)

    timer(time_in_second)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer(count):
    sec = int(count % 60)
    minute = (count - sec) / 60

    if sec < 10:
        sec = f"0{sec}"

    new_time = f"{int(minute)} : {sec}"

    canvas.itemconfig(time, text=new_time)
    if count >= 0:
        global Timer
        Timer = window.after(1000, timer, count - 1)
    else:
        check = ""
        Nooftick = math.floor(NoOfLoop / 2) + 1
        for i in range(Nooftick):
            check += "✓"
        mark_level.config(text=check)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Timer")
window.config(padx=50, pady=30, bg=YELLOW)

title_level = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_level.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
my_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 113, image=my_image)
time = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

st_button = Button(text="Start", highlightthickness=0, command=start_timer)
st_button.grid(column=0, row=2)

rs_button = Button(text="Reset", highlightthickness=0, command=reset)
rs_button.grid(column=2, row=2)

mark_level = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
mark_level.grid(column=1, row=3)

window.mainloop()
