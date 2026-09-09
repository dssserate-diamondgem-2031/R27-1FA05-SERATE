import math 

x1 = float(input("Enter x1: ")) 
x2 = float(input("Enter x2: ")) 
y1 = float(input("Enter y1: ")) 
y2 = float(input("Enter y2: ")) 

d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)) 

print("The distance between the two points is: ", d)