from tkinter import *
from tkinter import ttk


window = Tk()  # root widget

# GUI size
window.geometry("740x400")
window.minsize(600, 300)
window.maxsize(740, 400)

# GUI title
window.title("Hand Gesture based Natural User Interface")

# GUI Icon
# Will enable later on.
icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
dominant = ''
right = ''
left = ''
volume = ''
brightness = ''
cancel = False
movement = ''


def okButton():
    global dominant, right, left, volume, brightness, movement
    dominant = myDominant.get()
    right = myRight.get()
    left = myLeft.get()
    volume = myVolume.get()
    brightness = myBrightness.get()
    movement = mymouse.get()
    window.destroy()


def cancelButton():
    global cancel
    cancel = True
    window.destroy()


def applyButton():
    global dominant, right, left, volume, brightness, movement
    dominant = myDominant.get()
    right = myRight.get()
    left = myLeft.get()
    volume = myVolume.get()
    brightness = myBrightness.get()
    movement = mymouse.get()


options = ["Right", "Left"]
EorD = ["Enable", "Disable"]

# Label
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

dominant_hand_label = Label(window,
                            text="Dominant Hand :",
                            font=('Helvetica',
                                  10
                                  )
                            )
dominant_hand_label.grid(row=1,
                         column=1,
                         )

myDominant = ttk.Combobox(window, value=options, width=12)
myDominant.current(0)
myDominant.grid(row=1, column=2, pady=20)

left_click_label = Label(window,
                         text="Left Click :",
                         font=('Helvetica',
                               10
                               ),
                         )

left_click_label.grid(row=2,
                      column=1,
                      )

myLeft = ttk.Combobox(window, value=EorD, width=12)
myLeft.current(0)
myLeft.grid(row=2, column=2, pady=20)

mouse_movement_label = Label(window,
                         text="Mouse Movement :",
                         font=('Helvetica',
                               10
                               ),
                         )

mouse_movement_label.grid(row=1,
                      column=5,
                      )

mymouse = ttk.Combobox(window, value=EorD, width=12)
mymouse.current(0)
mymouse.grid(row=1, column=6, pady=20)

right_click_label = Label(window,
                          text="Right Click :",
                          font=('Helvetica',
                                10
                                )
                          )

right_click_label.grid(row=2,
                       column=5,
                       )

myRight = ttk.Combobox(window, value=EorD, width=12)
myRight.current(0)
myRight.grid(row=2, column=6, pady=20)

volume_label = Label(window,
                     text="Volume :",
                     font=('Helvetica',
                           10
                           ),
                     )

volume_label.grid(row=3,
                  column=1,
                  )

myVolume = ttk.Combobox(window, value=EorD, width=12)
myVolume.current(0)
myVolume.grid(row=3, column=2, pady=20)

brightness_label = Label(window,
                         text="Brightness :",
                         font=('Helvetica',
                               10
                               )
                         )

brightness_label.grid(row=3,
                      column=5,
                      )

myBrightness = ttk.Combobox(window, value=EorD, width=12)
myBrightness.current(0)
myBrightness.grid(row=3, column=6, pady=20)

# Buttons
OK_button = Button(window,
                   text="OK",
                   padx=35,
                   command=okButton,
                   borderwidth=2
                   )
OK_button.grid(row=15, column=4, pady=20)

CANCEL_button = Button(window,
                       text="Cancel",
                       padx=25,
                       command=cancelButton,
                       borderwidth=2
                       )
CANCEL_button.grid(row=15, column=5, pady=20)

APPLY_button = Button(window,
                      text="Apply",
                      padx=27,
                      command=applyButton,
                      borderwidth=2
                      )
APPLY_button.grid(row=15, column=6, pady=20)
print(dominant)
window.mainloop()
