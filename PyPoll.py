# The data we need to retrieve (dependencies)
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

    
#1. The total number of votes cast
#2. A complsit list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
# Create a filename variable to a direct or indirect path to file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    # Write some data to the file
    txt_file.write("Counties in the Election\n-------\nArapahoe\nDenver\nJefferson")