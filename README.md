# Election_Analysis

## Election Audit Overview
This project is initiated upon the request of a Colorado Board of election employee request to complete the election audit of a recent local congressional election,using python progamming language. The following tasks were completed at end of the election result data analysis;

1. Calculate the total votes cast during the election
2. Retreive complete list of candidates who received votes
3. Calculate the total number of votes each candidate received
4. calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular votes

## Election Audit Result
- There are 369,711 votes cast in the congressional election
- For each of thr 3 counties in the precint, the number of votes cas, and percentage of total vote cast are;
  * In Jefferson county, 10.5% of total votes is cast votes cast, and 38,855 votes
  * In Denver county, 82.8% of total votes is cast votes cast, and 306,055 votes
  * In Arapahoe county, 6.7% of total votes is cast votes cast, and 24,801 votes
- Denver is the county with the lagest number of votes
- The candidates results are;
  * Charles casper Stockham received 23.0% of the total votes and 85,213 votes
  * Diana DeGette received 73.8% of the total votes and 272,892 votes
  * Raymon Anthony Doane received 3.1% of the total votes and 11,606 votes
- The winner of the election is;
  * Diana DeGette, who received 73.8% of votes and 272,892 votes
- ![Election_Analysis_Results](https://github.com/Omodayo/Election_Analysis/blob/main/analysis/election_analysis.txt)

## Election Audit Summarry
This is a very interesting but challenging analysis. Once the code is cleane and debug to remove any cluster, this will present an automated opportunity in the future for the the electoral officials in Colorado to collate and tally their election result quickly and with less room for error. Though this code is written for a specic election, it is mutable and can be modified to be used for any election regardless of the size, number of counties, and canditates by;
  * County list and dictonary can be modified to accomodate more locations depending on the size of the election
  * Candidates list & dictionary can also be modified to accomodate more number of candidates
