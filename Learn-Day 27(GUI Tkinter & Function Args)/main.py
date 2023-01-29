from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=600, height=500)
window.config(padx=50, pady=50)


def button_used():
    user_input = int(input.get())
    result = round(user_input * 1.60934, 2)
    output.config(text=result)


# Entry
input = Entry()
input.insert(END, 0)
input.grid(row=0, column=1)
# input.config()

# Label
miles = Label(text="Miles")
miles.grid(row=0, column=2)

# Label
my_label = Label(text="is equal to")
my_label.grid(row=1, column=0)

# Label
output = Label(text="0")
output.grid(row=1, column=1)

# Label
km = Label(text="Km")
km.grid(row=1, column=2)

# Button
button = Button(text="Calculate", command=button_used)
button.grid(row=2, column=1)

window.mainloop()
