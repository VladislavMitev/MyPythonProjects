from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ("Courier", 12, "normal")


# ---------------------------- SEARCH DATA ------------------------------- #
def search_data():
    try:
        with open("data.json", "r") as data_file:
            # Reading the saved data
            saved_data = json.load(data_file)
    except FileNotFoundError:  # If the file doesn't exist, generate a messagebox showing an error message
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        searched_website = website_entry.get().title()  # Get user's input in title case
        if searched_website in saved_data:
            messagebox.showinfo(title=f"{searched_website}", message=f"Email/Username: "
                                                                     f"{saved_data[searched_website]['username']}\n"
                                                                     f"Password: "
                                                                     f"{saved_data[searched_website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {searched_website} exist.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    # Join list items into a string
    generated_password = "".join(password_list)
    # Insert the generated password into the password entry
    password_entry.insert(0, generated_password)
    # Copy the generated password to the clipboard automatically
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get().title()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    # Checking if there are empty entries
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")
    else:
        details_are_ok = messagebox.askokcancel(title="These are the entered details", message=f"Website: {website}\n"
                                                                                           f"Email/Username: {username}"
                                                                                           f"\nPassword: {password}\n\n"
                                                                                           f"Do you want to save them?")
        if details_are_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
                    # Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:  # If the file doesn't exist, create the file and write the new_data
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:  # If the file does exist, open it and save the updated data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:  # Clear the entries
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:", font=FONT)
username_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=34)
website_entry.grid(row=1, column=1)
username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Buttons
search_btn = Button(text="Search", width=14, highlightthickness=0, command=search_data)
search_btn.grid(row=1, column=2)
password_btn = Button(text="Generate Password", highlightthickness=0, command=generate_password)
password_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=44, highlightthickness=0, command=save)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()
