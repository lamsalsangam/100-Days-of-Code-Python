# https://tcl.tk/man/tcl8.6.13/TkCmd/entry.htm

import tkinter

# This is Equivalent to the Screen in the turtle.
window = tkinter.Tk()

# For the title bar of the application
window.title("My First GUI Program")
# Sizing of the window
# If defined the sizing will go to the value defined below otherwise,
# The defaukt size will keep on accomodating with the content inside the application window
window.minsize(width=500, height=300)

# Label
# my_label = tkinter.Label(text="I am the Label")  # Component
my_label = tkinter.Label(text="I am the Label",
                         font=("Arial", 18))  # Component
# my_label = tkinter.Label(text="I am the Label", font=("Arial", 24, "italic"))  # Component
# my_label = tkinter.Label(text="I am the Label", font=("Arial", 24, "bold"))  # Component


# Describing how the component should be laid out on the screen
# If you donot the pack the given component it will not show in the screen
# my_label.pack()  # It will place the label into the screen and automatiocally center it into the screen which is default
# ['left', 'right', 'top', 'bottom']
# my_label.pack(side="left")  # Center Left
# my_label.pack(side="bottom") # Center Bottom
# my_label.pack(side="right") # Center Right
# my_label.pack(expand = True) # it will take the entire height and width available of the screen(center)
my_label.pack()  # Center Top

# my_label["text"] = "Some GUI Thing"  # here only one attribute can be set
# my_label.config(text="GUI Thing")  # multiple attribute can be set


# Buttons
def button_clicked():
    print("Calculated")
    user_input = input.get()
    my_label.config(text=user_input)


# command is the attribute allocated for the callback function
button = tkinter.Button(text="Calculate", command=button_clicked)  # Components
button.pack()


# Entry

input = tkinter.Entry()  # it sets the input field
# input.config(width=15)
input.pack()
# get() will help in getting hold of the value that came from the input field
# user_input = input.get()


# This is equivalent to the exit on click on the turtle
# Example  # while True:    #     listening... # it keeps on holding to the window and keeps on listening to see if there is any thing else the user is going to do
window.mainloop()
