##
# Code by: Parker Jolly
# On: 10/16/2025
# Program name: Coordinates
##

# Import
import math

def main():
    # Loop so program can be ran multiple times
    while True:
        try:
            # Create tuples using input instead of numbers
            pos1 = (
                    float(input("Enter x1: ")),
                    float(input("Enter y1: ")),
                    float(input("Enter z1: ")),
                    )
            pos2 = (
                    float(input("Now enter x2: ")),
                    float(input("Enter y2: ")),
                    float(input("Enter z2: ")),
                    )
        except:
            # Handle input errors
            print("Your last input was not a proper number. Ending program...")
            break
        
        # Call our distancebetween function inside the print statement
        print("The distance between the 2 points is " + str(distancebetween(pos1,pos2)))

def distancebetween(pos1,pos2):
    
    # Return the distance and run the distance equation in the return statement
    return math.sqrt(

        (pos1[0] - pos2[0])**2 + 
        (pos1[1] - pos2[1])**2 + 
        (pos1[2] - pos2[2])**2
    )

# Run main
if __name__ == "__main__":
    main()