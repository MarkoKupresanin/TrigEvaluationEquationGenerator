import os
import random
from tkinter import *

class appWindow:
    def __init__(self, master, appFont="Arial", equationFont="Courier", angleChoice=None):
        self.master = master
        self.appFont=appFont
        self.equationFont=equationFont
        if angleChoice==None:#checks if anything was provided, if not defualt is radians
            angleChoice='rad'
        else:
            pass

        master.title("Trigonometric Evaluation Equation Generator")

        self.makeQuestion_button = Button(master, text="Generate Question", highlightbackground="lime", height=3,command=lambda: self.reloadQuestion(angleChoice))#Using a lambda function in order to pass in arguments to the Button
        self.makeQuestion_button.config(font=(appFont,20))

        self.label = Label(master, text="Equation:")
        self.blankSpace1= Label(master, text="")
        self.blankSpace2= Label(master, text="")
        self.label.config(font=(appFont,24))

        self.equationText = Label(master,text="")
        self.equationText.config(font=(equationFont,44))


        self.close_button = Button(master, text="Close",highlightbackground="red", command=master.quit,bg="red", border=2)
        self.close_button.config(font=(appFont,20))

        # Adding all elements to window
        self.label.pack()
        self.equationText.pack()
        self.blankSpace1.pack()  
        self.makeQuestion_button.pack()
        self.blankSpace2.pack()
        self.close_button.pack()

    def createQuestion(self,anglePreference):
        functions = ["sin", "cos", "tan", "cot", "sec", "csc"]
        deg_angles = [0,30,60,90,120,135,150,180,210,225,240,270,300,315,330,360]
        rad_angles = ["π/6", "π/4", "π/3","π/2", "2π/3","3π/4","5π/6","π","7π/6","5π/4","4π/3","3π/2","5π/3","7π/4","11π/6"]
        degOrRad = random.randint(1,2)
        if anglePreference.lower()=='rad':
            degOrRad=2
        elif anglePreference.lower()=='deg':
            degOrRad=1
        elif anglePreference.lower()=='both':
            degOrRad = random.randint(1,2)
        else:
            degOrRad = random.randint(1,2)

        if degOrRad == 1:
            randomFunction=random.choice(functions)
            randomDegree=random.choice(deg_angles)
            text=randomFunction+" "+str(randomDegree)+str("°")
            return text
        elif degOrRad ==2:
            randomFunction=random.choice(functions)
            randomRadian=random.choice(rad_angles)
            text=randomFunction+" "+str(randomRadian)
            return text
        else:
            return "An error has occured"

    def reloadQuestion(self, angleChoice):
        global theEquation        # Creating global variable in order to modify the variable outside the current scope (when initalizing the app)
        theEquation=self.createQuestion(angleChoice)
        self.equationText.config(text=theEquation)


root = Tk()
app= appWindow(root, "Times New Roman", "Courier", "rad")
root.geometry("480x260")
root.resizable(width=False, height=False)
root.mainloop()
