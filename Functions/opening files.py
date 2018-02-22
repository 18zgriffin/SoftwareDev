#get the filename from the user
print("Enter the name of the file to be read")
fname = input(":")

#open the file specified by the user
try:
    f = open(fname, "r")
except FileNotFoundError:
    print("File does not exist")
    exit(0)

#print contents of file
for line in f:
    #strip new line character
    line = line.strip('\n')
    #prints line
    print(line)

#close file
f.close()

#open file for write
f = open(fname, "a")

#add a new line to the file
f.write("\n")

#write to file
f.write(input("Add a new line to the bottom of the file: "))

#close file
f.close()
import csv

help(csv)