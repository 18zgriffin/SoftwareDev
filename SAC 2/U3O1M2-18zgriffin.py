#names each of the files needed to be opened
weather = "weather.txt"
summary = "summary.txt"

#creates the dailytemp list for later use
dailytemp = []

#function which finds the average temp of a list
def avTemp(list):
    listlen = len(list)
    sumlist = sum(list)
    avTemp = round((sumlist/listlen),2)
    return avTemp

#opens each file for either reading or writing
w = open(weather, "r")
s = open(summary, "a")

#loops and performs the whole process for each day
for i in w:
    dailytemp = []
    #strip newline charecter
    i = i.strip('\n')
    #splits day into a list
    i = i.split(" ")
    #assigns the day, date and dew values to their variables
    try:
        day = str(i[0])
        date = i[1]
        dew = float(i[2])
    except ValueError:
        print("Your dew entry is incorrect")
        exit(0)
    try:
        day =+ "1"
        print("You entered you day wrong, find out whats wrong and try again")
        exit(1)
    except TypeError:
        break

    #creates the list and adds all of the daily temps to it
    try:
        for v in i[3:]:
            dailytemp.append(float(v))
    except ValueError:
        print("One of your temperatures is not an integer or float")
        exit(2)

    #sorts the list and then finds out which values are the minimum and maximum, and uses average function to find average
    dailytemp.sort()
    minTemp = dailytemp[0]
    maxTemp = dailytemp[(len(dailytemp))-1]
    avTemp(dailytemp)

    #determines what level of dew the day is and assigns the appropriate message
    if dew <= 16:
        msg = "Dry and Comfortable"
    elif dew > 16 and dew < 20:
        msg = "Muggy"
    elif dew >= 20:
        msg = "Very sticky and oppressive"

    #outputs the data on screeen to the user
    output = ("On", day, date, "Max temp of",maxTemp, "Min temo of", minTemp, "Average temo of", avTemp(dailytemp), "and", msg)

    #writes the data to the file
    p1 = str("On " + day + date)
    s.write(p1)
    s.write("\n")
    s.write("     min temp: "+ str(minTemp)+"C")
    s.write("\n")
    s.write("     min temp: "+ str(maxTemp)+"C")
    s.write("\n")
    s.write("     average temp: "+ str(avTemp(dailytemp))+"C")
    s.write("\n")
    s.write("Forecast:" + msg)
    s.write("\n")
    print(output)

w.close()
s.close()
