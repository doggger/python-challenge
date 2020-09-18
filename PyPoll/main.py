# Importing Modules and Setting Path
import os
import csv

csvpath = os.path.join('resources', 'election_data.csv')

#Setting Variables and Opening csv file and pulling off headers
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    Total_Votes = 0
    Winner = ' '
    candidates = []
    votes =[]
    counts = []
    percentages = []
    y = 0
#loops through data and performs calculations
    for row in csvreader:
    #counting total votes
        Total_Votes = Total_Votes + 1

    #creates a list of candidates who received votes and a list of votes
        if row[2] not in candidates:
            candidates.append(row[2])
        votes.append(row[2])
    
#tabulates vote counts and percentages
for candi in candidates:
    counts.append(votes.count(candi))
    percentages.append(round(votes.count(candi) / Total_Votes * 100.000, 3))

#picks a winner
for x in counts:
    if x > y:
        y = x
Winner = candidates[counts.index(y)]

# creates list for printing and prints to text and terminal
Dash = '---------------------------'

print('Election Results')
print(Dash)
z = 0
for candi in candidates:
    print(candi, ': ', str(percentages[z]), '% (', str(counts[z]), ")")
    z = z +1
print(Dash)
print('Winner: ', Winner)
print(Dash)

z = 0
textpath = os.path.join('analysis', 'analysis.txt')
L1 = ['Election Results \n',
Dash,  '\n',
'Total Votes: ', str(Total_Votes), '\n',
Dash, '\n']

L3 = [Dash, '\n',
'Winnner: ', Winner, '\n',
Dash, '\n']

with open(textpath, 'w') as textfile:
    textfile.writelines(L1)
    for candi in candidates:
        L2 = [candi, ': ', str(percentages[z]), '% (', str(counts[z]), ')', '\n']
        textfile.writelines(L2)
        z = z + 1
    textfile.writelines(L3)