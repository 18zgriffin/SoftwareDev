#defines some variables and identifies the name of the contacts lists
nameList = []
birthList = []
contacts = "contacts.txt"
menuOption = 0


#function that loads the contacts, into two seperate lists
def LoadContacts():
    c = open(contacts, "r")
    for i in c:
        #strips
        i = i.strip("\n")
        i = i.split(" ")
        #appends current name and current birthday to each approriate list
        nameList.append(i[0])
        birthList.append(i[1])
    print("Contacts Succesfully loaded")
    return nameList, birthList

#function that adds a new function to both the original file and name/birth lists
def NewContact():
    #opens file for reading
    c = open(contacts, "a")
    #gets the input for a new contacts name and birthday
    NCname = input("Enter the new contacts name: ")
    #loops so that the new birthday is in the correct format
    lenNCbirthday = 0
    while lenNCbirthday != 10:
        NCbirthday = input("Enter the new contacts birthday(##/##/####): ")
        lenNCbirthday = len(NCbirthday)
    #adds each the name and birthday to appropriate list
    nameList.append(NCname)
    birthList.append(NCbirthday)
    #writes the name and birthday to the file(incase program crashes midway)
    c.write("\n")
    c.write(NCname + " " + NCbirthday)
    c.close()
    print("")
    return

#function that changes the birthday of one contact to a new birthday
def ChangeBirthday(nameList, birthList):
    #gets the name of the contact to be changed and finds its position
    CBname = input("Enter the name of the contact you wish to change: ")
    position = SearchFunction(nameList, CBname)
    if position == -1:
        print("That contact does not exist")
        return
    else:
        #displays the contacts current birthday, then accepts the new birthday input
        print(nameList[position]+"'s current birthday is " + birthList[position])
        newDay = input("Enter a new birthday(##/##/####) or enter (0) to cancel: ")
        #changes their birthday to the new birthday or ends the function if the user decides to cancel
        if newDay != 0:
            birthList[position] = newDay
            print("Name" + ((len(nameList[position])-4)*" ") + " : Birthdate")
            print("----" + ((len(nameList[position])-4)*"-") + "   ----------")
            print(nameList[position] + " : " +birthList[position])
        else:
            return
    print("")
    return

#function that deletes the contact name and birthday, from the lists, doesnt remove from original file
def DeleteContact(nameList, birthList):
    #user inputs name of contact to change, and search function finds its position
    DCname = input("Enter the name of the contact you wish to remove: ")
    position = SearchFunction(nameList, DCname)
    if position == -1:
        print("That contact does not exist")
        return
    else:
        #removes the contact from the list
        nameList.remove(nameList[position])
        birthList.remove(birthList[position])
    print("")
    return

#function that displays the birthday of an entered contact
def LookupBirthday(nameList, birthList):
    #user inputs the name of the contact being searched, and search function finds its position
    LBname = input("Enter the name of the contact: ")
    position = SearchFunction(nameList, LBname)
    if position == -1:
        print("That contact does not exist")
    else:
        #prints the contacts name and birthday
        print("Name" + ((len(nameList[position])-4)*" ") + " : Birthdate")
        print("----" + ((len(nameList[position])-4)*"-") + "   ----------")
        print(nameList[position] + " : " +birthList[position])
    print("")
    return

#saves any changes made to the nameList and birthList to the original file, overiding the current contents
def SaveFile(nameList, birthList):
    #opens the contacts file for writing, also clears it
    c = open(contacts, "w")
    pos = -1
    #writes each of the contacts currently in the lists to the file
    for name in nameList:
        pos = pos + 1
        c.write(name + " " + birthList[pos])
        c.write("\n")
    print("")
    return

#function that searches for the position of a name within the contacts
def SearchFunction(listCon,  searchName):
    #loops for every name in the list
    for name in listCon:
        #checks if the name is the same as the search name
        if name == searchName:
            #identifies the position of the name and returns it to where it was called
            position = listCon.index(name)
            return position
        else:
            position = -1
    return position

#function that displays all of the current contacts in the list
def ShowAll(nameList, birthList):
    #prints the initial "Name : Birthdate" display
    print("")
    print("Name " + " : Birthdate")
    print("----" + "   ----------")
    position = -1
    #prints each contact on a seperate line
    for i in nameList:
        position = position + 1
        print("- " + nameList[position] + " : " +birthList[position])
    print("")

#runs the LoadContacts function so there are ready
LoadContacts()

#menu loop, gives the user options to pick from
while True:
    #gives the user the selections they can make
    print("Please enter the number of the option you wish to select")
    print("    1. Look up contact")
    print("    2. Add a new contact with birth date")
    print("    3. Change a birthday")
    print("    4. Delete a contact and birth date")
    print("    5. Quit program")
    print("    6. Display all")
    #takes selection via input
    menuOption = input("Selection: ")
    print("")
    #performs the specified function
    if menuOption == "1":
        LookupBirthday(nameList, birthList)
    elif menuOption == "2":
        NewContact()
    elif menuOption == "3":
        ChangeBirthday(nameList, birthList)
    elif menuOption == "4":
        DeleteContact(nameList, birthList)
    elif menuOption == "5":
        SaveFile(nameList, birthList)
        exit(0)
    elif menuOption == "6":
        ShowAll(nameList, birthList)
    else:
        #reloops the menu because their selection made did not exist
        print("Menu option selection does not exist: ")
        menuOption = 0

