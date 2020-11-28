from tkinter import *
import tkinter.font as tkFont
from PIL import Image,ImageTk
from time import *
def draw(top,maze,R,C,cur,dst):
	for r in range(R):
		for c in range(C):
			fontStyle = tkFont.Font(family="Lucida Grande", size=20)
			if(maze[r][c]==2):
				t="    "
				Label(top, text=t,borderwidth=0,relief="solid",bg = 'red',font=fontStyle,width=3).grid(row=r,column=c)
			elif(maze[r][c]==0):
				t="    "
				Label(top, text=t,borderwidth=0,relief="solid",bg = 'black',font=fontStyle,width=3).grid(row=r,column=c)
			else:
				if(r==cur[0] and c==cur[1]):
					Label(top, image=rat,borderwidth=0,relief="solid",width=50,height=34).grid(row=r,column=c)
				elif(r==dst[0] and c==dst[1]):
					Label(top, image=close,borderwidth=0,relief="solid",width=50,height=34).grid(row=r,column=c)
				else:
					t="    "
					if(maze[r][c]==3):
						Label(top, text=t,borderwidth=0,relief="solid",bg = 'green',font=fontStyle,width=3).grid(row=r,column=c)
					else:
						Label(top, text=t,borderwidth=0,relief="solid",font=fontStyle,width=3).grid(row=r,column=c)
	

def main():
	# maze = [
		# [1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ],
		# [1 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,0 ],
		# [1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ],
		# [1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ],
		# [1 ,1 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ],
		# [0 ,0 ,1 ,0 ,0 ,1 ,1 ,0 ,0 ,1 ,0 ,1 ,1 ],
		# [1 ,0 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ],
		# [0 ,0 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ],
		# [1 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ],
		# [0 ,0 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,0 ,0 ],
		# [0 ,1 ,0 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,0 ,1 ],
		# [0 ,0 ,1 ,1 ,1 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ]]

	maze = [
		[1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ],
		[1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,0 ],
		[1 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ],
		[1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ],
		[1 ,1 ,1 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,0 ,0 ,1 ],
		[0 ,0 ,1 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ],
		[0 ,0 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ],
		[0 ,0 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,1 ],
		[1 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ],
		[1 ,0 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,0 ,1 ],
		[0 ,0 ,0 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,0 ,1 ],
		[0 ,0 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ]]
	cur = [0,0]
	dst = [11,12]
	R = len(maze)
	C = len(maze[0])
	top=Tk()
	top.geometry('1100x900')
	global start
	start = Image.open('start.png')
	start = start.resize((50,30))
	start = ImageTk.PhotoImage(start)
	global rat
	rat = Image.open('rat.jpg')
	rat = rat.resize((30,30))
	rat = ImageTk.PhotoImage(rat)
	global close
	close = Image.open('dst.png')
	close = close.resize((30, 30))
	close = ImageTk.PhotoImage(close)
	st_btn = Button(top,image=start,command=lambda:solve(maze,top,cur,dst,R,C)).grid(row=22,column=0,columnspan=10,sticky=W)
	cl_btn = Button(top,image=close,command=top.destroy).grid(row=22,column=2,columnspan=10,sticky=W)
	empty_row = Label(top, text='	').grid(row=10,column=0,columnspan=10)

	draw(top,maze,R,C,cur,dst)

	top.mainloop()


def isValid(pos,R,C,maze):
	x=pos[0]
	y=pos[1]
	if(x<0 or x>=R or y<0 or y>=C):
		return False
	if(maze[x][y]==0 or maze[x][y]==2 or maze[x][y]==3):
		return False
	# print("ok",x,y,maze[x][y])
	return True


def solve(maze,top,cur,dst,R,C):
	maze[cur[0]][cur[1]]=3
	draw(top,maze,R,C,cur,dst)
	#top.update()
	if(cur==dst):
		draw(top,maze,R,C,cur,dst)
		#top.update()
		print("destination reached")
		return 1

	nxt=cur

	# RIGHT
	nxt[1]=nxt[1]+1
	if(isValid(nxt,R,C,maze)):
		if(solve(maze,top,nxt,dst,R,C)==1):
			return 1
		else:
			maze[nxt[0]][nxt[1]]=2
	nxt[1]=nxt[1]-1
	draw(top,maze,R,C,cur,dst)
	#top.update()

	# DOWN
	nxt[0]=nxt[0]+1
	if(isValid(nxt,R,C,maze)):
		if(solve(maze,top,nxt,dst,R,C)==1):
			return 1
		else:
			maze[nxt[0]][nxt[1]]=2
	nxt[0]=nxt[0]-1
	draw(top,maze,R,C,cur,dst)
	#top.update()

	# LEFT
	nxt[1]=nxt[1]-1
	if(isValid(nxt,R,C,maze)):
		if(solve(maze,top,nxt,dst,R,C)==1):
			return 1
		else:
			maze[nxt[0]][nxt[1]]=2
	nxt[1]=nxt[1]+1
	draw(top,maze,R,C,cur,dst)
	#top.update()

	# UP
	nxt[0]=nxt[0]-1
	if(isValid(nxt,R,C,maze)):
		if(solve(maze,top,nxt,dst,R,C)==1):
			return 1
		else:
			maze[nxt[0]][nxt[1]]=2
	nxt[0]=nxt[0]+1
	draw(top,maze,R,C,cur,dst)
	#top.update()

	return 0

if(__name__ == '__main__'):
		main()