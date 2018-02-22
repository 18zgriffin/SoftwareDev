def listsort(arg_list):
    arg_list.sort()
    listlen = len(arg_list)
    print("The sorted list is", arg_list)
    print("The largest value in the list is", arg_list[listlen-1])

def listreverse(or_list):
    rlist = []
    for i in or_list:
        rlist.insert(0, i)
    print("The reverse list is", rlist)

def eleminlist(in_list):
    elem = int(input("What do you want to find in the list "))
    if elem in in_list:
        print("Yes that is in the list")
    else:
        print("No that is not in the list")

list = []
UI = "\n"
while (UI != ""):
    UI = input("Enter a value for the list: ")
    if (UI != ""):
       list.append(int(UI))
print("The current values are: ")
print(list)

(listsort(list))

(listreverse(list))

(eleminlist(list))