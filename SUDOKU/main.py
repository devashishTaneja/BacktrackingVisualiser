from tkinter import *
import tkinter.font as tkFont
from PIL import Image,ImageTk
from time import *
def draw(top,sud,r,c):
	if(sud[r][c]==0):
		t="    "
	else:
		t=" "+str(sud[r][c])+" "
	fontStyle = tkFont.Font(family="Lucida Grande", size=20)
	Label(top, text=t,borderwidth=1,relief="solid",font=fontStyle,width=3).grid(row=r,column=c)
	

def main():
	sud = [[8, 1, 0, 0, 3, 0, 0, 2, 7], 
            [0, 6, 2, 0, 5, 0, 0, 9, 0], 
            [0, 7, 0, 0, 0, 0, 0, 0, 0], 
            [0, 9, 0, 6, 0, 0, 1, 0, 0], 
            [1, 0, 0, 0, 2, 0, 0, 0, 4], 
            [0, 0, 8, 0, 0, 5, 0, 7, 0], 
            [0, 0, 0, 0, 0, 0, 0, 8, 0], 
            [0, 2, 0, 0, 1, 0, 7, 5, 0], 
            [3, 8, 0, 0, 7, 0, 0, 4, 2]]

	top=Tk()
	top.geometry('500x400')
	start = Image.open('start.png')
	start = start.resize((70, 30))
	start = ImageTk.PhotoImage(start)
	close = Image.open('close.png')
	close = close.resize((30, 30))
	close = ImageTk.PhotoImage(close)
	st_btn = Button(top,image=start,command=lambda:solve(sud,top)).grid(row=12,column=0,columnspan=10,sticky=W)
	cl_btn = Button(top,image=close,command=top.destroy).grid(row=12,column=2,columnspan=10,sticky=W)
	empty_row = Label(top, text='	').grid(row=10,column=0,columnspan=10)
	for r in range(9):
		for c in range(9):
			draw(top,sud,r,c)
	top.mainloop()

def empty(sud):
	for i in range(9):
		for j in range(9):
			if(sud[i][j]<1):
				return (i,j)
	return None

def isValid(sud,k,x,y):
	for i in range(9):
		if(sud[i][y]==k):
			return False

	for i in range(9):
		if(sud[x][i]==k):
			return False

	a=x//3
	b=y//3
	for i in range(a*3,a*3+3):
		for j in range(b*3,b*3+3):
			if(sud[i][j] == k):
				return False
	return True


def solve(sud,top):
	# print("working")
	
	pos = empty(sud)

	if not pos:
		# draw(top,sud)
		print("Solution Exists")
		return True
	else:
		x=pos[0]
		y=pos[1]
		# print("point ")
		# print(x)
		# print(y)

	for i in range(1,10):
		if(isValid(sud,i,x,y)):
			sud[x][y]=i
			draw(top,sud,x,y)
			top.update()
			if(solve(sud,top)):
				return True
			sud[x][y]=0
			draw(top,sud,x,y)
			top.update()

	# print("No solution")

	return False

if(__name__ == '__main__'):
		main()