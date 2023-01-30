from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
# WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_second = SHORT_BREAK_MIN * 60
    long_break_second = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        count_down(long_break_second)
        label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_second)
        label.config(text="BREAK", fg=YELLOW)
    else:
        count_down(work_sec)
        label.config(text="Timer", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    "25:00"
    count_min = math.floor(count/60)  # Minutes
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60  # Seconds
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # Call function once after given time.
        # MS specifies the time in milliseconds
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔️"
        check_marks.config(text=marks)


 # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)


# def say_something(a, b):
#     print(a)
#     print(b)


# after() Exeutes a ommand after the time delay
# window.after(1000, say_something, "Hello", "World")


# Label
label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
label.grid(row=0, column=1)
# Canvas
canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# Button
start = Button(text="Start", command=start_timer, highlightthickness=0)
start.grid(row=2, column=0)
reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset.grid(row=2, column=2)


# Label
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
