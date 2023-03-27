import tkinter as tk
from tkinter import filedialog
import os

def calculate_size():
    # Prompt the user to select a file
    file_path = filedialog.askopenfilename()
    # Calculate the file size in bytes
    file_size = os.path.getsize(file_path)
    # Convert the file size to a human-readable format
    units = ('B', 'KB', 'MB', 'GB', 'TB')
    size = file_size
    for unit in units:
        if size < 1024:
            break
        size /= 1024
    size_str = '{:.2f} {}'.format(size, unit)
    # Display the file size in the GUI
    size_label.config(text=size_str)

# Create a Tkinter window
root = tk.Tk()
root.title('File Size Calculator')

# Create a button to prompt the user to select a file
select_button = tk.Button(root, text='Select File', command=calculate_size)
select_button.pack(pady=10)

# Create a label to display the file size
size_label = tk.Label(root, text='')
size_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
