# Lesson 5 | Homework

# Conditional Statements

# -------------------------------------------------------------------------------------- #

# 1.Determines whether a given year is a leap year.

# A year is a leap year if:
# - It is divisible by 4, and
# - It is NOT divisible by 100, unless it is also divisible by 400.

# Parameters:
# year (int): The year to be checked.

# Returns:
# bool: True if the year is a leap year, False otherwise.
# """
# if not isinstance(year, int):
#     raise ValueError("Year must be an integer.")

# return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year!")

# -------------------------------------------------------------------------------------- #

# 2. Conditional Statements Exercise

# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Input Format
# A single line containing a positive integer, n.

# Constraints
# 1 <= n <= 100
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input 0
# 3
# Sample Output 0
# Weird
# Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
# Give two solutions.

# Solution 1 with if-else statement.
try:
    n = int(input("Enter a number: "))
    if not (1 <= n <= 100):
        print("Number must be between 1 and 100")
        exit()

    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird") 

except ValueError:
    print("Please enter a valid integer")


# Solution 2 without if-else statement.
try:
    n = int(input("Enter a number: "))
    print({True: "Number must be between 1 and 100"}.get(not(1 <= n <= 100),
          {(n % 2 != 0): "Weird",
           (n % 2 == 0 and 2 <= n <= 5): "Not Weird",
           (n % 2 == 0 and 6 <= n <= 20): "Weird",
           (n % 2 == 0 and n > 20): "Not Weird"}.get(True, "Error")))
except ValueError:
    print("Please enter a valid integer")
