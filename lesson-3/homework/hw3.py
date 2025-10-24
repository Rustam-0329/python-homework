# Homework: List and Tuple Exercises #

# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.

fruits = ['apple', 'banana', 'kiwi', 'cherry', 'avacado']
print(fruits[2])

# ----------------------------------------------------------------------------------------------------- #

# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.
a = [1, 6, 9, 4, 3]
b = [2, 5, 7, 8, 0]

# 1
concatenate_list = a + b
print(concatenate_list)

# 2
a.extend(b)
print(a)

# ----------------------------------------------------------------------------------------------------- #

# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

list = [13, 45, 32, 'a', 4, 'f']
first = list[0]
middle = len(list) // 2
last = list[-1]

print(f"The first element: {first}, the middle element: {middle}, the last element: {last}")

# ----------------------------------------------------------------------------------------------------- #

# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.

movies = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'The Lord of the Rings', 'Pulp Fiction']
tpl_mov = tuple(movies)
print(type(tpl_mov))

# ----------------------------------------------------------------------------------------------------- #

# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.

cities = ['London', 'Vienna', 'Berlin', 'Paris', 'Madrid']
element = "Paris"

if element in cities:
    print(f"{element} exists in the list")
else:
    print(f"{element} does not exist in the list")

# ----------------------------------------------------------------------------------------------------- #

# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.

nums = [12, 56, 78, 92, 23, 31]
dublicate = [i for i in nums for _ in range(2)]
print(dublicate)

# ----------------------------------------------------------------------------------------------------- #

# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.

list = ['Abror', 'Jamshid', 'Rustam', 'Bobur']
list[0], list[3] = list[3], list[0]

print(list)

# ----------------------------------------------------------------------------------------------------- #

# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tpl[3:7])

# ----------------------------------------------------------------------------------------------------- #

# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.

colors = ['red', 'grey', 'blue', 'black', 'white', 'blue', 'yellow']
a = 'blue'

count = colors.count(a)
print(f"The element {a} appears {count} times.")

# ----------------------------------------------------------------------------------------------------- #

# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".

animals = ('dog', 'wolf', 'bear', 'lion', 'monkey')
index_lion = animals.index('lion')
print(f"The index of 'lion' is: {index_lion}")

# ----------------------------------------------------------------------------------------------------- #

# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.

tpl1 = (123, 485, 223)
tpl2 = (34, 77, 89)

merge = tpl1 + tpl2
print(merge)

# ----------------------------------------------------------------------------------------------------- #

# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.

list = [12, 34, 56, 79, 87, 27]
tuple = (34, 54, 66, 88, 72)
length_l = len(list)
length_t = len(tuple)

print(f"The length of the list is {length_l} and the tuple is {length_t}")

# ----------------------------------------------------------------------------------------------------- #

# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.

tpl = (2, 6, 9, 19, 45)
my_list = [*tpl]

print(type(my_list))

# ----------------------------------------------------------------------------------------------------- #

# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.

tpl = (2, 6, 9, 19, 45)

max_num = max(tpl)
min_num = min(tpl)

print(f"The max number is: {max_num} and min number is: {min_num}")

# ----------------------------------------------------------------------------------------------------- #

# 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.

tpl2 = ("What a beautiful day?")
print(tpl2[::-1])
