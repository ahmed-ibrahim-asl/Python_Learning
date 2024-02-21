'''
Event Binding in tkinter,
Mechanism that allows you to connect an event
(ex. Keyboard input, Mouse click/motion, widgets selected/unselected) to a function or widget.
'''


import tkinter as tk
from tkinter import ttk


root_window = tk.Tk()
root_window.title('Event Binding')
root_window.geometry('500x500')

''' Placing Widgets 💃 '''
'''
1. Widget.bind(event, functionToBe)
    event Format: [ modifier - type - detail ]
                    Alt      - Keypress - a 
'''

multi_text = tk.Text(master=root_window)
multi_text.pack()

entry = ttk.Entry(master=root_window)
entry.pack(pady=5)

button = ttk.Button(master=root_window, text="click Me")
button.pack(pady=5)

######### Let's bind stuff #########

# root_window.bind('<KeyPress>', lambda x: print(f'Pressed Key is {x}'))
# root_window.bind('<KeyPress>', lambda x: print(f'Pressed Key is {x.char}'))

# root_window.bind('<Motion>', lambda event: print(f'x: {event.x}  y: {event.y}'))

entry.bind('<FocusIn>', lambda event: button.config(text="Final step"))
entry.bind('<FocusOut>', lambda event: button.config(text="click me"))

root_window.mainloop()
