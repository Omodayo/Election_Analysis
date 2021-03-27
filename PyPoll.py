# The data we need to retreive, using 'indirect path' to a file
# Add our dependencies
import csv
import os
# Assign a variable to load the file from the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Open the elction results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the csv file.
    for row in file_reader:
        print(row)

    # To do: read and analyze the election data here.
    print(election_data)

# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 4. The total number of votes each candidate won.
# 3. The percentage of votes each candidate won.
# 5. The winner of election based on popular vote.

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
