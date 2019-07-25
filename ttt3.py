from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import collections
# Global Variables

ActivePlayer=1
p2=[] #What player 1 selected
p1=[] #What player 2 selected
players = p1, p2
window=Tk()
window.title("Tic Tac Toe :Player X")
style=ttk.Style()
style.theme_use('classic')

# Add Buttons
bu1=ttk.Button(window, text=' ')
bu1.grid(row=0, column=0, sticky='snew', ipadx=50, ipady=50)
bu1.config(command=lambda: ButtonClick(1))

bu2=ttk.Button(window, text=' ')
bu2.grid(row=0, column=1, sticky='snew', ipadx=50, ipady=50)
bu2.config(command=lambda: ButtonClick(2))

bu3=ttk.Button(window, text=' ')
bu3.grid(row=0, column=2, sticky='snew', ipadx=50, ipady=50)
bu3.config(command=lambda: ButtonClick(3))

bu4=ttk.Button(window, text=' ')
bu4.grid(row=1, column=0, sticky='snew', ipadx=50, ipady=50)
bu4.config(command=lambda: ButtonClick(4))

bu5=ttk.Button(window, text=' ')
bu5.grid(row=1, column=1, sticky='snew', ipadx=50, ipady=50)
bu5.config(command=lambda: ButtonClick(5))

bu6=ttk.Button(window, text=' ')
bu6.grid(row=1, column=2, sticky='snew', ipadx=50, ipady=50)
bu6.config(command=lambda: ButtonClick(6))

bu7=ttk.Button(window, text=' ')
bu7.grid(row=2, column=0, sticky='snew', ipadx=50, ipady=50)
bu7.config(command=lambda: ButtonClick(7))

bu8=ttk.Button(window, text=' ')
bu8.grid(row=2, column=1, sticky='snew', ipadx=50, ipady=50)
bu8.config(command=lambda: ButtonClick(8))

bu9=ttk.Button(window, text=' ')
bu9.grid(row=2, column=2, sticky='snew', ipadx=50, ipady=50)
bu9.config(command=lambda: ButtonClick(9))

def ButtonClick(id):
	global ActivePlayer
	global p2
	global p1
	if(ActivePlayer==1):
		SetLayout(id, "X")
		p1.append(id)
		window.title("Tic Tac Toe :Player X")
		CheckWiner()
		CheckTie()
		ActivePlayer=2
	elif(ActivePlayer==2):
		SetLayout(id, "O")
		p2.append(id)
		window.title("Tic Tac Toe :Player O")
		CheckWiner()
		ActivePlayer=1

def SetLayout(id,PlayerSymbol):

	if id==1:
		bu1.config(text=PlayerSymbol)
		bu1.state(['disabled'])

	elif id==2:
		bu2.config(text=PlayerSymbol)
		bu2.state(['disabled'])

	elif id==3:
		bu3.config(text=PlayerSymbol)
		bu3.state(['disabled'])

	elif id==4:
		bu4.config(text=PlayerSymbol)
		bu4.state(['disabled'])

	elif id==5:
		bu5.config(text=PlayerSymbol)
		bu5.state(['disabled'])

	elif id==6:
		bu6.config(text=PlayerSymbol)
		bu6.state(['disabled'])

	elif id==7:
		bu7.config(text=PlayerSymbol)
		bu7.state(['disabled'])

	elif id==8:
		bu8.config(text=PlayerSymbol)
		bu8.state(['disabled'])

	elif id==9:
		bu9.config(text=PlayerSymbol)
		bu9.state(['disabled'])

def CheckWiner():
	winer=-1
	if((  1 in p1) and (2 in p1) and (3 in p1)):
		winer=1
	if((  1 in p2) and (2 in p2) and (3 in p2)):
		winer=2

	if((  4 in p1) and (5 in p1) and (6 in p1)):
		winer=1
	if((  4 in p2) and (5 in p2) and (6 in p2)):
		winer=2

	if((  7 in p1) and (8 in p1) and (9 in p1)):
		winer=1
	if((  7 in p2) and (8 in p2) and (9 in p2)):
		winer=2

	if((  1 in p1) and (4 in p1) and (7 in p1)):
		winer=1
	if((  1 in p2) and (4 in p2) and (7 in p2)):
		winer=2

	if((  2 in p1) and (5 in p1) and (8 in p1)):
		winer=1
	if((  2 in p2) and (5 in p2) and (8 in p2)):
		winer=2

	if((  3 in p1) and (6 in p1) and (9 in p1)):
		winer=1
	if((  3 in p2) and (6 in p2) and (9 in p2)):
		winer=2

	if((  3 in p1) and (5 in p1) and (7 in p1)):
		winer=1
	if((  3 in p2) and (5 in p2) and (7 in p2)):
		winer=2

	if((  1 in p1) and (5 in p1) and (9 in p1)):
		winer=1
	if((  1 in p2) and (5 in p2) and (9 in p2)):
		winer=2

	if winer==1:
		messagebox.showinfo(title="Congratulations", message="Player 'X' is the winer")
		window.destroy()
	elif winer==2:
		messagebox.showinfo(title="Congratulations", message="Player 'O' is the winer")
		window.destroy()

def CheckTie():
	global p1
	tie = len(p1)
	if tie == 5:
		messagebox.showinfo(title="Tie", message="It's a tie")
		window.destroy()

window.mainloop()
