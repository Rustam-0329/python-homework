# Lesson-8 | Homework

# Python Exception Handling: Exercises, Solutions, and Practice

# Exception Handling Exercises
# =============================================================================================================== #
# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    result = 2 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")

# =============================================================================================================== #
# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    val = int(input("Enter a number: "))
    result = 5 * val
except ValueError:
    print("Not a valid number!")

# =============================================================================================================== #
# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    with open("output.txt", "r") as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print("File does not exist! {FileNotFoundError}")

# =============================================================================================================== #
# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    val1 = int(input("Enter the first number: "))
    val2 = int(input("Enter the second number: "))
    result = val1 + val2
except:
    print("Inputs are not numerical - {TypeError}")

# =============================================================================================================== #
# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try:
    with open("movies.csv") as f:
        for line in f:
            print(line)
except:
    print("Permission issue, error type {PermissionError}")

# =============================================================================================================== #
# 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
try:
    num = (2,4,6)
    print(num[4])
except IndexError as e:
    print('This problem is', e)

# =============================================================================================================== #
# 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    while True:
        print("Dastur ishlamoqda... Ctrl+C bilan to'xtating")
except KeyboardInterrupt:
    print("\nDastur foydalanuvchi tomonidan to'xtatildi")

# =============================================================================================================== #
# 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    result = 4 / (0 * 2)
except ArithmeticError as e:
    print(f"Arithmetic Error: {e}")

# =============================================================================================================== #
# 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
try:
    with open("output.txt", "r", encoding="UTF-8") as f:
        content = f.read()
except UnicodeDecodeError as e:
    print(f"Error: {e}")

# =============================================================================================================== #
# 10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
try:
    my_list = [1, 2, 3]
    my_list.apppend(4)
except AttributeError as e:
    print(f"Error: {e}")

# =============================================================================================================== #

# Python File Input Output: Exercises, Practice, Solution

# File Input/Output Exercises

# =============================================================================================================== #

#1 Write a Python program to read an entire text file.
try:
    with open("output.txt", "r") as f:
        content = f.read()
        print("Content of file:", content)
except FileNotFoundError:
    print("File not Found")

# =============================================================================================================== #
#2 Write a Python program to read first n lines of a file.
try:
    n = int(input("Enter the number of lines to read: "))
    if n < 0:
        print("Please enter a non-negative number")
        exit()

    with open("output.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()[:n]  # Read and slice first n lines
        for line in lines:
            print(line.strip())
except FileNotFoundError:
    print("File 'output.txt' not found")

# =============================================================================================================== #
#3 Write a Python program to append text to a file and display the text.
with open("output.txt", "a") as file:
    file.write("\n" + "The exercises are tricky")

# =============================================================================================================== #
#4 Write a Python program to read last n lines of a file.
with open("output.txt", "r") as f:
    lines = f.readlines()
    last_n_lines = lines[-1:]
    for line in last_n_lines:
        print(line.strip())

# =============================================================================================================== #
#5 Write a Python program to read a file line by line and store it into a list.
lines = []
with open("output.txt", "r") as f:
    for line in f:
        lines.append(line.strip())
    print(lines)

# =============================================================================================================== #
#6 Write a Python program to read a file line by line and store it into a variable.
with open("output.txt", "r") as f:
    l = [line.strip() for line in f]
print(l)

# =============================================================================================================== #
#7 Write a Python program to read a file line by line and store it into an array.
array = []
with open("output.txt", "r") as f:
    for line in f:
        array.append(line.strip())
    print(array)

# =============================================================================================================== #
#8 Write a Python program to find the longest words.
with open("output.txt", "r") as f:
    words = f.read().split()
    for line in lines:
        longest_word = max(words, key = len)
    print(longest_word)

# =============================================================================================================== #
#9 Write a Python program to count the number of lines in a text file.
with open("output.txt", "r") as f:
    line_count = sum(1 for line in f)
print(line_count)

# =============================================================================================================== #
#10 Write a Python program to count the frequency of words in a file.
word_freq = {}
with open("output.txt", "r") as f:
    content = f.read().lower()
    for char in ".,!?;:'\"()\n":
        content = content.replace(char, " ")
    words = content.split()
    for word in words:
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1
if word_freq:
    print("Word frequencies:")
    for word, count in sorted(word_freq.items()):
        print(f"{word}: {count}")
else:
    print("No words were count")

# =============================================================================================================== #
#11 Write a Python program to get the file size of a plain file.
import os

with open("output.txt", "r") as f:
    file_size = os.path.getsize("output.txt")
    print(f"File size is {file_size} bytes")

# =============================================================================================================== #
#12 Write a Python program to write a list to a file.
file = "fruits.txt"
data_list = [
        "Apple",
        "Banana",
        "Cherry",
        "Date",
        "Elderberry",
        "Fig",
        "Grape"
    ]

with open("fruits.txt", "w") as f:
    for i in data_list:
        f.write(i + '\n')

# =============================================================================================================== #
#13 Write a Python program to copy the contents of a file to another file.
o = "output.txt"
f = "fruits.txt"

with open(o, "r") as source, open(f, "w") as fruits:
    for line in source:
        fruits.write(line)
print(f"Successfully copied contents from {o} to {f}")

# =============================================================================================================== #
#14 Write a Python program to combine each line from the first file with the corresponding line in the second file.
o = "output.txt"
f = "fruits.txt"
with open(o, "r") as f1, open(f, "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        max_lines = max(len(lines1), len(lines2))
        for i in range(max_lines):
            line1 = lines1[i].strip() if i < len(lines1) else ""
            line2 = lines2[i].strip() if i < len(lines2) else ""
            if line1 or line2:
                print(line1 + " " + line2)

# =============================================================================================================== #
#15 Write a Python program to read a random line from a file.
import random

line_count = 0
with open("output.txt", "r") as f:
    for line in f:
        line_count += 1
        if random.random() < 1 / line_count:
            selected_line = line.strip()
    print(selected_line)

# =============================================================================================================== #
#16 Write a Python program to assess if a file is closed or not.
file_path = "output.txt"

with open(file_path, 'r') as file:
    if not file.closed:
        print("File is open!")
print("File is now closed!" if file.closed else "File is still open!")

# =============================================================================================================== #
#17 Write a Python program to remove newline characters from a file.
with open("output.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f if line.strip()]
print(lines)

# =============================================================================================================== #
#18 Write a Python program that takes a text file as input and returns the number of words in a given text file.
word_count = 0
with open('output.txt', 'r') as file:
    for line in file:
        words = line.split()
        word_count += len(words)
print("The number of words:", word_count)

# Note: Some words can be separated by a comma with no space.
# =============================================================================================================== #
#19 Write a Python program to extract characters from various text files and put them into a list.
characters = []
with open('output.txt', 'r') as file:
    content = file.read()
    characters.extend(list(content))
print(characters)

# =============================================================================================================== #
#20 Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
import string
import os
directory = "."
try:
    os.makedirs(directory, exist_ok=True)
    file_paths = []
    for letter in string.ascii_uppercase:
        file_path = os.path.join(directory, f"{letter}.txt")
        with open(file_path, 'w') as file:
            pass  
        file_paths.append(file_path)
    print(f"Created {len(file_paths)} files: {', '.join(file_paths)}")
except OSError as e:
    print(f"Error: Failed to create files - {str(e)}")

# =============================================================================================================== #
#21 Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.
import string
import os

file_path = "alphabet.txt"
letters_per_line = 5
directory = "."

try:
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, file_path)

    letters = list(string.ascii_uppercase)

    with open(file_path, 'w') as file:
        for i in range(0, len(letters), letters_per_line):
            chunk = letters[i:i + letters_per_line]
            file.write(" ".join(chunk) + "\n")
    
    print(f"File '{file_path}' created with {letters_per_line} letters per line")
except OSError as e:
    print(f"Error: Failed to create file - {str(e)}")

