# Lesson - 6 | Homework

# 1. Modify String with Underscores

# Given a string txt, insert an underscore (_) after every third character. 
# If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. 
# No underscore should be added at the end.

# Examples
# Input: hello Output: hel_lo

# Input: assalom Output: ass_alom

# Input: abcabcabcdeabcdefabcdefg Output: abc_abcab_cdeabcd_efabcdef_g

w = str(input("Enter a string: "))

vowels = set('aeiouAEIOU')

result = []
count = 0

i = 0
while i < len(w):
    result.append(w[i])
    count += 1
    if count == 3 and i < len(w) - 1:
        if w[i] in vowels or (i + 1 < len(w) and w[i + 1] == '_'):
            i += 1
            if i < len(w):
                result.append(w[i])
        result.append('_')
        count = 0
    i += 1

print(''.join(result))

# -------------------------------------------------------------------------------------- #

# 2. Integer Squares Exercise

# The provided code stub reads an integer, n, from STDIN. 
# For all non-negative integers i where 0 <= i < n, print i^2.
# Example Input:
# 5
# Example Output:
# 0
# 1
# 4
# 9
# 16

# Input Format
# The first and only line contains the integer, n.

# Constraints
# 1 <= n <= 20
# Output Format
# Print n lines, one corresponding to each i^2 where 0 <= i < n.

n = int(input("Enter a number: "))
if 1 <= n <= 20:
    for i in range(n):
        print(i * i)
else:
    print("Input must be between 1 and 20")

# -------------------------------------------------------------------------------------- #

# 3. Loop-Based Exercises
# Exercise 1: Print first 10 natural numbers using a while loop
# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Exercise 1:
n = 1
while n < 11:
    print(n)
    n += 1 

# Exercise 2:
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# -------------------------------------------------------------------------------------- #

# Exercise 3: Calculate sum of all numbers from 1 to a given number
# Example:
# Enter number 10
# Sum is: 55

n = int(input("Enter a number: "))
sum = 0

while n > 0:
    sum += n
    n -= 1
print("The sum is", sum)

# -------------------------------------------------------------------------------------- #

# Exercise 4: Print multiplication table of a given number
# Example:

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

n = int(input("Enter a number: "))

for i in range(1, 10):
    print(f"{n * i}")

# -------------------------------------------------------------------------------------- #

# Exercise 5: Display numbers from a list using a loop
# Given:

# numbers = [12, 75, 150, 180, 145, 525, 50]
# Expected Output:

# 75
# 150
# 145

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if 70 <= num <= 150:
        print(num)

# -------------------------------------------------------------------------------------- #

# Exercise 6: Count the total number of digits in a number
# Example:

# 75869
# Output: 5

n = 75869
count = 0

if n == 0:
    count = 1
else:
    while n != 0:
        n //= 10
        count += 1
print(f"Number of digits: {count}")

# -------------------------------------------------------------------------------------- #

# Exercise 7: Print reverse number pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# -------------------------------------------------------------------------------------- #

# Exercise 8: Print list in reverse order using a loop
# Given:

# list1 = [10, 20, 30, 40, 50]
# Expected Output:

# 50
# 40
# 30
# 20
# 10

list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1,-1,-1):
    print(list1[i])

# -------------------------------------------------------------------------------------- #

# Exercise 9: Display numbers from -10 to -1 using a for loop
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

n = -10
while n < 0:
    print(n)
    n += 1 

# -------------------------------------------------------------------------------------- #

# Exercise 10: Display message “Done” after successful loop execution
# Example:

# 0
# 1
# 2
# 3
# 4
# Done!

n = 0
while n < 10:
    if n == 5:
        print("Done!")
        break
    print(n)
    n += 1

# -------------------------------------------------------------------------------------- #

# Exercise 11: Print all prime numbers within a range
# Example:

# Prime numbers between 25 and 50:
# 29
# 31
# 37
# 41
# 43
# 47


lower = 25
upper = 50

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

# -------------------------------------------------------------------------------------- #

# Exercise 12: Display Fibonacci series up to 10 terms
# Example:

# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34

n = 10
a, b = 0, 1
fibonacci_numbers = []

for _ in range(n):
    fibonacci_numbers.append(str(a))
    a, b = b, a + b

print(' '.join(fibonacci_numbers))

# -------------------------------------------------------------------------------------- #

# Exercise 13: Find the factorial of a given number
# Example:

# 5! = 120

num = int(input("Enter a number:"))

factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of", num, "is", factorial)

# -------------------------------------------------------------------------------------- #

# 4. Return Uncommon Elements of Lists
# Task
# Return the elements that are not common between two lists. The order of elements does not matter.

# Examples
# Input: list1 = [1, 1, 2], list2 = [2, 3, 4]
# Output: [1, 1, 3, 4]

# Input: list1 = [1, 2, 3], list2 = [4, 5, 6]
# Output: [1, 2, 3, 4, 5, 6]

# Input: list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]
# Output: [2, 2, 5]


# 1
list1 = [1, 1, 2]
list2 = [2, 3, 4]
uncommon_elements = []

for i in list1:
    if i not in list2:
        uncommon_elements.append(i)
for j in list2:
    if j not in list1:
        uncommon_elements.append(j)
print("Uncommon elements from the lists: ", uncommon_elements)

# 2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
uncommon_elements = []

for i in list1:
    if i not in list2:
        uncommon_elements.append(i)
for j in list2:
    if j not in list1:
        uncommon_elements.append(j)
print("Uncommon elements from the lists: ", uncommon_elements)

# 3
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
uncommon_elements = []

for i in list1:
    if i not in list2:
        uncommon_elements.append(i)
for j in list2:
    if j not in list1:
        uncommon_elements.append(j)
print("Uncommon elements from the lists: ", uncommon_elements)
