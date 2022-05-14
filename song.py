from cProfile import label
import pywhatkit
from tkinter import *
import tkinter.messagebox
import requests 
# s = input('Enter a song : ')
# pywhatkit.playonyt(s)

tk = Tk()
tk.title('Online songs')
tk.geometry('500x300')
label = Label(tk, text='Enter the song :',font=('bold',12))
label.place(x=150,y=70)
songtext = StringVar()
songentry = Entry(tk, textvariable=songtext).place(x=150,y=100)

def searchsong():
    song = songtext.get()
    pywhatkit.playonyt(song)

searchbutton = Button(tk, text='Search',width=12, command=searchsong).place(x=150,y=150)

tk.mainloop()