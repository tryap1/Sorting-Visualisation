import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
from bubble import bubble_sort
from merge import merge_sort
from selection import select_sort
from quick import quick_sort
data = []



def visualise(data,color):
    #set graph constraints
    canvash = 425
    canvasw = 1150
    barwidth = canvasw/(len(data)+1)
    offset = 5
    spacing = 2
    normalise = [i/max(data) for i in data]
    graph_canvas.delete('all')
    for sizecounter, height in enumerate(normalise):
        #Prepare retangle values

        xtl = (sizecounter*barwidth)+offset +spacing
        ytl = canvash - (height*400)
        xbr = ((sizecounter+1)*barwidth) + offset
        ybr = canvash

        graph_canvas.create_rectangle(xtl,ytl,xbr,ybr,fill = color[sizecounter])

    parent.update_idletasks()

def generate():
    global data
    min =0
    max = 12000
    try:
        size = int(sizeentry.get())
    except:
        size = 30


    if size > 700 or size < 3:
        size = 50


    data = []
    for i in range(size):
        data.append(random.randrange(min, max+1))

    visualise(data,['#E8DAEF' for x in range(len(data))])

def sort():
    global data
    if not data:
        return
    print("Selected Algorithm:" + option1.get())
    if algoslec.get() == 'Bubble Sort':
        bubble_sort(data,visualise,float(timeslec.get()))

    if algoslec.get() == 'Merge Sort':
        merge_sort(data,visualise, float(timeslec.get()))

    if algoslec.get() =='Selection Sort':
        select_sort(data, visualise, float(timeslec.get()))

    if algoslec.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1,visualise,float(timeslec.get()))

    visualise(data, ['#D5F5E3' for x in range(len(data))])


Height = 600
Width = 1200
Algoptions = ['Bubble Sort','Selection Sort','Merge Sort','Quick Sort']
parent = tk.Tk()
parent.maxsize(Width, Height)

parent_canvas = tk.Canvas(parent, height = Height,width = Width, bg = '#AED6F1')
parent_canvas.pack()

#user interface section
input_frame = tk.Frame(parent, bg = "#5c6559")
input_frame.place( relx = 0.5, rely = 0.05,height = 80, relwidth = 0.95,anchor= 'n')

tk.Label(input_frame,text = "Select Algorithm:", bd=3,bg = "#5c6559",font = (1,12)).place(relx = 0.0075, rely = 0.05)
option1 = StringVar()
algoslec = ttk.Combobox(input_frame, textvariable = option1,values = Algoptions)
algoslec.place(relx = 0.12, rely = 0.075)
algoslec.current(0)

tk.Label(input_frame,text = "Step-Time Delay(s) :", bd=3,bg = "#5c6559",font = (1,12)).place(relx = 0.0075, rely = 0.5)
option2 = StringVar()
timeslec = ttk.Combobox(input_frame, textvariable = option2,values = ['0.0','0.01','0.1','0.5','1.0'])
timeslec.place(relx = 0.14, rely = 0.55)
timeslec.current(0)





algobutton = tk.Button(input_frame, text = "SORT!!!",font = (1,14), command = lambda: sort(),bg = 'green')
algobutton.place(relx = 0.3, rely = 0.25, width =200, height = 40 )


tk.Label(input_frame,text = "Number of Elements:", bd=3,bg = "#5c6559",font = (1,13)).place(relx = 0.5, rely = 0.25)
sizeentry = tk.Entry(input_frame, font = 40)
sizeentry.place(relx = 0.65, rely =0.25, width = 70 )


arraybutton = tk.Button(input_frame, text = "Generate Aray",font = (1,13), command = lambda: generate(),bg = 'red')
arraybutton.place(relx = 0.75, rely = 0.25, width =200, height = 40 )

#graphical output
graph_canvas = tk.Canvas(parent_canvas, bg= '#F0F3F4', height = 425, width = 1150)
graph_canvas.place(relx = 0.5, rely = 0.22, anchor='n')


parent.mainloop()