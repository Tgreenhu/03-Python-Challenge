import os
import csv
pybank = os.path.join("resources", "budget_data.csv")

months = []
total = []
change = []

with open(pybank, "r") as pybank_file:
    pybank_reader = csv.reader(pybank_file, delimiter = ',')
    pybank_header = next(pybank_reader)
    for month in pybank_reader:
        months.append(month[0]) #List out all months
        total_months = len(months) #Calculate # of months in list
        total.append(int(month[1])) #List out all profits/losses
        net_amount = sum(total) #Sum of the list of all profit/losses
    for x in range(len(total)-1): 
        change.append(total[x+1]-total[x]) #Cycle through all rows and subtract the new profit from the previous
    average_change = sum(change)/len(change) #Average profit/loss per month
    max_change = max(change) #Maximum profit
    min_change = min(change) #Minimum profit (loss)
    max_month = change.index(max(change))+1 #Find where in the data our max profit took place
    min_month = change.index(min(change))+1 #Find where in the data our min profit took place
    max = months[max_month] #Find the month that saw the highest profit
    min = months[min_month] #Find the month that saw the lowest profit (loss)

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {max} (${max_change})")
print(f"Greatest Decrease in Profits: {min} (${min_change})")

pybank_analysis = os.path.join("analysis", "financial_analysis.txt") #Export to .txt file
with open(pybank_analysis, "w") as pybank_final:
    pybank_final.write(f"Financial Analysis")
    pybank_final.write("\n")
    pybank_final.write(f"----------------------------")
    pybank_final.write("\n")
    pybank_final.write(f"Total Months: {total_months}")
    pybank_final.write("\n")
    pybank_final.write(f"Total: ${net_amount}")
    pybank_final.write("\n")
    pybank_final.write(f"Average Change: ${round(average_change, 2)}")
    pybank_final.write("\n")
    pybank_final.write(f"Greatest Increase in Profits: {max} (${max_change})")
    pybank_final.write("\n")
    pybank_final.write(f"Greatest Decrease in Profits: {min} (${min_change})")