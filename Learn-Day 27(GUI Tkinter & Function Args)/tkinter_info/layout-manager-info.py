###### Layout Manager##########
# pack() # It is difficult to specify a precise position
# place() # Its all about precise positioning
# Example: place(x=0,y=0)
# grid() # It imagines that the entire program is grid and we can divide it into any number of rows and column that we want
# Example: grid(column=0, row=0) # We can't mix up the pack() and grid() at the same application

from tkinter import *

window = Tk()
window.title("Some Challenges")
window.minsize(width=600, height=300)
# Adding padding around all of the element in the window
window.config(padx=20, pady=20)

# Label
my_label = Label()
my_label.config(text="GUI", padx=10)
my_label.grid(row=0, column=0)

# Button
button = Button()
button.config(text="Button Here")
button.grid(row=1, column=1)
button1 = Button()
button1.config(text=" New Button Here")
button1.grid(row=0, column=2)

# Entry
input = Entry()
input.insert(END, "Hallelujah")
input.grid(row=2, column=3)

window.mainloop()
