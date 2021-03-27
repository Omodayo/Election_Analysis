# REPITION STATEMENTS
# This is refer to as 'for' loop - using a code to perform same task over and over
# There are 2 types;
# 1) 'condition-controlled or 'while' loops
#        uses a true or false condition to control the number of times that it repeats, 
#        like asking a user if they want to continue with their online shopping after they 
#        add something to their "basket." This type of loop is also called a 'while' loop.
# 2) 'count-controlled' or 'for' loops'
#        repeats a specific number of times depending on the conditions, such as getting 
#        all the items in a list. This type of loop is also called a 'for' loop.

# WHILE LOOPS
# This test if a condition is true & perform a task if true. This type of loop has 2 parts;
# 1) A condition that is tested for a true/false value, and
# 2) A statement(s) that are repeated as long as the condition is true

x =0
while x <= 5:
    print(x)
    x = x + 1

# FOR LOOPS
#This loop  iterates/runs for a specific number of times before it stops, and can be written like 'if' and 'if-else' statement

# for item in [items]
#     statement 1
#     statement 2 i.e

counties = []
counties = ['Arapahoe', 'Denver', 'Jefferson']

# declare a variable, county

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

counties_dict ={}
counties_dict['Arapahoe'] = 422829
counties_dict['Denver'] = 463353
counties_dict['Jefferson'] = 432438
print(counties_dict)

#To get the keys of a dictionary using a for loop
for county in counties_dict:
    print(county)
#         or
for county in counties_dict.keys():
    print(county)

#To get the values of a dictionary using a for loop
for county in counties_dict.values():
    print(county)
#         or
for county in counties_dict:
    print(counties_dict.get(county))

#To get the key-value pairs of a dictionary using a for loop
# for key, value in dictionary_name.items()
#    print(key, value)    i.e

for county, voters in counties_dict.items():
    print(county, voters)

#To print each county and registered voters in counties_dict using a for loop
for county, voters in counties_dict.items():
    print(county + ' county has ' + str(counties_dict.get(county)) + ' registered voters.')
#                                  or f-string
    print(f'{county} county has {voters:,} registered voters.')
#                                  or
print(counties[0] + ' county has ' + str(counties_dict[counties[0]]) + ' registered voters.')
print(counties[1] + ' county has ' + str(counties_dict[counties[1]]) + ' registered voters.')
print(counties[2] + ' county has ' + str(counties_dict[counties[2]]) + ' registered voters.')

voting_data = []
voting_data.append({'county':'Arapahoe', 'registered_voters':422829})
voting_data.append({'county':'Denver', 'registered_voters':463353})
voting_data.append({'county':'Jefferson', 'registered_voters':432438})
print(voting_data)

#To get each dictionary in a list of dictionaries using a for loop
for county_dict in voting_data:
    print(county_dict)

for county_dict in range(len(voting_data)):
    print(voting_data[county_dict])

#To get the values from a list of dictionaries using nested for loop
for county_dict in voting_data:
    # first for loop to retrieve each dicionary
    for value in county_dict.values():
        # second for loop to get values from each dictionary using "value()"
        print(value)

#To retreive numbers of regisered voters (values) from each dictionary using for loop
for county_dict in voting_data:
    # first for loop to retrieve each dicionary
    print(county_dict['registered_voters'])

#To retreive county names (keys) from each dictionary using for loop
for county_dict in voting_data:
    # first for loop to retrieve each dicionary
    print(county_dict['county'])


#                           F-STRING
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
print(f"I received {percentage_votes}% of the total votes.")

#                       MULTIPLE F-STRING
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

#                       FORMATTING FLOATING-POINT DECIMALS (f'{value:{width}.{precision}}')
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)