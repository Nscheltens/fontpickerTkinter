#=============================
#   Font Picker
#=============================

import tkinter as tk
from tkinter import ttk
from tkinter import font

mainWin = tk.Tk()
mainWin.title("Font Picker")

mainFrame = tk.Frame(mainWin)

def updateText(self):
    print(fontPick_chosen.current(), fontPick_chosen.get())
    print(fontSize_chosen.current(), fontSize_chosen.get())
    sampleFont.configure(family=fontPick_chosen.get())
    sampleFont.configure(size=fontSize_chosen.get())
    sampleFont.configure(weight=isBold())
    sampleFont.configure(slant=isSlant())
    sampleFont.configure(underline=isUnderline())
    sampleFont.configure(overstrike=isOverstrike())
    mainWin.update()

def textCall():
    sampleFont.configure(weight=isBold())
    sampleFont.configure(slant=isSlant())
    sampleFont.configure(underline=isUnderline())
    sampleFont.configure(overstrike=isOverstrike())

def isBold():
    if(checkVarB.get()):
        return 'bold'
    else:
        return 'normal'
def isSlant():
    if(checkVarI.get()):
        return 'italic'
    else:
        return 'roman'
def isUnderline():
    if(checkVarU.get()):
        return True
    else:
        return False
def isOverstrike():
    if(checkVarO.get()):
        return True
    else:
        return False

startFrame = tk.Frame(mainFrame)
startFrame.grid(column=0, row=0)

a_comboLabel = ttk.Label(startFrame, text="Pick a Font style:")
a_comboLabel.grid(column=0,row=0)
fontPick = tk.StringVar()
fontPick_chosen = ttk.Combobox(startFrame, width=32, textvariable=fontPick, state='readonly')
fontPick_chosen['values'] = font.families()
fontPick_chosen.grid(column=0, row=1)
fontPick_chosen.current(0)

b_comboLabel = ttk.Label(startFrame, text="Pick a Font size:")
b_comboLabel.grid(column=1,row=0)
fontSize = tk.StringVar()
fontSize_chosen = ttk.Combobox(startFrame, width=8, textvariable=fontSize, state='readonly')
fontSize_chosen['values'] = list(range(4, 43))
fontSize_chosen.grid(column=1, row=1)
fontSize_chosen.current(10)

sampleTextLabel = ttk.Label(mainFrame, text="Text to be displayed")
sampleTextLabel.grid(column=0, row=2)

restFrame = tk.Frame(mainFrame)
restFrame.grid(column=0, row=1)

sampleText = tk.StringVar()
sampleText.set('SampleText')
sampleText_entered = ttk.Entry(mainFrame, width=24, textvariable=sampleText)
sampleText_entered.grid(column=0, row=3)

checkVarB = tk.IntVar()
checkVarI = tk.IntVar()
checkVarU = tk.IntVar()
checkVarO = tk.IntVar()
text = ['Bold', 'Italics', 'Underline', 'Overstrike']

curRad = tk.Checkbutton(restFrame, text=text[0], variable=checkVarB, command=textCall)
curRad.grid(column=0, row=0, sticky=tk.W)
curRad = tk.Checkbutton(restFrame, text=text[1], variable=checkVarI, command=textCall)
curRad.grid(column=1, row=0, sticky=tk.W)
curRad = tk.Checkbutton(restFrame, text=text[2], variable=checkVarU, command=textCall)
curRad.grid(column=2, row=0, sticky=tk.W)
curRad = tk.Checkbutton(restFrame, text=text[3], variable=checkVarO, command=textCall)
curRad.grid(column=3, row=0, sticky=tk.W)

SampleLabelFrame = ttk.LabelFrame(mainFrame, text=' The Sample Text ')
SampleLabelFrame.grid(column=0, row=4)

sampleFont = font.Font(family=fontSize_chosen.get(),size=fontSize_chosen.get())

sampleLabel = ttk.Label(SampleLabelFrame)
sampleLabel['textvariable'] = sampleText
sampleLabel['font'] = sampleFont
sampleLabel.grid(column=0, row=0)

fontPick_chosen.bind("<<ComboboxSelected>>", updateText)
fontSize_chosen.bind("<<ComboboxSelected>>", updateText)

mainFrame.pack()
mainWin.mainloop()