# Lesson-11 | Homework

#1 Create your own virtual environment and install some python packages.

import pandas as pd
import numpy as np
import requests

#2 Create custom modules.
#   Create math_operations.py module. Define add, subtract, multiply and divide functions in it. 
#   (All functions accept two arguments in this task)
#   Create string_utils.py module. Define reverse_string and count_vowels functions in it. 
#   (All functions accept one argument in this task)

# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)

# main.py

from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels

def main():
    print("=== Math Operations ===")
    print(f"add(10, 5)       = {add(10, 5)}")
    print(f"subtract(10, 5)  = {subtract(10, 5)}")
    print(f"multiply(10, 5)  = {multiply(10, 5)}")
    try:
        print(f"divide(10, 5)    = {divide(10, 5)}")
        print(f"divide(10, 0)    = {divide(10, 0)}")
    except ZeroDivisionError as e:
        print(f"divide(10, 0)    = Error: {e}")

    print("\n=== String Utils ===")
    text = "Hello World"
    print(f"Original: {text}")
    print(f"Reversed: {reverse_string(text)}")
    print(f"Vowel count: {count_vowels(text)}")

    text2 = "Education"
    print(f"\nText: {text2}")
    print(f"Reversed: {reverse_string(text2)}")
    print(f"Vowel count: {count_vowels(text2)}")

if __name__ == "__main__":
    main()

#3 Create custom packages.
#    Create geometry package.
# geometry\
#      __init__.py
#      circle.py

#__init__.py
from .circle import area as circle_area
from .circle import circumference as circle_circumference

__all__ = ['circle_area', 'circle_circumference']

# circle.py
import math

def area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def circumference(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius

# Define calculate_area and calculate_circumference functions in circle.py. 
# These functions accept one argument(radius).

from geometry import circle_area, circle_circumference

def main():
    r1 = 5
    r2 = 3.5

    try:
        print(f"Circle (r={r1}):")
        print(f"  Area         = {circle_area(r1):.4f}")
        print(f"  Circumference = {circle_circumference(r1):.4f}\n")

        print(f"Circle (r={r2}):")
        print(f"  Area         = {circle_area(r2):.4f}")
        print(f"  Circumference = {circle_circumference(r2):.4f}\n")

        # Test error handling
        print(f"Circle (r=-1):")
        circle_area(-1)
    except ValueError as e:
        print(f"  Error: {e}")

if __name__ == "__main__":
    main()

#   Create file_operations package.
#  file_operations\
#      __init__.py
#      file_reader.py
#      file_writer.py

#      __init__.py
from .file_reader import read_file
from .file_writer import write_file

__all__ = ['read_file', 'write_file']


# Define read_file function in file_reader.py. This function accepts one argument(file_path). 
# Define write_file function in file_writer.py. This function accepts two arguments(file_path, content).

# file_operations/file_reader.py
def read_file(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File not found -> {file_path}")
    except PermissionError:
        raise PermissionError(f"Error: Permission denied reading -> {file_path}")
    except OSError as e:
        raise OSError(f"Error reading file -> {e}")
    

# file_operations/file_writer.py
def write_file(file_path: str, content: str) -> None:
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except PermissionError:
        raise PermissionError(f"Error: Permission denied writing -> {file_path}")
    except OSError as e:
        raise OSError(f"Error writing file -> {e}")
    
# test_package.py
from file_operations import read_file, write_file

def main():
    test_content = "Hello from file_operations!\nThis is line 2.\nLine 3: Success!"
    output_file = "output_test.txt"

    try:
        print("Writing to file...")
        write_file(output_file, test_content)
        print(f"Success: File written -> {output_file}")

        print("\nReading file back...")
        content = read_file(output_file)
        print("File content:")
        print("-" * 40)
        print(content)
        print("-" * 40)

        if content == test_content:
            print("Test PASSED: Content matches!")
        else:
            print("Test FAILED: Content mismatch.")

    except Exception as e:
        print(f"Test FAILED: {e}")

if __name__ == "__main__":
    main()

