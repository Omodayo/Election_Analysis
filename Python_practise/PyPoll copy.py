# The data we need to retreive.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Election_Analysis', 'Resources', 'election_results.csv')

# Open the elction results and read the file.
with open(file_to_load) as election_data:
    # To do: perform analysis.
    print(election_data)

# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 4. The total number of votes each candidate won.
# 3. The percentage of votes each candidate won.
# 5. The winner of election based on popular vote.

# Close the file
election_data.close()


# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# print the present time
print('The time right now is: ', now)
