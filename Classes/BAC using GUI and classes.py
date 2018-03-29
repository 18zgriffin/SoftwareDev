from tkinter import *

def calcBAC(SD, CF, M, T):
    return float(SD)/(float(CF)*float(M))*100 - (0.00015*float(T))

def outCome(status, BAC):
    if status == 'L' or status == 'P':
        if BAC > 0:
            return 'License cancelled, interlock device'
        else:
            return 'Safe to Drive'
    if status == 'FL':
        if BAC > 0.07:
            return 'License cancelled, interlock device'
        elif 0.05 <= BAC <= 0.07 :
            return 'Fine and 10 demerit points'
        else:
            return 'Safe to Drive'

class ConversionGUI:
    def __init__(self, master):
        self.master = master
        master.title("BMI Calculator")

        self.titleText = Label(master, text="BAC Calculator:", bg="blue", font=("Times", "24", "bold italic"), fg="red")
        self.titleText.grid(columnspan = 3, row = 0)
        self.titleText.grid()

        self.radioSelect1 = DoubleVar()
        self.radioM = Radiobutton(master, text='Male', variable=self.radioSelect1, value=0)
        self.radioM.grid(column = 0, row = 1, columnspan = 2)
        self.radioF = Radiobutton(master, text="Female", variable=self.radioSelect1, value=1)
        self.radioF.grid(column = 1, row = 1, columnspan = 2)

        self.radioSelect2 = DoubleVar()
        self.radioI = Radiobutton(master, text='Imperial(lb)', variable=self.radioSelect2, value=0)
        self.radioI.grid(column = 0, row = 3, columnspan = 2)
        self.radioM = Radiobutton(master, text="Metric(Kg)", variable=self.radioSelect2, value=1)
        self.radioM.grid(column = 1, row = 3, columnspan = 2)

        self.radioSelect3 = StringVar()
        self.radioL = Radiobutton(master, text='Learner', variable=self.radioSelect3, value="L")
        self.radioL.grid(column = 0, row = 4, sticky = W, padx = 15)
        self.radioP = Radiobutton(master, text="Probationary", variable=self.radioSelect3, value="P")
        self.radioP.grid(column = 0, row = 4, columnspan = 3)
        self.radioF = Radiobutton(master, text="Fully Licensed", variable=self.radioSelect3, value="FL")
        self.radioF.grid(column=2, row=4, sticky = E)

        self.feetLabel = Label(master, text="Time since last drink: ")
        self.feetLabel.grid(column = 0, row = 5, sticky = W)
        self.time = StringVar()
        self.entryValue = Entry(master, textvariable=self.time)
        self.entryValue.grid(row = 5, column = 1, columnspan = 2)

        self.feetLabel = Label(master, text="Number of Drinks: ")
        self.feetLabel.grid(column = 0, row = 6, sticky = W)
        self.nDrinks = StringVar()
        self.entryValue = Entry(master, textvariable=self.nDrinks)
        self.entryValue.grid(row=6, column = 1, columnspan = 2 )

        self.feetLabel = Label(master, text="Weight: ")
        self.feetLabel.grid(column = 0, row = 7, sticky = W)
        self.mass = StringVar()
        self.entryValue = Entry(master, textvariable=self.mass)
        self.entryValue.grid(row=7, column = 1, columnspan = 2)

        self.calcButton = Button(master, text="Calculate", command=self.calculate)
        self.calcButton.grid(row=10, column = 0)

        self.resultLabel = Label(master, text="BAC:")
        self.resultLabel.grid(row = 8, column = 0, columnspan = 2)

        self.result = DoubleVar()
        self.resultValue = Label(master, textvariable=self.result)
        self.result.set(0.0)
        self.resultValue.grid(row = 8, column=1, columnspan = 2)

        self.categoryLabel = Label(master, text="Category:")
        self.categoryLabel.grid(row = 9, column = 0, columnspan = 2)

        self.outcome = DoubleVar()
        self.categoryValue = Label(master, textvariable=self.outcome)
        self.outcome.set("None")
        self.categoryValue.grid(row=9, column=1, columnspan = 2)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=10, column=1, columnspan = 2)

    def calculate(self):
        time = self.time.get()
        nDrinks = self.nDrinks.get()
        mass = self.mass.get()

        if not(self.radioSelect2.get()):
            massinG = (float(mass) * 453.92)
        elif self.radioSelect2.get():
            massinG = (float(mass) * 1000)

        if not(self.radioSelect1.get()):
            CF = 0.68
        elif self.radioSelect1.get():
            CF = 0.55

        status = self.radioSelect3.get()

        SD = float(nDrinks) * 10

        result = round(calcBAC(SD, CF, massinG, time), 2)
        self.result.set(result)

        category = outCome(status, result)
        self.outcome.set(category)
        return

root = Tk()
gui = ConversionGUI(root)
root.mainloop()