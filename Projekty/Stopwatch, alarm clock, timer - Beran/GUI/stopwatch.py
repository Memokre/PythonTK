#from GUI import *
#
#from tkinter import Label,Button
from tkinter.ttk import Label,Button

from .root import root
from Controls import start,stop,restart
from Controls import stp

def start_stopwatch():
    restart()
    root.children['start_stopwatch'].configure(state = 'disabled')
    start()

def stop_stopwatch():
    root.children['start_stopwatch'].configure(state = 'normal')
    stop()


def stopwatchWidgets():
    """Display stopwatch labels and buttons"""
    
    Label(root, text="Stopwatch",font=('arial',30,'bold'),background="dimgray",foreground='black').pack(anchor = 'center')
    Label(root, text='0:0:0',font=('arial',30,'bold'),foreground='green',background="black",width=6).place(x=110,y=260)
    button1=Button(root,text="Start",command=start_stopwatch, name='start_stopwatch').place(x=100,y=230)
    button2=Button(root,text="Stop",command=stop_stopwatch, name='stop_stopwatch').place(x=180,y=230)