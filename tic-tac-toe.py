from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox
app = Tk()

app.title("TIC TAC TOE")

player_a = StringVar()
player_b = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(app, textvariable=p1, bd = 5)
player1_name.grid(row=1, column=1, columnspan=6)
player2_name = Entry(app, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=6)

bclick = True
flag = 0

def disablebutton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)
    
def clickbutton(buttons):
    global bclick, flag, player2_name, player1_name, player_b, player_a
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        player_b = p2.get() + " " + " Wins!"
        player_a = p1.get() + " " + " Wins!"
        checkForWin()
        flag += 1

    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1

    else:
        tkinter.messagebox.showinfo("TIC TAC TOE", "Button Already Clicked")

def checkForWin():
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        disablebutton()
        tkinter.messagebox.showinfo("TIC TAC TOE", player_a)

    elif (flag == 8):
        tkinter.messagebox.showinfo("TIC TAC TOE", "GAME OVER")

    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
          button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
          button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
          button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
          button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
          button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
          button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
          button3["text"] == "0" and button5["text"] == "O" and button7["text"] == "O"):
        disablebutton()
        tkinter.messagebox.showinfo("TIC TAC TOE", player_b)

buttons = StringVar()

label = Label(app, text = "Player 1:", font = "Arial 20 bold", bg = "White", fg = "Black", height = 1, width = 8)
label.grid(row=1, column=0)

label = Label(app, text = "Player 2:", font = "Arial 20 bold", bg = "White", fg = "Black", height = 1, width = 8)
label.grid(row=2, column=0)

label = Label(app, text = "X", font = "Arial 20 bold", fg = "red")
label.grid(row=1, column=2)

label = Label(app, text = "O", font = "Arial 20 bold", fg = "red")
label.grid(row=2, column=2)

button1 = Button(app, text = " ", font = "Arial 30 bold", bg = "Purple", fg = "yellow", height = 3, width = 6, command=lambda: clickbutton(button1))
button1.grid(row=3, column=0)

button2 = Button(app, text = " ", font = "Arial 30 bold", bg = "Purple", fg = "yellow", height = 3, width = 6, command=lambda: clickbutton(button2))
button2.grid(row=3, column=1)

button3 = Button(app, text = " ", font = "Arial 30 bold", bg = "Purple", fg = "yellow", height = 3, width = 6, command=lambda: clickbutton(button3))
button3.grid(row=3, column=2)

button4 = Button(app, text = " ", font = "Arial 30 bold", bg = "Purple", fg = "yellow", height = 3, width = 6, command=lambda: clickbutton(button4))
button4.grid(row=4, column=0)

button5 = Button(app, text = " ", font = "Arial 30 bold", bg = "Purple", fg = "yellow", height = 3, width = 6, command=lambda: clickbutton(button5))
button5.grid(row=4, column=1)

button6 = Button(app, text = " ", font = "Arial 30 bold", bg = "purple", fg = "yellow", height = 3, width = 6, command=lambda: clickbutton(button6))
button6.grid(row=4, column=2)

button7 = Button(app, text = " ", font = "Arial 30 bold", bg = "Purple", fg = "yellow", height = 3, width = 6, command=lambda: clickbutton(button7))
button7.grid(row=5, column=0)

button8 = Button(app, text = " ", font = "Arial 30 bold", bg = "Purple", fg = "yellow", height = 3, width = 6, command=lambda: clickbutton(button8))
button8.grid(row=5, column=1)

button9 = Button(app, text = " ", font = "Arial 30 bold", bg = "Purple", fg = "yellow", height = 3, width = 6, command=lambda: clickbutton(button9))
button9.grid(row=5, column=2)

app.mainloop()

