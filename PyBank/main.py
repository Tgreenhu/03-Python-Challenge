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
        months.append(month[0])
        total_months = len(months)
        total.append(int(month[1]))
        net_amount = sum(total)
    for x in range(len(total)-1):
        change.append(total[x+1]-total[x])
    average_change = sum(change)/len(change)
    max_change = max(change)
    min_change = min(change)
    max_month = change.index(max(change))+1
    min_month = change.index(min(change))+1
    max = months[max_month]
    min = months[min_month]

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {max} (${max_change})")
print(f"Greatest Decrease in Profits: {min} (${min_change})")

pybank_analysis = os.path.join("analysis", "financial_analysis.txt")
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