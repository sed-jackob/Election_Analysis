# Election Analysis
## Election Audit Overview
A Colorado Board of Elections employee has given our team the following tasks to complete the election audit of a recent local congressional election.
1. Calculate the total number of votes cast.
2. Get turnout total and percentage of total votes for each county.
3. Get county with largest turnout.
2. Get total votes and percentage of total votes for each candidate.
5. Determine the winner of the election based on popular vote.

The board will provide a text file (csv) with election's data which we will process via a Python script and provide results to both, screen and output text file.

### Resources
- Data Source: ***Resources\election_results.csv***
- Output File: ***Analysis\election_analysis.txt***
- Software: *Python 3.6.1, Spyder 4.2.3*
## Election Audit Results
The analysis of the election show that:
- There were **369,711** votes cast in the election.
- Counties were:
  - *Jefferson*: with **10.5%** (**38,855**) of total votes
  - *Denver*: **82.8%** with (**306,055**) of total votes
  - *Arapahoe*: **6.7%** with (**24,801**) of total votes
- The county with the largest turnout was *Denver*
- The candidates were:
  - *Charles Casper Stockham* received **23.0%** of the vote and **85,213** number of votes.
  - *Diana DeGette received* **73.8%** of the vote and **272,892*** number of votes.
  - *Raymon Anthony Doane* received **3.1%** of the vote and **11,606** number of votes.
- The winner of the election was: 
  - *Diana DeGette*, who received **73.8%** of the vote and **272,892** number of votes.

Charts below visually illustrates the results:

## Election Audit Summary
This script can be modified to work for any state election. Below are two modifications that can be implemented:
1. Prompt user to enter the state's name to be analyzed. The script will then open and process the required state (provided that the data for that state is available in the Resources folder as *"state_name.csv"*) then write results to a text file named *"state_name_results.txt"*
2. 
