import os
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

dictionary =  {}

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
            csvpath = row[2]
            if csvpath in dictionary:
                dictionary[csvpath] = dictionary[csvpath] + 1
            else:
                dictionary[csvpath] = 1
    row_count = csvreader.line_num - 1 #subtract header
    maximum = max(dictionary, key=dictionary.get)  
    print('Election Results')
    print('-------------------------')
    print('Total Votes: ' + str(row_count))
    print('-------------------------')
    for csvpath, num in dictionary.items():
        print(csvpath + ": " + str(round((num/row_count)*100, 4)) + '% (' + str(num) + ')') 
    print('-------------------------')

    print('Winner: ' + maximum)
    print('-------------------------')     

