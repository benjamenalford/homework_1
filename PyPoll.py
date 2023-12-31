import csv
csv_path = 'PyPoll/Resources/election_data.csv'
#open the file.
total_votes =0
candidates = []
candidate_votes =[]
candidates_dict = []
with open(csv_path,encoding="UTF-8") as vote_file:
    #create a csv reader
    csv_reader = csv.reader(vote_file)
    #get the header
    header = next(csv_reader)
    #loop through all votes (rows)
    for vote in csv_reader:
        #count the total of votes
        total_votes=total_votes+1
        #save list of canidates
        candidate = vote[2]
        #list logic
        if (candidate not in candidates):
            candidates.append(candidate)
            candidate_votes.append(1)
        else:
            #number of votes for each candidate
            current_votes =candidate_votes[candidates.index(candidate)]
            current_votes = current_votes+1
            candidate_votes[candidates.index(candidate)] = current_votes

#print results
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
for candidate in candidates:
    vote_count =candidate_votes[candidates.index(candidate)]
    print(f'{candidate}: 23.049% ({vote_count})')
print(f'-------------------------')
print(f'Winner: Diana DeGette')
print(f'-------------------------')
