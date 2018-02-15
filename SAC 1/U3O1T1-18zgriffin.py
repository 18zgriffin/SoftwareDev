#function the coverts imperial height to metric height
def convertHeight(heighti, heightf):
    heightinMetres = ((heightf*12+heighti)*0.0254)
    return(heightinMetres)

#function that converts imperial weight to metric weight
def convertWeight(weight):
    weightInKgs = (weight*0.45359237)
    return(weightInKgs)

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

#loop that validates your unit input either runs the convertion function or simply assigns metric values
while True:
    units = input("Would you like to enter your measurements in imperial(i) ir metric(m) units? ")
    #checks if units is in imperial
    if units == "i" or units == 'I':
        #loop that makes sure the user inputs the values as floats
        while True:
            try:
                heightf = float(input("What is your height? (Feet Value): "))
                heighti = float(input("What is you height? (Inches Value): "))
                weight = float(input("What is you weight? (lb's) "))
                #checks if values entered are positive
                if heightf > 0 and weight > 0 and heighti > 0:
                    break
                print("You entered your height or weight as a negative, try again")
            except ValueError:
                print("You input that value incorrectly, try again")
        #performs the imperial to metric function conversion for height and weight
        heightinMetres = (convertHeight(heighti, heightf))
        weightInKgs = (convertWeight(weight))
        break
    #checks if units are in metric
    elif units == "m" or units == 'M':
        # loop that makes sure the user inputs the values as floats
        while True:
            try:
                height = float(input("What is your height? (m's) "))
                weight = float(input("What is you weight? (kg's) "))
                #checks if values are positive
                if height > 0 and weight > 0:
                    break
                print("You entered your height or weight as a negative, try again")
            except ValueError:
                print("You input that value incorrectly, try again")
        #assigns the metric values to the calculation variables
        heightinMetres = height
        weightInKgs = weight
        break
    #tells user to try again as they did not enter m for metric or i for imperial
    else:
        print("You entered neither m or i, try again")

#calculates the BMI
BMI = round(weightInKgs/(heightinMetres**2),2)

#calls the BMI category function and gets the BMI category then prints it with the calculated BMI
category = getBMIcategory(BMI)
print("You have a BMI of", BMI, "and are", category)