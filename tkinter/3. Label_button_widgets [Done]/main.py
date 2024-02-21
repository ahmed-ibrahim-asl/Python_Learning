import tkinter as tk
from tkinter import ttk


def root_window():
    window_root = tk.Tk()
    window_root.title('Label widget')

    # return the width, height of your screen
    screen_width = window_root.winfo_screenwidth()
    screen_height = window_root.winfo_screenheight()

    # syntax ('widthxheigh+leftPos+topPos')

    window_width = 600
    window_height = 400
    leftPos = int(screen_width/2 - window_width/2)
    topPos = int(screen_height/2 - window_height/2)

    window_root.geometry(f'{window_width}x{window_height}+{leftPos}+{topPos}')

    #!!!!! working Label widget

    label = ttk.Label(
        # setting parent which going to host that widget
        master=window_root,

        # Set the text you want to display
        text="Some text",

        # font arg, syntax: font=(TypeFont, size, normal/bold/italic)
        # font=('Calibri', 24, 'bold italic')
        font=('Calibri', 24, 'bold')

        # set color for text to black
        # foreground="black"    - (another valid syntax) fg="black"

        # set color for background to white
        # background="white"    - (another valid syntax) bg="white"
    )

    # Think of pack method: As you telling python interpreter, pack label widget inside there master
    # pack method parameters:
    # pady  - y-axis margin
    # padx  - x-axis margin
    #! side - A bit advanced Topic
    '''
        
        side argument used to specify the side of the parent widget against which the child 
        widget should be aligned

        #!{RIGTH, LEFT}
        - we going to refer '[ ]'  as root window
        - pack1 -> (1), pack2 -> (2)
        let's say we have 2 widgets first one is set to LEFT, with respect to window
        [(1)         ]

        and if we set it to LEFT again for (2)
        [(1) (2)]
        RIGHT is same 

        #!{TOP, BOTTOM}
        Thinking of TOP and BOTTOM in terms of the order of adding widgets
        
        [or think of it like that ]
        side=TOP will always stack from the top downwards in the order they are packed, 
        and widgets packed with side=BOTTOM will stack from the bottom upwards in the order
        they are packed.

        #! Example
        label1.pack(side=TOP)
        label2.pack(side=BOTTOM)
        label3.pack(side=TOP)
        label4.pack(side=BOTTOM)
        label5.pack(side=TOP)
        label6.pack(side=BOTTOM)
    
        Top of the window
        -------------------
        [label1]
        [label3]
        [label5]
        
        [label6]
        [label4]
        [label2]
        -------------------
        Bottom of the window


    '''
    # ? Note: pack method respect the order of calling
    # label1.pack() -> label2.pack() -> label3.pack()
    # result:
    #       label1
    #       label2
    #       label3
    label.pack()

    window_root.mainloop()


root_window()
