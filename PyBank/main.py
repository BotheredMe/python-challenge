import os
import csv

avg_prof_change = 0
max_prof_change = 0
min_prof_change = 0
max_prof_change_date = 0
min_prof_change_date = 0
i = 0
profit = []
absprofit = []
date = []
prof_change = []

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    #row_count = csvreader.line_num - 1
    for row in csvreader:
        

        profit.append(float(row[1]))
        absprofit.append(abs(float(row[1])))
        date.append(row[0])
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total: $" + str(sum((profit))))
    for i in range(1,len(profit)):
        prof_change.append(profit[i] - profit[i-1])
        avg_prof_change = sum(prof_change)/len(prof_change)
        max_prof_change = max(prof_change)
        min_prof_change = min(prof_change)
        max_prof_change_date = str(date[prof_change.index(max(prof_change))])
        min_prof_change_date = str(date[prof_change.index(min(prof_change))])  
    print("Average Change: $", round(avg_prof_change))
    print("Greatest Increase in Profits:", max_prof_change_date,"($", max_prof_change,")")
    print("Greatest Decrease in Profits:", min_prof_change_date,"($", min_prof_change,")")
