import os 
import csv

pypollCSV = os.path.join('election_data.csv')

with open(pypollCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)


    total_votes = {}
    for row in csvreader:
        if row[2] in total_votes: 
            total_votes[row[2]] += 1
        else:
            total_votes[row[2]]= 1

    count_of_votes = sum(total_votes.values())
    print(count_of_votes)

    print(total_votes)

    
    
