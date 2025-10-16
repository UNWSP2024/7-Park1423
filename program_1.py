##
# Code by: Parker Jolly
# On: 10/16/2025
# Program name: Rainfall
##

# Create rainfall list
rainfall = []

# Ask the user for the monthy rainfall 12 times and save it to the rainfall list.
for i in range(12):
    # Use a try/except to tellt the user if they gave bad input.
    try:
        rainfall.append(float(input("Enter the amount of rainfall for month " + str(i + 1) + ": ")))
        
    except ValueError:
        print("Thats not a number.")
        print("Ending program...")
        break

# Get the sum of rainfall for the total rainfall.
print("The total rainfall for that year was " + str( sum(rainfall)))
# Get the sum of rainfall divided by the length for the average rainfall.
print("The average rainfall for that year was " + str( sum(rainfall) / len(rainfall) ))
# Get the max number in the list and first occurance of that number to tell the user the month with the most rainfall and which month it was.
print("The month with the most rainfall was month " + str( rainfall.index(max(rainfall)) + 1) + " with " + str( max(rainfall) ))
# Repeat the last step for the lowest number.
print("The month with the least rainfall was month " + str( rainfall.index(min(rainfall)) + 1) + " with " + str( min(rainfall) ))
