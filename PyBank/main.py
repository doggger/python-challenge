# Importing Modules and Setting Path
import os
import csv

csvpath = os.path.join('resources', 'budget_data.csv')

#Setting Variables and Opening csv file and pulling off headers
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    Unique_Month = 0
    Profit_Loss = 0
    Average_Profit_Loss = 0
    temp = ' '
    change = 0
    holder = 0
    temp2 = 0
    sum = 0
    greatest_increase_date = ''
    greatest_decrease_date = ''
    greatest_decrease = 0
    greatest_increase = 0

#loops through data and performs calculations
    for row in csvreader:
        # counts unique values in first row
        if temp != row[0]:
            Unique_Month = Unique_Month + 1
        temp = row[0]
       
       #running sum of profit/loss
        Profit_Loss = Profit_Loss + int(row[1])
       
    #skips first iteration, calculates greatest increase and decrease, calculates avg change
        if holder != 0:
            change = (int(row[1]) - previous_pl)
            if previous_pl > int(row[1]):
                if greatest_decrease > change:
                    greatest_decrease = change
                    greatest_decrease_date = row[0]
            if previous_pl < int(row[1]):
                if greatest_increase < change:
                    greatest_increase = change
                    greatest_increase_date = row[0]
            temp2 = temp2 + change
            sum = sum + 1
        previous_pl = int(row[1])
        holder = holder + 1
    Average_Profit_Loss = round(temp2 / sum, 2)

#Printing to Terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months:  {Unique_Month}")
    print(f"Total:  ${Profit_Loss}")
    print (f"Average Change: ${Average_Profit_Loss}")
    print (f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print (f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

#Printing to text File
    textpath = os.path.join('analysis', 'analysis.txt')
    L = [
        'Financial Analysis \n', 
        '-------------------------- \n', 
        'Total Months: ', str(Unique_Month), '\n', 
        'Total: $', str(Profit_Loss), '\n', 
        'Average Change: $', str(Average_Profit_Loss), '\n', 
        'Greatest Increase in Profits: ', greatest_increase_date, '  ($', str(greatest_increase), ') \n', 
        'Greatest Decrease in Profits: ', greatest_decrease_date, '  ($', str(greatest_decrease), ')'  
        ]
    with open(textpath, 'w') as textfile:
       textfile.writelines(L)

