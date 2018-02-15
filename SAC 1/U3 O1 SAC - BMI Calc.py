def convertHeight(height):
    heightinMetres = ((heightf*12+heighti)*0.0254)

def convertWeight(weight):
    weightInKgs = (weightInKgs*0.45359237)

x = input("Would you like to enter your measurements in imperial(i) ir metric(m) units? ")

if x == i:
    heightf = input("What is your height? (Feet Value): ")
    heighti = input("What is you height? (Inches Value): ")
    weight = input("What is you weight? (lbs) ")
    convertHeight(height)
    convertweight(weight)
else:
    height = input("What is your height? (ms)")
    weight = input("What is you weight? (kg)")