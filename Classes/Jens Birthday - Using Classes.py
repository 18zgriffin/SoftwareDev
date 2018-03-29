"""Author: Stuart Thornhill
Date: 8/03/2018
Version: 1.0
This code will read in a list of contacts and allow users to edit, add new, delete and read contacts from the
file. The file is called contacts.txt
Contact lists are formatted as a class containing a firstname, lastname, day, month and year. The function self.date()
will return the birthdate in a formatted string.
"""

class Contact:

    def __init__(self, firstname, lastname, day, month, year):
        self.firstname = firstname
        self.lastname = lastname
        self.day = day
        self.month = month
        self.year = year

    def date(self):
        date = self.day + "/" + self.month + "/" + self.year
        return date

#This function searches based on a name in a contact list
#sName is the name to be search for
#firstnameBool is a True or False value where false means it is a surename, true means it is a first name
#sContactList is a list formatted according to the contact list structure
#The return value will be the index of the sName in the contact list, or -1 if it was not found
def SearchFunction(sName, firstnameBool, sContactList):
    sIndex = -1
    #Searches for the first name
    if firstnameBool:
        sIndex = 0
        for sRecord in sContactList:
            #This searches in the list of lists on the First Name index
            if sRecord.firstname == sName:
                return sIndex
            sIndex += 1
    #Search for the last name
    elif not(firstnameBool):
        sIndex = 0
        for sRecord in sContactList:
            #This searches in the list of lists on the Last Name index
            if sRecord.lastname == sName:
                return sIndex
            sIndex += 1
    sIndex = -1
    return sIndex

#Takes the contact lists and take user input to search it for a name return the index
#of the resulting search, will loop until a valid name is searched
#ulContactList is a list in the contact list format
def UserToLookup(ulContactList):
    loop = True
    while loop:
        loop = False
        print("Do you want to look up contact to change by (First) or (Last) name?")
        flname = input(": ")
        if flname == "First":
            fnamebool = True
        elif flname == "Last":
            fnamebool = False
        else:
            print("Please select option again and enter (First) or (Last) for the name")
            loop = True

    loop = True
    while loop:
        loop = False
        nameForSearch = input("What name are you looking for: ")
        index = SearchFunction(nameForSearch, fnamebool, ulContactList)

        #Check to ensure that the searched name was found, if not resume loop
        if index == -1:
            print("No such name found, these are the names in your contacts:")
            print("Names in the list are:")
            for record in ulContactList:
                print(record.firstname, ", ", record.lastname)
            loop = True
    return index

#Loads contacts from a file called contacts.txt
#r_contactsList is the read contact list and will be returned
def LoadContacts():
    r_contactsList = []
    #Creates a file if it does not exist
    try:
        f = open("contacts.txt", "r")
    except FileNotFoundError:
        f = open("contacts.txt", "w")
        f.close()
        f = open("contacts.txt", "r")
    for line in f:
        line = line.strip('\n')
        line = line.split(",")
        date = line[2].split("/")
        con = Contact(line[0], line[1], date[0], date[1], date[2])
        r_contactsList.append(con)
    f.close()
    return r_contactsList

#Gets the details of a new contact and adds it to the list
#c_contactList should be a list in contact list format
#The list is returned with the new contact added
def NewContact(c_contactList):
    print("----Create contact----")
    #Getting information from user
    print("Enter the new contacts details")
    fname = input("Firstname: ")
    sname = input("Surname: ")
    print("Birthday")
    ddate = input("Day: ")
    mdate = input("Month: ")
    ydate = input("Year: ")

    #Appending all data to lists
    newContact = Contact(fname, sname, ddate, mdate, ydate)

    #Appending lists to main contact list
    c_contactList.append(newContact)
    return c_contactList

#Changes the details of a contact
#cb_contactList is a list on the contact list format
#Returns the modified contact list
def ChangeBirthday(cb_contactList):
    print("----Change birthday----")
    index = UserToLookup(cb_contactList)
    print("Enter new values or just press enter to leave the same")
    print(cb_contactList[index])
    fname = input("Firstname: ")
    sname = input("Surname: ")
    print("Birthday")
    ddate = input("Day: ")
    mdate = input("Month: ")
    ydate = input("Year: ")
    if fname != "":
        cb_contactList[index].firstname = fname
    if sname != "":
        cb_contactList[index].lastname = sname
    if ddate != "":
        cb_contactList[index].day = ddate
    if mdate != "":
        cb_contactList[index].month = mdate
    if ydate != "":
        cb_contactList[index].year = ydate
    return cb_contactList

#Deletes a contact by popping a list
#dc_contactList is a list on the contact list format
#Returns the list with a contact removed
def DeleteContact(dc_contactList):
    print("----Delete contact----")
    index = UserToLookup(dc_contactList)
    print("Are you sure you wish to delete this record? (Yes/No) ", dc_contactList[index])
    userResponse = input(": ")
    if(userResponse == "Yes"):
        dc_contactList.pop(index)
    return dc_contactList

#Finds a birthday and prints it for the user
#lb_contactList is a list on the contact list format
def LookupBirthday(lb_contactlist):
    print("----Look up contact----")
    index = UserToLookup(lb_contactlist)
    print(lb_contactlist[index].firstname, lb_contactlist[index].lastname,"has their birthday on ", lb_contactlist[index].date())
    return

#Saves a contact list back to a file in a format readable by LoadContacts()
#Saved in the format: John,Smith,01/01/2000
#Ed,White,05/11/1999
#Erin,Kirk,23/07/2994
def SaveFile(w_contactsList):
    f = open("contacts.txt", 'w')
    for entry in w_contactsList:
        f.write(entry.firstname)
        f.write(',')
        f.write(entry.lastname)
        f.write(',')
        f.write(entry.date())
        f.write('\n')
    f.close()
    print("File saved")
    return 1

#Set menu value to zero
menuOption = 0

#Load in existing contact list
contactsList = LoadContacts()

### MAIN BODY LOOP###
#Loops over the menu script to determine menu option selected
#Set loop to false for testing
while True:
    print("Please enter the number of the option you wish to select:")
    print("    1. Look up contact")
    print("    2. Add a new contact with a birth date")
    print("    3. Change a birthday")
    print("    4. Delete a contact with a birthday")
    print("    5. Quit the program")
    menuOption = input("Selection: ")
    if menuOption == "1":
        LookupBirthday(contactsList)
    elif menuOption == "2":
        contactsList = NewContact(contactsList)
        SaveFile(contactsList)
    elif menuOption == "3":
        ChangeBirthday(contactsList)
        SaveFile(contactsList)
    elif menuOption == "4":
        DeleteContact(contactsList)
        SaveFile()
    elif menuOption == "5":
        SaveFile(contactsList)
        exit(0)
    else:
        print("Menu option entered does not exist")
        menuOption = 0
    print("----------------------------------------")