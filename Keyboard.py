import tkinter as tk

from functools import partial

from tkinter import*
import tkinter
import select

keyboard_showcase = tkinter.Tk()
keyboard_showcase.title("Layout showcase")
keyboard_showcase ['bg']='powder blue'
keyboard_showcase.resizable (0,0)

def select (value):

#skriver ut space
    if value ==" Space \n":
        entry.insert(tkinter.END, ' ')

#skriver ut resten
    else:
        entry.insert(tkinter.END, value )

labell = Label (keyboard_showcase, text="", font =('arial', 30, 'bold'),
                bg ='powder blue', fg="#000000") .grid(row = 0, columnspan = 40)
entry = Text(keyboard_showcase, width=138, font =('arial', 12, 'bold'))
entry.grid(row = 1, columnspan = 40)
#import random
Optimized_layout = [
    'q\n','w\n','e\n','r\n','t\n','y\n','u\n','i\n','o\n','p\n','{\n[','}\n]',
    'a\n','s\n','d\n','f\n','g\n','h\n','j\n','k\n','l\n',':\n;',"@\n'",'~\n#',
    '|\n\\','z\n','x\n','c\n','v\n','b\n','n\n','m\n','<\n,','>\n.','?\n/',
    ' Space \n'
]

#random.shuffle(Optimized_layout)


varRow = 2
varColumn = 0

for button in Optimized_layout:
    command = lambda x= button: select(x)

    if button != " Space ":
        tkinter.Button(keyboard_showcase, text= button, width=5,padx=3,pady=3,bd=12,font =('arial', 12, 'bold'),
                        command = command) .grid(row=varRow, column = varColumn)
    #Extra utseende för space
    if button == " Space":
        
        tkinter.Button(keyboard_showcase, text= button, width = 118,
                        command = command) .grid(row=varRow, column = varColumn)
    varColumn +=1
    if varColumn > 11 and varRow == 2:
        varColumn = 0
        varRow += 1
    if varColumn > 11 and varRow == 3:
        varColumn = 0
        varRow +=1
    if varColumn > 10 and varRow == 4:
        varColumn = 0
        varRow += 1



keyboard_showcase.mainloop()