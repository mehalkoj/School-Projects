#idList stores all the IDs that have access to the archives
idList = ["18550", "98551", "78532", "18521", "48526", "38520", "88578", \
"98583", "48566", "28579", "18586", "88559", "18593", "38570", "28596", "58537", \
"58516", "18577", "78557", "18503", "98501", "28504", "98539"]

print("ID Search\n")
idSearch = input("Enter ID to search(enter XXX to exit): ")
while idSearch!="XXX":
    
    isFound = False
    
    for id in idList:
        
        if id==idSearch:
            
            print("On The List")
            
            isFound = True
            
    if not isFound:
        
        print("Not On The List")
    idSearch = input("Enter ID to search(enter XXX to exit): ")