from tkinter import *
from tkinter import ttk

window = Tk()  # root widget

# GUI size
window.geometry("600x370")
window.minsize(600, 370)
window.maxsize(600, 370)

# GUI title
window.title("Hand Gesture based Natural User Interface")

# GUI Icon
icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)

# Global Variables
dominant = ''
right = ''
left = ''
volume = ''
brightness = ''
movement = ''
drag = ''
cancel = False

def okButton():
    global dominant, right, left, volume, brightness, movement, drag
    dominant = myDomi.get()
    right = myRight.get()
    left = myLeft.get()
    volume = myVolume.get()
    brightness = myBrightness.get()
    movement = myMouse.get()
    drag = myDrag.get()
    window.destroy()


def cancelButton():
    global cancel
    cancel = True
    window.destroy()


def applyButton():
    global dominant, right, left, volume, brightness, movement, drag
    dominant = myDomi.get()
    right = myRight.get()
    left = myLeft.get()
    volume = myVolume.get()
    brightness = myBrightness.get()
    movement = myMouse.get()
    drag = myDrag.get()

    if dominant == "Right":
        status_r = f'''\nLeft Click = {left}\nRight Click = {right}\nMouse Movement = {movement}\nDrag and Drop ={drag}\n'''
        status_l = f'''\n\nVolume Control = {volume}\nBrightness Control = {brightness}\n\n'''
    else:
        status_l = f'''\nLeft Click = {left}\nRight Click = {right}\nMouse Movement = {movement}\nDrag and Drop ={drag}\n'''
        status_r = f'''\n\nVolume Control = {volume}\nBrightness Control = {brightness}\n\n'''

    right_status = LabelFrame(info,
                              text="Right Hand",
                              font=('Helvetica',
                                    10),
                              padx=59
                              )
    right_status.grid(row=0,
                      column=0,
                      )

    left_status = LabelFrame(info,
                             text="Left Hand",
                             font=('Helvetica',
                                   10),
                             padx=59
                             )
    left_status.grid(row=0,
                     column=5,
                     )

    op_Label_1 = Label(right_status,
                       text=status_r,
                       )
    op_Label_1.grid()

    op_Label_2 = Label(left_status,
                       text=status_l,
                       )
    op_Label_2.grid()

    window.geometry("600x516")
    window.maxsize(600, 516)


# Dropdown Options
options = ["Right", "Left"]
EorD = ["Enable", "Disable"]


# OPTIONS/SELECTIONS
# Title Label
title_text_label = Label(window,
                         text="Hand Gesture based Natural User Interface",
                         font=('Helvetica',
                               20,
                               'bold'
                               )
                         )
title_text_label.grid(columnspan=7,
                      padx=10,
                      pady=10
                      )

# Dominant Hand
dominant_hand_label = Label(window,
                            text="Dominant Hand :",
                            font=('Helvetica',
                                  10
                                  )
                            )
dominant_hand_label.grid(row=1,
                         column=1,
                         )

myDomi = StringVar()
myDomi.set(options[0])

Radiobutton(window, text="Right", variable=myDomi, value=options[0]).grid(row=1, column=2, pady=20)
Radiobutton(window, text="Left", variable=myDomi, value=options[1]).grid(row=1, column=4, pady=20)

# Mouse Movement
mouse_movement_label = Label(window,
                             text="Mouse Movement :",
                             font=('Helvetica',
                                   10
                                   ),
                             )

mouse_movement_label.grid(row=2,
                          column=1,
                          )

myMouse = ttk.Combobox(window, state="readonly", value=EorD, width=12)
myMouse.current(0)
myMouse.grid(row=2, column=2, pady=20)

# Drag and Drop
drag_n_drop_label = Label(window,
                          text="Drag and Drop :",
                          font=('Helvetica',
                                10
                                )
                          )

drag_n_drop_label.grid(row=2,
                       column=5,
                       )

myDrag = ttk.Combobox(window, state="readonly", value=EorD, width=12)
myDrag.current(0)
myDrag.grid(row=2, column=6, pady=20)

# Left Click
left_click_label = Label(window,
                         text="Left Click :",
                         font=('Helvetica',
                               10
                               ),
                         )

left_click_label.grid(row=3,
                      column=1,
                      )

myLeft = ttk.Combobox(window, state="readonly", value=EorD, width=12)
myLeft.current(0)
myLeft.grid(row=3, column=2, pady=20)

# Volume
volume_label = Label(window,
                     text="Volume :",
                     font=('Helvetica',
                           10
                           ),
                     )

volume_label.grid(row=3,
                  column=5,
                  )

myVolume = ttk.Combobox(window, state="readonly", value=EorD, width=12)
myVolume.current(0)
myVolume.grid(row=3, column=6, pady=20)

# Right Click
right_click_label = Label(window,
                          text="Right Click :",
                          font=('Helvetica',
                                10
                                )
                          )

right_click_label.grid(row=4,
                       column=1,
                       )

myRight = ttk.Combobox(window, state="readonly", value=EorD, width=12)
myRight.current(0)
myRight.grid(row=4, column=2, pady=20)

# Brightness
brightness_label = Label(window,
                         text="Brightness :",
                         font=('Helvetica',
                               10
                               )
                         )

brightness_label.grid(row=4,
                      column=5,
                      )

myBrightness = ttk.Combobox(window, state="readonly", value=EorD, width=12)
myBrightness.current(0)
myBrightness.grid(row=4, column=6, pady=20)

# BUTTONS
OK_button = Button(window,
                   text="OK",
                   padx=35,
                   command=okButton,
                   borderwidth=2
                   )
OK_button.grid(row=10, column=4, pady=20)

CANCEL_button = Button(window,
                       text="Cancel",
                       padx=25,
                       command=cancelButton,
                       borderwidth=2
                       )
CANCEL_button.grid(row=10, column=5, pady=20)

APPLY_button = Button(window,
                      text="Apply",
                      padx=27,
                      command=applyButton,
                      borderwidth=2
                      )
APPLY_button.grid(row=10, column=6, pady=20)

# STATUS BAR
info = LabelFrame(window,
                  text="Status",
                  font=('Helvetica',
                        10,
                        'bold')
                  )
info.grid(columnspan=7,
          row=12,
          column=1,
          padx=5,
          pady=5,
          )

window.mainloop()
