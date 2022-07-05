# Program: PriceCalculator.py
# Course: ITSE 1302- 7Z2
# Author: Jackson Mehalko
# Description: 


# Printing welcome message
print("Welcome to Store!")

# Variable that stores subtotal
subtotal = 0


while True:
   
   price = float(input("Enter item price: "))
   
   if price == 0:
       break
   
   qty = int(input("How many of item: "))
   
   subtotal = subtotal + (price * qty)


tax = subtotal * 0.0825


total = subtotal + tax

print("\n\nSubtotal:", "${:,.2f}".format(subtotal))
print("Tax:", "${:,.2f}".format(tax))
print("Total:", "${:,.2f}".format(total), "\n")    
    
input('Press ENTER to exit')