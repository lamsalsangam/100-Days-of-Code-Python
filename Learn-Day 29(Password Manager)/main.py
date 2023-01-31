from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password = password_letters+password_numbers+password_symbols
    # for i in range(nr_letters):
    #     password.append(random.choice(letters))
    # for i in range(nr_symbols):
    #     password.append(random.choice(symbols))
    # for i in range(nr_numbers):
    #     password.append(random.choice(numbers))

    random.shuffle(password)
    generated_password = "".join(password)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    if not website or not email or not password:
        messagebox.showinfo(
            title="Oops", message="Please don't leave the field empty")

    ####### Standard Dialog #######
    # messagebox.showinfo(title="Title", message="Message")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail: {email}\n Password:{password}\n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=40)

# Image >>>> Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

###### Entry and Label#####
###########################
# Label
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
# Entry
website_entry = Entry(width=48)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
###########################
# Label
email_username_label = Label(text="Email/Username")
email_username_label.grid(row=2, column=0)
# Entry
email_username_entry = Entry(width=48)
email_username_entry.insert(0, "shadow@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2)
###########################
# Label
password_label = Label(text="Password")
password_label.grid(row=3, column=0)
# Entry
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)
# Button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)
###########################
# Button
add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
