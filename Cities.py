citiesList = []
city = input("Enter city: ")

while city!="XXX":
    citiesList.append(city)
    city = input("Enter city: ")

citiesList.sort(reverse=True)

for x in citiesList:
    print(x)