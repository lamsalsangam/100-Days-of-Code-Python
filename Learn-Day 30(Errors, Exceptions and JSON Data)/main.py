from tkinter import *
from tkinter import messagebox
import json
import random
import pyperclip
# json.dump() >>>> Write
# json.load() >>>> Read
# json.update() >>>> Update
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

    random.shuffle(password)
    generated_password = "".join(password)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}
    # if not website or not email or not password:
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave the field empty")

    ####### Standard Dialog #######
    # messagebox.showinfo(title="Title", message="Message")
    else:
        # is_ok = messagebox.askokcancel(
        #     title=website, message=f"These are the details entered: \nEmail: {email}\n Password:{password}\n Is it ok to save?")
        # if is_ok:
        # with open("data.txt", "a") as data_file:
        try:
            with open("data.json", "r") as data_file:
                # data_file.write(f"{website} | {email} | {password}\n")
                # json.dump(new_data, data_file)
                # Reading the old data
                data = json.load(data_file)  # Read "r"
                # print(type(data))
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)  # Write
        else:
            # Updating the old data with the new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)  # Write
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- GET PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for the {website} exists.")

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
website_entry = Entry(width=30)
website_entry.focus()
website_entry.grid(row=1, column=1)
# Button
website_button = Button(text="Search", command=find_password, width=14)
website_button.grid(row=1, column=2)
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