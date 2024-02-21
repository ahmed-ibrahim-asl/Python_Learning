import tkinter as tk
import ttkbootstrap as ttk


root_window = tk.Tk()
root_window.title('Entry')
root_window.geometry('255x90')


# 2. entry
entry = ttk.Entry(
    master=root_window,
    font=('Calibri', 15, 'bold')
)
entry.pack()


root_window.mainloop()
