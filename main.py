import os
import random
from tkinter import *



class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Trigonometric Evaluation Equation Generator")

        self.makeQuestion_button = Button(master, text="Generate Question", highlightbackground="lime",command=self.reloadQuestion, height=3)

        self.label = Label(master, text="Equation:")
        self.blankSpace= Label(master, text="")
        self.label.config(font=("Courier",24))

        self.equationText = Label(master,text="")
        self.equationText.config(font=("Courier",44))


        self.close_button = Button(master, text="Close",highlightbackground="red", command=master.quit,bg="red", border=2)

        self.label.pack()
        self.equationText.pack()        
        self.makeQuestion_button.pack()
        self.blankSpace.pack()
        self.close_button.pack()

    def createQuestion(self):
        functions = ["sin", "cos", "tan", "cot", "sec", "csc"]
        deg_angles = [0,30,60,90,120,135,150,180,210,225,240,270,300,315,330,360]
        rad_angles = ["π/6", "π/4", "π/3","π/2", "2π/3","3π/4","5π/6","π","7π/6","5π/4","4π/3","3π/2","5π/3","7π/4","11π/6"]
        degOrRad = random.randint(1,2)

        if degOrRad == 1:
            randomFunction=random.choice(functions)
            randomDegree=random.choice(deg_angles)
            text=randomFunction+" "+str(randomDegree)
            return text
        elif degOrRad ==2:
            randomFunction=random.choice(functions)
            randomRadian=random.choice(rad_angles)
            text=randomFunction+" "+str(randomRadian)
            return text
        else:
            return "An error has occured"

    def reloadQuestion(self):
        global theEquation
        theEquation=self.createQuestion()
        self.equationText.config(text=theEquation)


root = Tk()
my_gui = MyFirstGUI(root)
theEquation=my_gui.createQuestion()
root.geometry("460x230")
root.resizable(width=False, height=False)
root.mainloop()
