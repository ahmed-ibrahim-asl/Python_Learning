#   Main {} for creating any tkinter application
#   1. Import tkinter
#   2. Functions of custom actions of buttons
#   3. Windows in your app
#       3.1 Intialize root window
#       3.2 Configure root window
#   4. Start the main root window


#! 1. Import tkinter
import tkinter as tk
from tkinter import ttk

#! for fixing path problem
import os
###############################################


#! 2. Functions for custom actions of buttons
# def buttonName_actionName():
#    pass
##############################################


#! 3. Windows in your app
# ? why i am seprating it into functions ?
# To ease move between windows

# ? First Window is main or called root_window

#! 3.1 Intialize root window
def root_window():
    window_root = tk.Tk()

    #! 3.2 Configure root window
    window_root.title("Demo Program")

    # geometry, iconbitmap, minsize, maxsize, resizable
    # winfo_screenwidth, winfo_screenheight
    # attributes
    ########################################################
    # ? Goal is to set icon
    current_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(current_dir, 'assets', 'rocket_logo.ico')

    window_root.iconbitmap(icon_path)

    ########################################################
    # ? Goal is to set diemention of program and make the program
    # starts in the middle of screen

    # return the width, height of your screen
    screen_width = window_root.winfo_screenwidth()
    screen_height = window_root.winfo_screenheight()

    # syntax ('widthxheigh+leftPos+topPos')

    window_width = 600
    window_height = 400
    leftPos = int(screen_width/2 - window_width/2)
    topPos = int(screen_height/2 - window_height/2)

    window_root.geometry(f'{window_width}x{window_height}+{leftPos}+{topPos}')
    ########################################################
    # ?  Goal is to disable the user from resize window
    # (x-axis, y-axis)
    window_root.resizable(False, False)
    ########################################################
    # ? Goal is to set max width and height a user can set
    # window_root.maxsize(800, 700)
    ########################################################
    # ? Goal is to set min width and heigh a user can set
    # To prevent user from missing looks of the program
    # window_root.minsize(150, 300)
    ########################################################
    # ? Goal Make our app the toppest program in the screen
    # ? Note: there still other configurations can be set with
    # ?       attributes method
    window_root.attributes('-topmost', True)

    #! 4. Start the main root window
    # Tkinter start event loop which listen for events such as
    # (mouse clicks, keyboard input, etc...)

    window_root.mainloop()


root_window()
