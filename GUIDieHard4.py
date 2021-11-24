# GUIDieHard4.py

from tkinter import *
import threading
import pygame
import time


pygame.mixer.init()
def play():
	# playsound('sound1.mp3')
	pygame.mixer.music.load("search.mp3")
	pygame.mixer.music.play(loops=0)


def playThread():
	task = threading.Thread(target=play)
	task.start()

GUI = Tk()
GUI.geometry('500x700')
GUI.state('zoomed')
GUI.title('โปรแกรม Dashboard Die Hard 4.0')

# COLOR
bg = '#2b2b2b'
fg = '#00ff08'

WW = 1920
WH = 1080

GUI.configure(background=bg)


# Fullscreen
GUI.attributes('-fullscreen',False)
GUI.bind('<F11>', lambda event: GUI.attributes('-fullscreen', not GUI.attributes('-fullscreen')))
GUI.bind('<Control-f>', lambda event: GUI.attributes('-fullscreen', not GUI.attributes('-fullscreen')))
GUI.bind('<Control-q>', lambda event: GUI.destroy())

# FONT
f1 = ('Sprite Coder',20,'bold')
f2 = ('Sprite Coder',15,'bold')

# CANVAS
canvas = Canvas(GUI,width=WW, height=WH, background=bg, bd=0, relief='ridge',highlightthickness=0)
canvas.place(x=0,y=0)

def MyFrame(x,y,width=300,height=100):
	frame1 = canvas.create_rectangle(0,0,width,height,fill=bg, outline=fg, width=2)
	canvas.move(frame1,x,y)


def FixedLabel(text='THIS IS A TEXT',x=50,y=50,font=f1, color=fg):
	L1 = Label(GUI, text=text, font=font, bg=bg, fg=color,justify=LEFT)
	L1.place(x=x,y=y)

# F1
MyFrame(20,20)
FixedLabel('MY COIN',50,100)
FixedLabel('โปรแกรมของลุง',50,200,font=('Angsana New',20,'bold'),color='yellow')


# IoT Frame
MyFrame(20,300,300,200)
FixedLabel('IoT-Device 1',25,280,font=f2)
FixedLabel('TEMP ( C ): 30\nHUMID (%): 55\nSTATUS: OK',25,320,font=f2)

# IoT Frame
MyFrame(20,600,300,200)
FixedLabel('IoT-Device 2',25,580,font=f2)
FixedLabel('TEMP ( C ): 30\nHUMID (%): 55\nSTATUS: OK',25,620,font=f2)

# CHECK STOCK
MyFrame(500,20,500,200)
FixedLabel('THAI STOCK',520,10,font=f2)

v_stockname = StringVar() #StringVar ตัวแปรสำหรับใช้กับ GUI

E1 = Entry(GUI, textvariable=v_stockname, font=f1,bg=bg,fg=fg)
E1.configure(insertbackground=fg) # cursor color
E1.configure(highlightthickness=2,highlightbackground=fg,highlightcolor=fg)
E1.place(x=570,y=40)

v_result = StringVar()
v_result.set('MY STOCK: 50 BAHT')

LResult = Label(GUI, textvariable=v_result, font=f1, bg=bg, fg=fg, justify=LEFT)
LResult.place(x=570,y=80)


from uncleengineer import thaistock
# ['BANPU ', '11.50', '+0.40', '+3.60%', '25/11/2021 00:19:57']
def CheckStockPrice(event):
	playThread()
	try:
		stockname = v_stockname.get()
		print(stockname)
		result = thaistock(stockname)
		text = 'STOCK: {}\nPRICE: {}\nCHANGE: {}\n%CHANGE: {}'.format(result[0],result[1],result[2],result[3])
		v_result.set(text)
	except:
		v_result.set('NOT FOUND')

E1.bind('<Return>',CheckStockPrice)

GUI.mainloop()