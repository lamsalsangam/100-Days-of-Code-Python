from tkinter import *

# Window
window = Tk()
window.title("Widgets Examples")
window.minsize(width=500, height=300)


# function


def button_clicked():
    my_label.config(text=input.get())


# Label
my_label = Label()
my_label.config(text="Widgets Scenarios")
my_label.pack()

# Button
button = Button()
button.config(text="Do Something", command=button_clicked)
button.pack()

# Entry
input = Entry()
# Add some text to begin with
input.insert(END, string="Hallelujah")
input.pack()

# TEXT
# >>>> Multiple line text entry box
text = Text(height=5, width=30)
# text.focus()  # it will create the first focus point in the application
text.insert(END, "Example of the multiline text entry.")
# 1.0 refers to get the hold of the text starting from the first line from the character 0
print(text.get("1.0", END))
text.pack()

# Spinbox


def spinbox_used():
    # gets the current value of the spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale >>>> Slider


def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton >>>> Checkbox


def checkbutton_used():
    # Print 1 if the button is checked ,0 if not
    print(checked_state.get())


# Variable to hold on to checked state, 0 is off, 1 is on
checked_state = IntVar()
checkbutton = Checkbutton(
    text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# >>>> Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold onto which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1,
                           variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option1", value=2,
                           variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
# List box of the choices >>>> Listbox


def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
