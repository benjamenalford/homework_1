import csv
csv_path = 'PyPoll/Resources/election_data.csv'
#open the file
with open(csv_path,encoding="UTF-8") as vote_file:
    #create a csv reader
    csv_reader = csv.reader(vote_file)
    #loop through all votes (rows)
    for vote in csv_reader:
        #count the total of votes
        #save list of canidates
        #number of votes for each candidate
        print(vote)
