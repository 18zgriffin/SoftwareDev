#sets up the initial values
v = 0.00015
gender = ""
mass = ""
time = ""
drinks = ""
yes = ""
x = 1

#tests if the gender is m or f and assign appropriate value to r
while True:
    gender = input("What gender are you? (M or F) ")
    #checks if input is m or f then loops if not
    if gender == "M":
        r = 0.68
        break
    elif gender == "F":
        break
        r = 0.55
    print("You entered neither M or F, try again")

#makes sure you entered the weight as a float and as either lb or kg
while True:
    #asks for input of weight and type
    try:
        mass = int(input("How much do you weigh? "))
        type = input("Did you use Imperial(lb) or Metric(kg) ")

    except ValueError:
        print("You entered your mass incorrectly, try again")
    else:
        #verifies type and performs conversion
        if type == "lb":
            w = mass*453.592
            break
        elif type == "kg":
            w = mass*1000
            break
        else:
            print("You entered the type incorrectly, try again")

#makes sure you entered the time as a float
while True:
    try:
        time = int(input("How many hours ago did you start drinking?(Hours) "))
    except ValueError:
        print("You entered the time wrong incorrectly, try again")
    else:
        break

#makes sure you enter the standard drinks a float
while True:
    try:
        drinks = float(input("How many standard drinks have you consumed? "))
    except ValueError:
        print("You entered the number of drinks incorrectly, try again")
    else:
        break

#asks what kind license holder they are and validates
while x == 1:
    license = input("What kind of license holder are you? learner(L), fully licensed (FL) or probationary(P)? ")
    if license == "L":
        break
    elif license == "FL":
        break
    elif license == "P":
        break
    print("You entered neither F or FL, try again")

#converts the drinkes to the appropriate value
a = int(10*drinks)

#calculates the BAC
BAC = round((a/(r*w)*100-(v*time)),2)

#tells the person their blood alchohol content and if using their licensing what kind of penalty for driving may incur
if license == "L" or license == "P":
    #checks if the learner of probationary drivers has a good BAC or not
    if BAC > 0.00:
        print("As a learner or probationary driver with a blood alchohol above 0.00 of", BAC, "your license would be cancelled and an interlock device required for 6 months after license is returned")
    else:
        print("Good job your blood alchohol is low enough at only", BAC)
elif license == "FL":
    #checks if the fully licensed driver has a good blood alchhol or not
    if BAC >= 0.05 and BAC <= 0.07:
        print("As a fully licensed driver with a blood alchohol between 0.05 and 0.07 equal to", BAC, "you will be fined and lose 10 demerit points")
    elif BAC > 0.07:
        print("As a fully licensed driver with a blood alchohol above 0.07, equal to", BAC, "you will lose your license and will have to install a interlock device for 6 months after license is returned")
    else:
        print("Good job your blood alchohol is low enough at only", BAC)
