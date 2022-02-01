# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
import pandas
import random

# ---------------------------- GLOBAL CONSTANTS AND VARIABLES ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_to_learn = []

# ---------------------------- READ FROM CSV AND CONVERT TO LIST OF DICTIONARIES ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/german_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")


# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    known_btn.config(state=DISABLED)
    unknown_btn.config(state=DISABLED)
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)
    known_btn.config(state=ACTIVE)
    unknown_btn.config(state=ACTIVE)


def known_word():
    words_to_learn.remove(current_card)
    pandas.DataFrame(words_to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Learn Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_img, highlightthickness=0, command=next_card, state=DISABLED)
unknown_btn.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_btn = Button(image=check_img, highlightthickness=0, command=known_word, state=DISABLED)
known_btn.grid(row=1, column=1)

# ---------------------------- FUNCTION CALLS ------------------------------- #
next_card()
window.mainloop()
