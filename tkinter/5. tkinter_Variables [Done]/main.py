import tkinter as tk
from tkinter import ttk


# create the window and configure it
root_window = tk.Tk()
root_window.title('Tkinter variables')
root_window.geometry('255x90')
root_window.resizable(False, False)

''' tkinter variables '''
# Number -  tk.IntVar()
# String -  tk.StringVar()
# Boolean - tk.BooleanVar()

string_var = tk.StringVar()


''' tkinter functions '''


def action():
    print(f"Content of entry: {string_var.get()}")

    # Now we can rest the content
    string_var.set('')


''' Placing Widgets 💃 '''

# 1. label widget
label = ttk.Label(master=root_window, text='Label', textvariable=string_var)
label.pack()


# 2. entry
entry = ttk.Entry(master=root_window, textvariable=string_var)
entry.pack()


# 3. button
button = ttk.Button(master=root_window, command=action, text='Print & Reset')
button.pack(pady=6)


# run the window
root_window.mainloop()
