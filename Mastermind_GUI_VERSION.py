import tkinter as tk
import numpy as np
import sys
import os

screen = tk.Tk()
screen.title('Mastermind Game')
screen.geometry("400x600")
screen.resizable(0, 0)

colorguessed = []
colorFillCount = 0

def codemaker():
    """ generates 4 random colors for the code-maker and returns a list
    """
    colorguess = np.random.choice(['yellow','blue', 'green', 'red','magenta', 'cyan'], 4)
    nonNumpyComp = []
    for i in colorguess:
        nonNumpyComp.append(i)
    colorguess = nonNumpyComp[:]

    return colorguess

if colorFillCount == 0:
    computerColor = codemaker()

def hintColor(guesses, compCode = computerColor):
    """
    :param guesses: list--takes the user input and determine hint(black or white) based on codemarker
    :return: list -- with elements 'black' and 'white'
    """
    initialX = len(guesses) - 4
    endX = len(guesses)
    hint = []
    compCod = compCode[:]
    guess = guesses[initialX:endX]
    hint = []
    compCod = compCode[:]
    for i in range(len(guess)):
        if guess[i] == compCode[i]:
            hint.append("BLACK")
            guess[i] = 'remove'
            compCod[i] = 'jack'

    for i, j in zip(range(len(guess)), guess):
        if j in compCod:
            hint.append("WHITE")
            compCod.remove(j)

    return hint

def winDetermine(listofHint):
    """
    :param listofHint: list--to determine if the guess match the computer code
    :return: boolean--true if the color match and false o.t
    """
    allBlack = False
    if len(listofHint) == 4:
        for i in listofHint:
            if i == 'WHITE':
                return allBlack
            else:
                allBlack = True
                continue
    return allBlack

firstRowBut_height = 4
firstRowBut_width = 400
wn = tk.Frame(screen, relief='groove', borderwidth=5, bg='#DCDCDC', width=firstRowBut_width, height=firstRowBut_height)
wn.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
wn.pack(fill=tk.BOTH, expand=1)

secRowBut_height = 4
secRowBut_width = 360
wn1 = tk.Frame(screen, width=secRowBut_width, height=secRowBut_height, bg='#808080')
wn1.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
wn1.pack(fill=tk.BOTH, expand=1)

trdRowBut_height = 600-secRowBut_height-firstRowBut_height
trdRowBut_width = 400
wnCanvas = tk.Canvas(screen, height=trdRowBut_height, relief='sunken', borderwidth=7, width=trdRowBut_width, bg='#808080')
wnCanvas.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
wnCanvas.pack(fill=tk.BOTH, expand=1)

dividerHeight = 600-secRowBut_height-firstRowBut_height-70
dividerWidth = 20
dividerFrame = tk.Frame(wnCanvas, width=dividerWidth, height=dividerHeight, borderwidth=0.5, bg='#DCDCDC', relief='raised')
dividerFrame.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
dividerFrame.pack(anchor='center', expand=0)
#ttk.Separator(screen, orient='vertical')

beginLX = 25
beginTopY = 20
beginRghtX = beginLX+28
beginBotY = beginTopY+28
space = 13 #16 ideal
circleName = ['one','two','three', 'four', 'five','six','seven','eight','nine','ten',
            'eleven','twelve','thirteen','fourteen', 'fifteen','sixteen','seventeen','eighteen', 'ninteen',
            'twenty','twenty_one','twenty_two', 'twenty_three', 'twenty_four','twenty_five','twenty_six',
            'twenty_seven','twenty_eight','twenty_nine','thirty','thirty_one','thirty_two',
            'thirty_three','thirty_four','thirty_five','thirty_six','thirty_seven','thirty_eight',
            'thirty_nine', 'forty','forty_one','forty_two','forty_three','forty_four','forty_five',
            'forty_six','forty_seven','forty_eight']

circleName2 = ['forty_nine','fifty','fifty_one','fifty_two','fifty_three','fifty_four',
            'fifty_five','fifty_six','fifty_seven','fifty_eight','fifty_nine','sixty','sixty_one','sixty_two', 'sixty_three',
            'sixty_four','sixty_five','sixty_six','sixty_seven','sixty_eight','sixty_nine','seventy','seventy_one','seventy_two',
            'seventy_three','seventy_four','seventy_five','seventy_six','seventy_seven','seventy_eight','seventy_night','eighty',
            'eighty_one','eighty_two','eighty_three','eighty_four','eighty_five','eighty_six','eighty_seven','eighty_eight',
            'eighty_nine','ninty','ninty_one','ninty_two','ninty_three','ninty_four','ninty_five','ninty_six']

for j, i in zip(range(1,len(circleName)+1), circleName):
    if j % 4 == 0:
        circleName[j - 1] = wnCanvas.create_oval(beginLX, beginTopY, beginRghtX, beginBotY, outline='#696969')
        beginTopY = beginBotY+space
        beginBotY = beginTopY + 28
        beginLX = 25
        beginRghtX = beginLX + 28
    else:
        circleName[j - 1] = wnCanvas.create_oval(beginLX, beginTopY, beginRghtX, beginBotY, outline='#696969')
        beginLX = beginRghtX + space
        beginRghtX = beginLX + 28

beginLX_2 = 220
beginTopY_2 = 26
beginRghtX_2 = beginLX_2 + 20
beginBotY_2 = beginTopY_2 + 20
space_y = 20
for j, i in zip(range(1,len(circleName2)+1), circleName2):
    if j % 4 == 0:
        circleName2[j - 1] = wnCanvas.create_oval(beginLX_2, beginTopY_2, beginRghtX_2, beginBotY_2, outline='#696969')
        beginTopY_2 = beginBotY_2 + space_y
        beginBotY_2 = beginTopY_2 + 21
        beginLX_2 = 220
        beginRghtX_2 = beginLX_2 + 20
    else:
        circleName2[j - 1] = wnCanvas.create_oval(beginLX_2, beginTopY_2, beginRghtX_2, beginBotY_2, outline='#696969')
        beginLX_2 = beginRghtX_2 + space_y
        beginRghtX_2 = beginLX_2 + 20


def buttonRedClick():
    global colorguessed, colorFillCount
    wnCanvas.itemconfig(circleName[colorFillCount], fill ='red')
    colorFillCount += 1
    colorguessed.append('red')

def buttonBlueClick():
    global colorguessed, colorFillCount
    wnCanvas.itemconfig(circleName[colorFillCount], fill='blue')
    colorFillCount += 1
    colorguessed.append('blue')

def buttonGreenClick():
    global colorguessed, colorFillCount
    wnCanvas.itemconfig(circleName[colorFillCount], fill ='green')
    colorFillCount += 1
    colorguessed.append('green')

def buttonYellowClick():
    global colorguessed, colorFillCount
    wnCanvas.itemconfig(circleName[colorFillCount], fill ='yellow')
    colorFillCount += 1
    colorguessed.append('yellow')

def buttonCyanClick():
    global colorguessed, colorFillCount
    wnCanvas.itemconfig(circleName[colorFillCount], fill ='cyan')
    colorFillCount += 1
    colorguessed.append('cyan')

def buttonMagentaClick():
    global colorguessed, colorFillCount
    wnCanvas.itemconfig(circleName[colorFillCount], fill ='magenta')
    colorFillCount += 1
    colorguessed.append('magenta')

def fillHintColor(colorlist, computercol = computerColor):
    """accepts two lists, and fills the circles with appropriate colors"""
    initialX = len(colorlist)-4
    endX = len(colorlist)
    hint = hintColor(colorlist, computercol)
    if len(hint)==0:
        return
    elif len(hint)==1:
        wnCanvas.itemconfig(circleName2[initialX], fill=hint[0])
    elif len(hint)==2:
        wnCanvas.itemconfig(circleName2[initialX], fill=hint[0])
        wnCanvas.itemconfig(circleName2[initialX+1], fill=hint[1])
    elif len(hint)==3:
        wnCanvas.itemconfig(circleName2[initialX], fill=hint[0])
        wnCanvas.itemconfig(circleName2[initialX + 1], fill=hint[1])
        wnCanvas.itemconfig(circleName2[initialX + 2], fill=hint[2])
    else:
        wnCanvas.itemconfig(circleName2[initialX], fill=hint[0])
        wnCanvas.itemconfig(circleName2[initialX + 1], fill=hint[1])
        wnCanvas.itemconfig(circleName2[initialX + 2], fill=hint[2])
        wnCanvas.itemconfig(circleName2[initialX + 3], fill=hint[3])

def winMessage():
    from tkinter import messagebox
    messagebox.showinfo("WON", "Good Job, You Won!")

def loseMessage():
    from tkinter import messagebox
    messagebox.showinfo("LOST", "Sorry, you've ran out of guesses.")

def restartButton():
    """ Restarts the game by re-running the entire code"""
    python = sys.executable
    os.execl(python, python,  * sys.argv)

def checkButton():
    """determines win and call appropriate function"""
    global colorguessed, computerColor, colorFillCount
    if len(colorguessed) % 4 == 0:
        fillHintColor(colorguessed, computerColor)
        if winDetermine(hintColor(colorguessed, computerColor)):
            winMessage()
        elif colorFillCount >= 48:
            loseMessage()


buttonRestart = tk.Button(wn, text='RESTART', width=8, bg='#808080', command=restartButton)
buttonRestart.grid(row=0, column=0, padx=[345/2,398/2], pady=[5, 5])
buttonRed = tk.Button(wn1,borderwidth=1,  relief='raised', width=2, height=1, bg='red', command=buttonRedClick)
buttonBlue = tk.Button(wn1, borderwidth=1, relief='raised', width=2, height=1, bg ='blue', command=buttonBlueClick)
buttonYellow = tk.Button(wn1, borderwidth=1, relief='raised', width=2, height=1, bg='yellow', command=buttonYellowClick)
buttonGreen = tk.Button(wn1, borderwidth=1, relief='raised',width=2, height=1, bg ='green', command=buttonGreenClick)
buttonCyan = tk.Button(wn1, borderwidth=1, relief='raised', width=2, height=1, bg='cyan', command=buttonCyanClick)
buttonMagenta = tk.Button(wn1, borderwidth=1, width=2, relief='flat', height=1, bg ='magenta', command=buttonMagentaClick)
buttonCheck = tk.Button(wn1, text='CHECK', width=8, bg='#DCDCDC',fg='blue', command=checkButton)
buttonCheck.grid(row=0, column=12, padx=[135,5], pady=[5, 5])
buttonBlue.grid(row=0, column=0, padx=4)
buttonCyan.grid(row=0, column=2, padx=4)
buttonGreen.grid(row=0, column=4, padx=4)
buttonMagenta.grid(row=0, column=6, padx=4)
buttonYellow.grid(row=0, column=8, padx=4)
buttonRed.grid(row=0, column=10, padx=4)


screen.mainloop()

