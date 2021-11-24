from tkinter import *
from uncleengineer import thaistock
from playsound import playsound
import threading
import pygame
import time


pygame.mixer.init()
def play():
	# playsound('sound1.mp3')
	pygame.mixer.music.load("sound1.mp3")
	pygame.mixer.music.play(loops=0)


def playThread():
	task = threading.Thread(target=play)
	task.start()

#COLOR
bg='#000304'
# fg='#075178'
fg='#1a9900'
wt='#FFFFFF'
W=1920
H=1080

GUI = Tk()
GUI.geometry('500x500')
GUI.state('zoomed')
GUI.title('Uncle Crypto Check')
GUI.configure(background=bg)

GUI.bind('<F12>',lambda x: GUI.destroy())
GUI.bind('<Control-x>',lambda x: GUI.destroy())

GUI.attributes("-fullscreen", True)
GUI.bind("<F11>", lambda event: GUI.attributes("-fullscreen",not GUI.attributes("-fullscreen")))
GUI.bind("<Control-z>", lambda event: GUI.attributes("-fullscreen",not GUI.attributes("-fullscreen")))


FONT = 'Computer Pixel-7'
f1 = (FONT,20)
f0 = (FONT,15)

canvas = Canvas(GUI, width=W, height=H, bd=0, relief='ridge', highlightthickness=0)
canvas.configure(background=bg)
canvas.place(x=0,y=0)

a = canvas.create_rectangle(10, 10, W-45, H-45, fill=bg, outline=fg ,width=2)
canvas.move(a, 20, 20)

def text(x,y,text='this is a text',font=f1,textvariable=None):
	if textvariable != None:
		L = Label(GUI,textvariable=textvariable,font=font,bg=bg,fg=wt,justify=LEFT)
	else:
		L = Label(GUI,text=text,font=font,bg=bg,fg=wt,justify=LEFT)
	L.place(x=x,y=y)

def rect(x,y,W,H,title=None):
	a = canvas.create_rectangle(0, 0, x+W, y+H, fill=bg, outline=fg ,width=2)
	canvas.move(a, x, y)
	if title != None:
		text(x+10,y-10,title,font=f0)



text1 = StringVar()
text1.set('BTC: 0.0005\nETH: 0.5\nDOGE: 18005')
rect(50,50,300,100,'THAI STOCK')
text(60,60,textvariable=text1)


def textflow():
	try:
		t = ''
		c = thaistock(etext.get())
		for tt in c:
			t+=tt+'\n'
			text1.set(t)
			time.sleep(0.7)
		#text = '{}: {}\nCHANGE: {}\n%-CHANGE: {}\nUPDATE: {}'.format(c[0],c[1],c[2],c[3],c[4])
		#text1.set(text)
	except:
		text1.set(etext.get() + ' not found')



def settext(event=None):
	playThread()
	task2 = threading.Thread(target=textflow)
	task2.start()
	

etext = StringVar()
E1 = Entry(GUI,highlightthickness=2,font=f1,textvariable=etext)
E1.configure(background=bg,foreground=wt)
E1.configure(insertbackground='white')
E1.configure(highlightbackground=fg,highlightcolor=fg)
E1.place(x=50,y=220)

E1.bind('<Return>',settext)

###

def clock():
    string = time.strftime('%H:%M:%S')
    lbl.config(text = string)
    lbl.after(1000, clock)
 

lbl = Label(GUI, font = ('impact', 40, 'bold'),
            background = bg,
            foreground = 'white')

lbl.place(x=500,y=100)
clock()

GUI.mainloop()