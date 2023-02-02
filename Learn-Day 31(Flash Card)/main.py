from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# print(to_learn)


################## Functions #####################
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas_card.itemconfig(title, text="French", fill="black")
    canvas_card.itemconfig(word, text=current_card["French"], fill="black")
    canvas_card.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas_card.itemconfig(title, text="English", fill="white")
    canvas_card.itemconfig(
        word, text=current_card["English"], fill="white")
    canvas_card.itemconfig(card_background, image=card_back)


################## Creating The CSV ###############
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
################## /Creating The CSV ##############

################## /Functions #####################


################## User Window #####################
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
################## Canvas Card #####################
canvas_card = Canvas(width=800, height=526,
                     highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_background = canvas_card.create_image(400, 263, image=card_front)
title = canvas_card.create_text(400, 150,
                                font=("Ariel", 40, "italic"))
word = canvas_card.create_text(400, 263,
                               font=("Ariel", 60, "bold"))
# canvas_card.create_text(text="Word")
canvas_card.grid(row=0, column=0, columnspan=2)
################## /Canvas Card #####################
################## Button Cross #####################
wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0,
                      bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)
################## /Button Cross ####################
################## Button Right #####################
right = PhotoImage(file="./images/right.png")
right_button = Button(image=right, highlightthickness=0,
                      bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)
################## /Button Right ####################

next_card()

window.mainloop()
################## /User Window #####################
