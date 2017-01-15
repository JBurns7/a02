"""
Problem:

    You have been asked to write an algorithm to calculate 
    the average weight of some fruit. The program should
    do the following things:

    * Ask the user how many weights they want to enter.

    * Ask the user to enter the weights.

    * Calculate and print the mean weight, rounded to 2dp.

    
Example:

    How many weights do you want to enter?  3
    Enter a weight: 21
    Enter a weight: 10
    Enter a weight: 14
    The average weight is: 15.00


Hints:

    `a = int(input("Some prompt"))`  will ask the user for an
    input, turn it to an integer and store it as `a`

    round(num, 2) will round a decimal to 2dp.


Tests:

    There are no accompanying tests for this problem because it
    requires user input. You will need to test it manually.

"""

def mean_weight():
    
    mean = 0
    
    amount = int(input("How many weights? "))
    
    for i in range(0, amount):
         weights = int(input("Enter the weights:" )
         mean = mean + weights
                       
    mean = mean // amount
    round(mean, 2)
    
    print("The average weight is:", mean)











