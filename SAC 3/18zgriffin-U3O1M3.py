#declares the two main lists terms and meanings, also assigns a variable to the file
terms = []
meanings = []
lanFile = open("French.txt", "r")

#this runs automatically and loads every line from the code in the two lists terms and meanings
def loadLan():
    #loop so that everything in the file is written
    for line in lanFile:
        line = line.strip("\n")
        line = line.split(",")
        terms.append(line[0])
        meanings.append(line[1])
    return

#when run this first checks if the file contains values, if so it continous to print each of the terms and their translations
#onto a seperate line each
def display():
    x = 0
    #tests if the file has values, if it doesnt it returns
    if len(terms) == 0:
        print("There are now values in this file, add some first")
        return
    print("Word or phrase  :  Translation")
    #for everyterm in the term list, it prints it and and its corresponding translation
    for term in terms:
        print(term + ", " + meanings[x])
        x = x + 1
    print("")

#this function is run either when delete and word or search a word, it asks for the search term then goes through the term list
#and checks if it is in the list. If the list is empty or the term is not in the list it ends and tells the user the problem,
#other if it does exists it printd the word and translation and if need be returns the position
def search():
    #takes the input for the term to be searched
    searTerm = input("Enter the term you wish to select: ")
    pos = 0
    flag = 0
    #sets a loop to go until there is no other terms in the list to go through
    while pos < len(terms):
        #checks if the search term matches the corresponding term in the list
        if terms[pos] == searTerm:
            flag = 1
            #prints the term and translation and then returns its position
            print("Word or phrase  :  Translation")
            print(terms[pos]+ ", " + meanings[pos])
            return(pos)
        pos = pos + 1
    #if the while loop passes without returning, position is set to 0 and the user is informed of the mistake
    if flag == 0:
        print("The file that was searched is empty, or your input does not exist in the file")
        pos = -1
        return(pos)
    print("")

#this function adds new terms and translations to the list, the user will input the new term first and then the new translation
#both of which get appended to the new lists and file
def add():
    x = 0
    #takes the input for the new term
    newTerm = input("Enter the new word or phrase: ")
    #tests to make sure it is not an integer
    try:
        int(newTerm)
    except ValueError:
        pass
    else:
        print("You must enter Terms as words not integers")
        return
    #takes the input for the correspinding meaning
    newMeaning = input("Enter the meaning: ")
    #tests to make sure it is not an integer
    try:
        int(newMeaning)
    except ValueError:
        pass
    else:
        print("You must enter translations as words not integers")
        return
    #addes the term and meaning to the lists
    terms.append(newTerm)
    meanings.append(newMeaning)
    lanFile = open("French.txt", "w")
    #adds the term and meaning to the file
    for term in terms:
        lanFile.write(term)
        lanFile.write(",")
        lanFile.write(meanings[x])
        lanFile.write("\n")
        x = x + 1
    print("Term succesfully added")

#this function uses the search function to find a term in the list and delete it. It runs search to find the position of
#the term to delete and then if it exists removes the term from both lists
def delete():
    #runs the search function
    pos = search()
    #if the function returned -1 it again informs the user that the word or phrase didnt exist
    if pos == -1:
        print("That word or phrase doesnt exist")
        menuOption = 0
    #if the word does exist, the term and its corresponding meaning a removed from the list
    else:
        terms.remove(terms[pos])
        meanings.remove(meanings[pos])
    print("Term succesfully deleted")

#this function saves all of the terms and meanings from the list and then exits the code
def save():
    x = 0
    #opens the file for writing
    lanFile = open("French.txt", "w")
    #writes each of the terms and meanings to the file
    for term in terms:
        lanFile.write(terms[x])
        lanFile.write(meanings[x])
        lanFile.write("\n")
        x = x + 1
    #exits the code
    exit(1)

#runs the languages file
loadLan()

#the menu
while True:
    #gives the user the selections they can make
    print("Please enter the number of the option you wish to select")
    print("    1. Display")
    print("    2. Search")
    print("    3. Add new Words")
    print("    4. Delete saved word")
    print("    5. Save and exit")
    #takes selection via input
    menuOption = input("Selection: ")
    #performs the specified function
    if menuOption == "1":
        display()
    elif menuOption == "2":
        search()
    elif menuOption == "3":
        add()
    elif menuOption == "4":
        delete()
    elif menuOption == "5":
        save()
    else:
        #reloops the menu because their selection made did not exist
        print("Menu option selection does not exist: ")
        menuOption = 0