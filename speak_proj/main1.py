import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os


root=Tk()
root.title("Speak")
root.geometry("1000x500")
root.resizable(False,False)
root.configure(bg="#00FFFF")

#===================================================================================================================================
eng=pyttsx3.init()

def speak_m():
	text=txt_ara.get(1.0,END)
	speed=sped_cmbx.get()
	voices=eng.getProperty('voices')

	eng.setProperty('voice',voices[0].id)
	eng.say(text)
	eng.runAndWait()

	if(text):
		if(speed=='Fast'):
			eng.setProperty('rate',250)
		elif(speed=='Normal'):
			eng.setProperty('rate',150)
		else:
			eng.setProperty('rate',60)
			


def speak_f():
	text=txt_ara.get(1.0,END)
	speed=sped_cmbx.get()
	voices=eng.getProperty('voices')

	eng.setProperty('voice',voices[1].id)
	eng.say(text)
	eng.runAndWait()

	if(text):
		if(speed=='Fast'):
			eng.setProperty('rate',250)
		elif(speed=='Normal'):
			eng.setProperty('rate',150)
		else:
			eng.setProperty('rate',60)
	


def download():pass







#===================================================================================================================================
tp_frm=Frame(root,bg="white",width=1000,height=100)
tp_frm.place(x=0,y=0)

lg=PhotoImage(file="logo.png")

lbl1=Label(tp_frm,image=lg,bg="white")
lbl1.place(x=50,y=0)


lbl2=Label(tp_frm,image=lg,bg="white")
lbl2.place(x=840,y=0)



Label(tp_frm,text="CONVERTER TO SPEECH",font="arial 30 bold",bg="white",fg="#FF1493").place(x=240,y=30)




#---------------------------------------------------------------------

txt_ara=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
txt_ara.place(x=10,y=110,width=700,height=380)

sped_cmbx=Combobox(root,values=['Fast','Normal','Slow'],font="arial 16",state='r',width=15)
sped_cmbx.place(x=750,y=150)

Label(root,text='SPEED',font="arial 17 bold",bg="#00FFFF",fg="#FF4040").place(x=795,y=110)



m_btn1=Button(root,text="Male Speak",width=14,font="arial 17 bold",command=speak_m)
m_btn1.place(x=750,y=215)

f_btn2=Button(root,text="Female Speak",width=14,font="arial 17 bold",command=speak_f)
f_btn2.place(x=750,y=290)


s_btn2=Button(root,text="Download Audio",width=14,font="arial 17 bold",command=download)
s_btn2.place(x=750,y=380)







root.mainloop()