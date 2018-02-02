q = int(input("What day of the month is it? "))
m = int(input("What month is it(the numeric value)? "))
l = (input("What is the year? "))

j = int(l[0]+l[1])
k = int(l[2]+l[3])

if 1 or 2 in m:
    m = m + 12
    k = k - 1

h = ((q +((13*(m+1))//5)+k+(k//4)+(j//4)-2*j)%7)

if h == 0:
    print("It is a Saturday")
elif h == 1:
    print("It is a Sunday")
elif h == 2:
    print("It is a Monday")
elif h == 3:
    print("It is a Tuesday")
elif h == 4:
    print("It is a Wednesday")
elif h == 5:
    print("It is a Thursday")
elif h == 6:
    print("It is a Friday")
# h is the day of the week
# d is the date of the month 31
# m is the month
# k is the year of century
# j is zero based century