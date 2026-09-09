import math 

x1 = float(input("Enter x1: ")) 
x2 = float(input("Enter x2: ")) 
y1 = float(input("Enter y1: ")) 
y2 = float(input("Enter y2: ")) 

d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)) 

print("The distance between the two points is: ", d) 

# What helped out in the activity were the sqrt() and pow() library functions, so that it won't be tedious and will be easier to do. The functions used in this code was the sqrt() and pow(), and not having these functions to help with the code would make coding much harder than it is with the two functions. Using functions in code simplifies very difficult parts of the code and is time-efficient.