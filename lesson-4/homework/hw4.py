# Homework #4 | Python Dictionary and Set Exercises

# Dictionary Exercises
# -------------------------------------------------------------------------------------- #

# 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.

sample_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}
sorted_dict_asc = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
sorted_dict_desc = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))

print("Sorted by value (ascending):", sorted_dict_asc)
print("Sorted by value (descending):", sorted_dict_desc)

# -------------------------------------------------------------------------------------- #

# 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.

# Sample Dictionary:
{0: 10, 1: 20}
# Expected Result:
# {0: 10, 1: 20, 2: 30}

num = {0: 10, 1: 20}
num[2] = 30

print(num)

# -------------------------------------------------------------------------------------- #

# 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.

# Sample Dictionaries:
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Expected Result:
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# 1:
concat_dic1 = {**dic1, **dic2, **dic3}
print(concat_dic1)

# 2:
concat_dic2 = dic1 | dic2 | dic3
print(concat_dic2)

# -------------------------------------------------------------------------------------- #

# 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

# Sample Dictionary (n = 5):
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

d = {i:i*i for i in range(1, 6)}
print(d)

# -------------------------------------------------------------------------------------- #

# 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

# Expected Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

sqr_d = {i:i*i for i in range(1, 16)}
print(sqr_d)

# -------------------------------------------------------------------------------------- #

# Set Exercises

# 1. Create a Set
# Write a Python program to create a set.

my_set = {3, 5, 6, 9}
print(my_set)

# -------------------------------------------------------------------------------------- #

# 2. Iterate Over a Set
# Write a Python program to iterate over sets.

my_set1 = {"apple", "banana", "cherry", "date"}

for i in my_set1:
    print(i)

# -------------------------------------------------------------------------------------- #

# 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.
# 1
names = {"Akmal", "Rustam", "Javohir", "Bobur"}
names.add("Ravshan")
print(names)
# 2
new_names = {"Abdurashid", "Davron"}
names.update(new_names)
print(names)
# -------------------------------------------------------------------------------------- #

# 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.
# 1
names = {"Akmal", "Rustam", "Javohir", "Bobur"}
names.remove("Bobur")
print(names)

# 2
names = {"Akmal", "Rustam", "Javohir", "Bobur"}
names.discard("Akmal")
print(names)

# -------------------------------------------------------------------------------------- #

# 5. Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.

names = {"Akmal", "Rustam", "Javohir", "Bobur"}
check_name = "Abdurashid"

if check_name in names:
    print(f"{check_name} is present in the Set.")
else:
    print(f"{check_name} is not present in the Set.")
