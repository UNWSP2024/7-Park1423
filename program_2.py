##
# Code by: Parker Jolly
# On: 10/16/2025
# Program name: Larger than n
##

def main():
    # Declare local variables
    number = 5
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Display the number.
    print('Number:', number)

    # Display the list of numbers.
    print('List of numbers:')
    print(f'{number_list}')
    
    # Display the list of numbers that are larger
    # than the number.
    print(f'List of numbers that are larger than {number}:')
    
    # Call the display_larger_than_n_list function,
    # passing a number and number list as arguments.
    display_larger_than_n_list(number, number_list)

# The display_larger_than_n_list function accepts two arguments:
# a list, and a number. The function displays all of the numbers
# in the list that are greater than the number.
def display_larger_than_n_list(n, n_list):
    # Create a empty list
    values_bigger = []

    # Iterate through the list passed to us and if the current 
    # number is bigger than n, add it to out accumulaing list.
    for current_number in n_list:
        if current_number > n:
            values_bigger.append(current_number)

    # Output results.
    print("The numbers in the list " + str(n_list) + " that are bigger than " + str(n) + " are " + str(values_bigger) + ".")
        
# Call the main function.
if __name__ == '__main__':
    main()