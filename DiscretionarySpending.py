# DiscretionarySpending, 
# ITSE 1302-7Z2, 
# Jackson Mehalko,
# Find the average of user inputs

#Variables for an int to be submited by the user
pay = int(input("Enter Pay:"))
rent = int(input("Enter Rent:"))
utilities = int(input("Enter Utilities:"))
groceries = int(input("Enter Groceries:"))

# variables with operations in them 
totalBills = (rent + utilities + groceries)
discretionary = pay - totalBills

# Displays the product of all the code up top
print("Pay = $",pay)
print("Total Bills = $",totalBills)
print("Discretionary = $",discretionary)

input()