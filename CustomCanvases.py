# Program: CustomCanvases.py
# Course: ITSE 1302- 7Z2
# Author: Jackson Mehalko
# Description: 

canvas=int(input("Enter number of canvas:"))

print()

i=1
total=0

while i<=canvas:
    
    print("Enter canvas",i,"length (ft):",end="")
    length=int(input())
    print("Enter canvas",i,"width (ft):",end="")
    width=int(input())
    
    i=+1
    total=+length*width
    
if(total>20):
    
    rate=float(input("\nPrice per sq foot: $"))
    
    print("Total canvas square feet:{0:1f}".format(total))
    print("Total Price: ${0:.2f}".format(total*rate))
else:
    
    print("\nOrder not big enough")