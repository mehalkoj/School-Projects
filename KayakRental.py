# Program: PriceCalculator.py
# Course: ITSE 1302- 7Z2
# Author: Jackson Mehalko
# Description: 


print('Welcome to Mega Mart!\n')
price: float
total: float = 0
while True:
    price = float(input('Enter item price: '))
    if price == 0:
        break
    total += price

print('\n\n')
print('Subtotal: ${:.2f}'.format(total))
tax = (total * 8.25) / 100
print('Tax: ${:.2f}'.format(tax))
print('Total ${:.2f}'.format(tax + total))

    
    
input('Press ENTER to exit')