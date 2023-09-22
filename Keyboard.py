
    #Python3
import tkinter as tk

from functools import partial

from tkinter import*
import tkinter

keyboard_showcase = tkinter.Tk()
keyboard_showcase.title("Kayboard Layout")
keyboard_showcase ['bg']='powder blue'
keyboard_showcase.resizable (0,0)

labell = Label (keyboard_showcase, text="Keyboard Layout", font =('arial', 30, 'bold'),
                bg ='powder blue', fg="#000000") .grid(row = 0, columnspan = 40)
entry = Text(keyboard_showcase, width=138, font =('arial', 10, 'bold')) .grid(row = 1, columnspan = 40)

keyboard_layout = [
    'q','w','e','r','t','y','u','i','o','p',
    'a','s','d','f','g','h','j','k','l',
    'z','x','c','v','b','n','m',
    ' Space '
]
varRow = 2
varColumn = 0


for button in keyboard_layout:
    command = lambda x= button: select(x)
    if button != " Space":
        tkinter.Button(keyboard_showcase, text= button,
                        command = command) .grid(row=varRow, column = varColumn)

    if button != " Space":
        tkinter.Button(keyboard_showcase, text= button,
                        command = command) .grid(row=varRow, column = varColumn)

    varColumn +=1
    if varColumn > 15 and varRow == 2:
        varColumn = 0
        varRow +=1

    if varColumn > 15 and varRow == 3:
        varColumn = 0
        varRow +=1

keyboard_showcase.mainloop()