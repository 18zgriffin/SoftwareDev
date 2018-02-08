import math

a = int(input("What is the length of side adjacent? "))
b = int(input("What is the length of side opposite? "))

c = math.sqrt(b**2 + a**2)

print("The hypotenuse is",c)

angl1rad = (math.atan(b/a))
angl2rad = (math.atan(a/b))

angle1deg = int(round(math.degrees(angl1rad),0))
angle2deg = int(round(math.degrees(angl2rad),0))

print("The angles of your triangle are", angle1deg, "degrees,", angle2deg, "degrees and 90 degrees")