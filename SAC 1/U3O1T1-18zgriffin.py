from tkinter import *
#function the coverts imperial height to metric height
def convertHeight(height):
    if height[-1:] != '"':
        height = "Error"
    else:
        height = (height[:-1].split("'"))
        try:
            height = ((float(height[0])*12+float(height[1]))*0.0254)
        except:
            height = "Error"
    return(height)

#function that converts imperial weight to metric weight
def convertWeight(weight):
    weight = (float(weight)*0.45359237)
    return(weight)

#function that calculates what BMI category someone is in
def getBMIcategory(BMI):
    if BMI < 18.5:
        category = "Underweight"
    elif BMI >= 18.5 and BMI < 25:
        category = "Healthy Weight"
    elif BMI >- 25 and BMI < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return(category)


class ConversionGUI:
    def __init__(self, master):
        self.master = master
        master.title("BMI Calculator")

        self.titleText = Label(master, text="BMI Calculator:", bg="blue", font=("Times", "24", "bold italic"), fg="red")
        self.titleText.grid(columnspan = 2, row = 0)
        self.titleText.grid()

        self.radioSelect = DoubleVar()

        self.radioI = Radiobutton(master, text='Imperial(lbs, Feet\'Inches\")', variable=self.radioSelect, value=0)
        self.radioI.grid(column = 0, row = 1)

        self.radioM = Radiobutton(master, text="Metric(kg, m)", variable=self.radioSelect, value=1)
        self.radioM.grid(column = 1, row = 1)

        self.feetLabel = Label(master, text="Enter your weight: ")
        self.feetLabel.grid(column = 0, row = 3)
        self.weight = StringVar()
        self.entryValue = Entry(master, textvariable=self.weight)
        self.entryValue.grid(row = 3, column = 1)

        self.feetLabel = Label(master, text="Enter your height: ")
        self.feetLabel.grid(column = 0, row = 4)
        self.height = StringVar()
        self.entryValue = Entry(master, textvariable=self.height)
        self.entryValue.grid(row=4, column = 1)

        self.calcButton = Button(master, text="Calculate", command=self.calculate)
        self.calcButton.grid(row=7, column = 0)

        self.resultLabel = Label(master, text="Result:")
        self.resultLabel.grid(row = 5, column = 0)

        self.result = DoubleVar()
        self.resultValue = Label(master, textvariable=self.result)
        self.result.set(0.0)
        self.resultValue.grid(row = 5, column=1)


        self.categoryLabel = Label(master, text="Category:")
        self.categoryLabel.grid(row = 6, column = 0)

        self.category = DoubleVar()
        self.categoryValue = Label(master, textvariable=self.category)
        self.category.set("None")
        self.categoryValue.grid(row=6, column=1)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=7, column=1)

    def calculate(self):
        height = self.height.get()
        weight = self.weight.get()
        if not(self.radioSelect.get()):
            try:
                height = convertHeight(height)
                weight = convertWeight(weight)
                result = round(weight / (height ** 2), 2)
                category = getBMIcategory(result)
                self.category.set(category)
            except TypeError:
                result = "Error"
        elif self.radioSelect.get():
            try:
                result = round(float(weight) / (float(height) ** 2), 2)
                category = getBMIcategory(result)
                self.category.set(category)
            except:
                result = "Error"
        self.result.set(result)
        return

root = Tk()
gui = ConversionGUI(root)
root.mainloop()

