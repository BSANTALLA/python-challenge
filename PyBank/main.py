import csv
from datetime import datetime

with open('Resources/budget_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    
    total_months = 0
    total_profit_loss = 0
    previous_profit_loss = 0
    monthly_changes = []
    greatest_increase = 0
    greatest_increase_date = ""
    greatest_decrease = 0
    greatest_decrease_date = ""
    
    #Begin storing the months
    for row in csv_reader:
        total_months += 1
        
        #Repeat over each row in the dataset
        date_string = row[0]
        profit_loss = int(row[1])
        
        #Convert the Date
        date = datetime.strptime(date_string, '%b-%y')
        
        total_profit_loss += profit_loss
        
        #Calc Change in Profit/Loss
        monthly_change = profit_loss - previous_profit_loss
        monthly_changes.append(monthly_change)
        
        #Greatest Increase Calc
        if monthly_change > greatest_increase:
            greatest_increase = monthly_change
            greatest_increase_date = date_string
        
        #Greatest Decrease Calc
        if monthly_change < greatest_decrease:
            greatest_decrease = monthly_change
            greatest_decrease_date = date_string
        
        #NewCalc for Profit Loss
        previous_profit_loss = profit_loss
    
    average_change = sum(monthly_changes) / (total_months-1)
    average_change_formatted = "${:,.2f}".format(average_change)
    total_profit_loss_formatted = "${:,.2f}".format(total_profit_loss)
    greatest_increase_formatted = "${:,.2f}".format(greatest_increase)
    greatest_decrease_formatted = "${:,.2f}".format(greatest_decrease)
    
    print("Total # of Months:", total_months)
    print("Total Profit/Loss:", total_profit_loss_formatted)
    print("Average Change:", average_change_formatted)
    print("Greatest Increase in Profits:", greatest_increase_date, "," , greatest_increase_formatted)
    print("Greatest Decrease in Profits:", greatest_decrease_date, ",", greatest_decrease_formatted)