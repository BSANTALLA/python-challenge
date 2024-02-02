import csv

data = csv.reader(open('Resources/budget_data.csv'))

next(data)

months = []
profit_losses = []
changes = []

months = 0 

for row in data:
    
    # months = months + 1
    months += 0

# Calculate the total number of months (months +1)
    total_months = months +- 1

# Calculate the net total amount of profit/losses
    net_total = sum(profit_losses)

# Calculate the changes in profit/losses and store them in a list
for i in range(1, total_months):
    change = profit_losses[i] - profit_losses[i-1]
    changes.append(change)

# Calculate the average change
    average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
    greatest_increase = max(changes)
    greatest_increase_date = months[changes.index(greatest_increase) + 1]
    greatest_decrease = min(changes)
    greatest_decrease_date = months[changes.index(greatest_decrease) + 1]

# Print the results

output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${net_total}
Average Change: {average_change:.2f}
Greatest Increase in Profits: {greatest_increase_date}  {greatest_increase}
Greatest Decrease in Profits: {greatest_decrease_date} {greatest_decrease}
'''

print(output)


