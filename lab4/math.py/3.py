import math
n=int(input("Number of sides: "))
m=int(input("Length of the sides: "))
area= int((n*m**2) / (4*math.tan(math.pi/n) ))
print("The area of the polygon: ", area)
      