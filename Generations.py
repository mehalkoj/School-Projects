# Program: Generations.py
# Course: ITSE-1302-7Z2
# Author: Jackson Mehalko
# Description: A Program that outputs the generatioanl cohort a person belongs to based on a persons age

age = float(input("Enter Age:"))

if (age < 6):
    print("This person is from Generation Alpha")
elif (age >= 6) and (age <= 24):
    print("This person is from Generation Z")
elif (age >= 25) and (age <= 40):
    print("This person is from Millenial Generation")
elif (age >= 41) and (age <= 56):
    print("This person is from Generation X")
elif (age >= 57) and (age <= 75):
    print("This person is from Baby Boomers")
elif (age >= 76) and (age <= 93):
    print("This person is from Silent Generation")
else:
    print("This person is from The Greatest Generation")
    
input("Press Enter To Quit")