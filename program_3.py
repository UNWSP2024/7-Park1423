##
# Code by: Parker Jolly
# On: 10/16/2025
# Program name: US_Population
##

def main():
    # Create a list for all our data.
    all_entered_values = []
    
    while True:
        # Create a temporary list to work with and get the input as a list, seperating by spaces and commas. I would use just spaces, but the state "New Mexico" has a space in it.
        inputlist = input("Input a year, a state, and the population for that year seperated by a comma and a space or enter the word end to finish: ").split(", ")

        # Check if the user has entered end instead of population data and break out of the loop if they have.
        if inputlist[0] == 'end':
            break
        else:
        # Convert the number strings into ints (Because you can't have half a person) and add the list to all_entered_values.
            inputlist[0] = int(inputlist[0])
            inputlist[2] = int(inputlist[2])
            all_entered_values.append(inputlist)

    # Call our function using input as the year we want to find the population for.
    sum_population_for_year(all_entered_values,int(input("Enter a year to sum the population for: ")))


def sum_population_for_year(all_entered_values, year_to_sum):

    # Create a total.
    total = 0
    
    for current_data_set in all_entered_values:
        # Iterate though all the entered values and if the year part matches the year we want to find the population of, add the population part to our total.
        if current_data_set[0] == year_to_sum:
            total += current_data_set[2]

    # Print results
    print("The total population for the year", str(year_to_sum), "is", str(total) , "people.")




# Call the main function.
if __name__ == '__main__':
    main()