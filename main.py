import os
import random
from tkinter import *

class appWindow:
    def __init__(self, master, appFont="Arial", equationFont="Courier", angleChoice=None, signChoice=None):
        self.master = master
        self.appFont=appFont
        self.equationFont=equationFont
        if angleChoice==None and signChoice==None:
            angleChoice='rad'
            signChoice='pos'
        else:
            pass

        master.title("Trigonometric Evaluation Equation Generator")

        self.makeQuestion_button = Button(master, text="Generate Question", highlightbackground="lime", height=3,command=lambda: self.reloadQuestion(angleChoice, signChoice))
        self.makeQuestion_button.config(font=(appFont,20))

        self.label = Label(master, text="Equation:")
        self.blankSpace1= Label(master, text="")
        self.blankSpace2= Label(master, text="")
        self.label.config(font=(appFont,24))

        self.equationText = Label(master,text="")
        self.equationText.config(font=(equationFont,44))


        self.close_button = Button(master, text="Close",highlightbackground="red", command=master.quit,bg="red", border=2)
        self.close_button.config(font=(appFont,20))


        self.label.pack()
        self.equationText.pack()
        self.blankSpace1.pack()  
        self.makeQuestion_button.pack()
        self.blankSpace2.pack()
        self.close_button.pack()

    def createQuestion(self, anglePreference, signChoice):
        functions = ["sin", "cos", "tan", "cot", "sec", "csc"]
        deg_angles = [0,30,60,90,120,135,150,180,210,225,240,270,300,315,330,360]
        rad_angles = ["π/6", "π/4", "π/3","π/2", "2π/3","3π/4","5π/6","π","7π/6","5π/4","4π/3","3π/2","5π/3","7π/4","11π/6"]
        neg_deg_angles = [-0,-30,-60,-90,-120,-135,-150,-180,-210,-225,-240,-270,-300,-315,-330,-360]
        neg_rad_angles = ["-π/6", "-π/4", "-π/3","-π/2", "-2π/3","-3π/4","-5π/6","-π","-7π/6","-5π/4","-4π/3","-3π/2","-5π/3","-7π/4","-11π/6"]

        degOrRad = random.randint(1,2)
        if signChoice.lower()=="pos":
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

        elif signChoice.lower()=="neg":
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
                randomDegree=random.choice(neg_deg_angles)
                text=randomFunction+" "+str(randomDegree)+str("°")
                return text
            elif degOrRad ==2:
                randomFunction=random.choice(functions)
                randomRadian=random.choice(neg_rad_angles)
                text=randomFunction+" "+str(randomRadian)
                return text
        elif signChoice.lower()=="both":
            if anglePreference.lower()=='rad':
                degOrRad=2
            elif anglePreference.lower()=='deg':
                degOrRad=1
            elif anglePreference.lower()=='both':
                degOrRad = random.randint(1,2)
            else:
                degOrRad = random.randint(1,2)
            choosingSign=random.randint(1,2)
            if degOrRad == 1:
                randomFunction=random.choice(functions)
                if choosingSign==1:
                    randomDegree=random.choice(neg_deg_angles)
                if choosingSign==2:
                    randomDegree=random.choice(deg_angles)
                text=randomFunction+" "+str(randomDegree)+str("°")
                return text
            elif degOrRad ==2:
                randomFunction=random.choice(functions)
                if choosingSign==1:
                    randomRadian=random.choice(neg_rad_angles)
                if choosingSign==2:
                    randomRadian=random.choice(rad_angles)
                text=randomFunction+" "+str(randomRadian)
                return text
        else:
            print(degOrRad)
            print(anglePreference)
            print(signChoice)
            return "An error has occured"

    def reloadQuestion(self, angleChoice, funcSign):
        global theEquation
        print(angleChoice)
        print(funcSign)
        theEquation=self.createQuestion(angleChoice,funcSign)
        self.equationText.config(text=theEquation)


root = Tk()
app= appWindow(root, "Times New Roman", "Courier", "both", "both")
root.geometry("480x260")
root.resizable(width=False, height=False)
root.mainloop()
