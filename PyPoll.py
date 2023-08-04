import csv
csv_path = 'PyPoll/Resources/election_data.csv'
#open the file.
total_votes =0
with open(csv_path,encoding="UTF-8") as vote_file:
    #create a csv reader
    csv_reader = csv.reader(vote_file)
    #get the header
    header = next(csv_reader)
    print(header)
    #loop through all votes (rows)
    for vote in csv_reader:
        #count the total of votes
        total_votes=total_votes+1
        #save list of canidates
        #number of votes for each candidate
        #print(vote)

#print results
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
