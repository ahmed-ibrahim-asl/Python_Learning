import tkinter as tk


def miles_kiloMeters_converter(miles, output_var):

    # print(miles.get())

    try:

        kilometers = miles.get() * 1.60934
        output_var.set(f"{miles.get()} Miles = {kilometers:.2f} Kilometers")

    except tk.TclError:
        output_var.set("Please set valid Number")


''' Windows contained within our application '''


def window_root():
    ''' 2. Intialize Root Window'''
    window_root = tk.Tk()
    window_root.title("Demo_Program")

    # window_root.resizable(x-axis, y-axis)
    window_root.resizable(False, False)

    ''' 3. Configure root window '''
    horizontal_offset = window_root.winfo_screenwidth() // 2
    vertical_offset = int(window_root.winfo_screenheight() * 0.2)
    window_root.geometry(
        '300x150+' + str(horizontal_offset) + '+' + str(vertical_offset))

    ##########################################################################################
    ''' Start Placing widgets which would make up our program '''
    # widgets are accessed from {ttk}

    # +-------------------------------------+
    # |                Label                |
    # +-------------------------------------+
    title_label = tk.Label(
        master=window_root,

        # Set the string you want to display
        text='Miles to Kilometers',

        # Set the text color to black
        foreground="black",

        # Set the text color to white
        # background="white",

        # font(TypeFont, size, normal/bold/italic)
        font=('Calibri', 24, 'bold italic')

    ).pack()

    # As we were telling label widget to pack yourself inside your master
    # you can pass to it arguments for padding and addjustments (side, padx, pady)
    # title_label.pack()

    # +-------------------------------------+
    # |                frame                |
    # +-------------------------------------+

    # Here I am defining a frame to group widgets to ease adjusting them in the main window
    # I am going to place up comming widgets inside that frame and set master of the frame to be root
    # window

    # userInput_frame = tk.Frame(master=window_root)
    userInput_frame = tk.Frame(master=window_root)

    # +------------------------------------+
    # |                Entry               |
    # +------------------------------------+

    # we need to have variable to store values from that entry
    # Tkinter classes that provide a way to manage widget values more dynamically.

    user_entry_int = tk.IntVar()
    output_string = tk.StringVar()

    user_entry = tk.Entry(
        master=userInput_frame,
        textvariable=user_entry_int)

    # +-------------------------------------+
    # |                Button               |
    # +-------------------------------------+
    convert_button = tk.Button(

        master=userInput_frame,
        text="Convert",



        # since command argument does not directly accept arguments for the function we can use lambda functions :)
        # command=miles_kiloMeters_converter

        command=lambda: miles_kiloMeters_converter(
            user_entry_int, output_string)

    )

    # user_entry.pack()
    # convert_button.pack()
    # userInput_frame.pack()

    convert_button.pack(side='left')
    user_entry.pack(side='left', padx=10)
    userInput_frame.pack(pady=10)

    #######################################
    #               Output                #
    #######################################

    # output_label = tk.Label(
    #     master=window_root,
    #     text='Output',
    #     font=('Calibri', 15))

    # # output_label.pack()
    # output_label.pack(pady=5)

    # ? Can I make output dynamic ?

    # output_string = tk.StringVar()     # look for this line up 👆, in entry section

    output_label = tk.Label(
        master=window_root,
        text='Output',
        font=('Calibri', 15),
        textvariable=output_string

    )

    # output_label.pack()
    output_label.pack(pady=5)

    # Notice that textVariable overWrite text

    ##########################################################################################
    ##########################################################################################
    ##########################################################################################
    ''' 4. run root window '''
    # you start the Tkinter event loop, which listens for events (such as mouse clicks, keyboard input, etc.)
    # and handles them accordingly.
    # - run the app -
    window_root.mainloop()
#################################################


window_root()
