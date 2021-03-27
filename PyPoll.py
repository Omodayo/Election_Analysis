# The data we need to retreive, using 'indirect path' to a file
# Add our dependencies
import csv
import os
# Assign a variable to load the file from the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Initialize a total vote counter
total_votes = 0

# Candidate options
candidate_options = []
# Declare an empty dictionary
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ''
winning_count = 0
winning_percentage = 0
# Open the elction results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the csv file.
    for row in file_reader:
        # Add increment to total vote count.
        total_votes += 1 

        # Print the candidate name from each row
        candidate_name = row[2]

        # if the candidate does not match any existing candidate....
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# 1. Print total votes.
print(total_votes)

# 2. Print the candidate list.
print(candidate_options)

# 3. Print the candidate vote dictionary.
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate the candidatee list.
for candidate_name in candidate_votes:
    # Retreive vote count of a candidate
    votes = candidate_votes[candidate_name]
    #Calculate percentage of vote.
    vote_percentage = float(votes) / float(total_votes) * 100

# 4.  To do: print out each candidate's name, vote count, and percetage of votes to the terminal.
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

    # Determine the winning vote count and candidate.
    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percentage = vote percentage
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
        # And, set the winning_candidate = to the candidate's name.
        #winning_candidate = candidate_name

# 5. To do: print out the winning candidate, vote count, and percetage to terminal.
winning_candidate_summary = (
    f'-------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'-------------------------\n')
print(winning_candidate_summary)

# Close the file
election_data.close()



# Using the with statement open the file as a text file
with open(file_to_save, 'w') as txt_file:

    # Write some data to the file
    txt_file.write('Counties in the Election.\n')
    txt_file.write('--------------------------\n')
    txt_file.write('Arapahoe\nDenver\nJefferson')

# Close  the file
txt_file.close()

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# print the present time
print('The time right now is: ', now)
