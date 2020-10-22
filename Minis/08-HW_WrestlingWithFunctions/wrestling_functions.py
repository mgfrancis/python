import os
import csv

# Path to collect data from the Resources folder

# Define the function and have it accept the 'wrestlerData' as its sole parameter

# Find the total number of matches wrestled

# Find the percentage of matches won

# Find the percentage of matches lost

# Find the percentage of matches drawn

# Print out the wrestler's name and their percentage stats

# Read in the CSV file

wrestling_csv = os.path.join('D:\\My_Repos_Python\\python\\Minis\\08-HW_WrestlingWithFunctions','Resources','WWE-Data-2016.csv')

def print_percentages(wrestlerData): 

    name = str(wrestlerData[0])
    wins = int(wrestlerData[1])
    loss = int(wrestlerData[2])
    drawn = int(wrestlerData[3])
     
    #calculate percentages
    total_matches = wins + loss + drawn
    won_matches = (wins / total_matches) * 100
    lost_matches = (loss / total_matches) * 100
    drawn_matches = (drawn/ total_matches) * 100     

    print(f"Stats for {name}")
    print(f"WIN PERCENT: {won_matches}")
    print(f"LOSS PERCENT: {lost_matches}")
    print(f"DRAWN PERCENT: {drawn_matches}")
    
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")
    
    
    # Loop through the data
    for row in csvreader:
        
          
    # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)
            
            
        
      