months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'October', 'November', 'December']
monthly_patron_count=[] 
for i in range(12):
    try:
        patron_count = int(input('{}  {} = '.format('Enter Monthly Patron count for', months_list[i])))
        monthly_patron_count.append(patron_count) 
        
    except:
        print('Warning:No input or Wrong input is given for',months_list[i])
        break 
        
        
if len(monthly_patron_count)==12: 

    
    total_patron=0 
    
    for i in range(len(monthly_patron_count)):
        total_patron = total_patron + monthly_patron_count[i]
    
    min_patron_index = 0 
    min_patron = monthly_patron_count[0] 
    
    for i in range(1,len(monthly_patron_count)):
        if monthly_patron_count[i]< monthly_patron_count[min_patron_index]:
            min_patron_index = i
            min_patron = monthly_patron_count[min_patron_index]

    max_patron_index = 0 
    max_patron = monthly_patron_count[0] 
    
    for i in range(1,len(monthly_patron_count)):
        if monthly_patron_count[i]> monthly_patron_count[max_patron_index]:
            max_patron_index = i
            max_patron = monthly_patron_count[max_patron_index]
            
    total_avg_patron = round(total_patron/12,2)
    
    print('-----------------------')
    print(f"{months_list[min_patron_index]:{13}} got smallest amount of patrons i.e:  {min_patron:{5}}")
    print(f"{months_list[max_patron_index]:{13}} got largest amount of patrons i.e:  {max_patron:{5}}")
    print(f"The average monthly visitors is {total_avg_patron:{5}}")

    print('-----------------------')