
'''
Nathanael

SDEV220

4/17/2018

Find the fibonacci number
'''
from math import sqrt
import tkinter 

class Convert:
    def __init__(self):
        #create main window
        self.main_window = tkinter.Tk()
        self.main_window.geometry("300x100")
        self.frame1 = tkinter.Frame(self.main_window)
        self.main_window.title('Fibonacci number')
        #self.frame2 = tkinter.Frame(self.main_window)

        self.answer_frame = tkinter.Frame(self.main_window)
        self.button = tkinter.Frame(self.main_window)


        self.label_1 = tkinter.Label(self.frame1, text='n = ')

        self.frame1_entry = tkinter.Entry(self.frame1,width=10)

        self.label_1.pack(side='left')
        self.frame1_entry.pack(side='left')

        self.result_label = tkinter.Label(self.answer_frame,text='Fibonacci number: ')


        #result label
        self.total = tkinter.StringVar()
        self.total_label = tkinter.Label(self.answer_frame,textvariable=self.total)

        self.result_label.pack(side='left')
        self.total_label.pack(side='left')


        #button
        self.calc_button = tkinter.Button(self.button,text='calculate',command=self.calc)
        self.calc_button.pack(side='left')


        #pack the frames
        self.frame1.pack()
        self.answer_frame.pack()
        self.answer_frame.pack()
        self.button.pack()

        tkinter.mainloop()


    def calc(self):
        self.answer = ((1+sqrt(5))**float(self.frame1_entry.get())\
                       -(1-sqrt(5))**float(self.frame1_entry.get()))\
                       /(2**float(self.frame1_entry.get())*sqrt(5))

        
        self.total.set(self.answer)
convert = Convert()
