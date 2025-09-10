# Lesson - 2 | Homework

# 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name =  str(input('What is your name?'))
birth = int(input('Year of birth'))

Y = 2025 - birth

print('Age = ', Y)


# 2. Extract Car Names
# Extract car names from the following text:

txt = 'LMaasleitbtui'
txt[::2] + ', ' + txt[1::2]


# 3. Extract Car Names
# Extract car names from the following text:

txt = 'MsaatmiazD'
txt[::-2] + ', ' + txt[::2]


# 4. Extract Residence Area
# Extract the residence area from the following text:

txt = "I'am John. I am from London"
txt[21:]


# 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.

txt = 'The sky is blue'
txt[::-1]


# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.

string = 'The sky is blue'
vowels = 'aeiouAEIOU'
vowel_count = len([char for char in string if char in vowels])

print(f"Number of vowels: {vowel_count}")


# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.

a = (1, 4, 6, 9, 42, 23)

print(max(a))


# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

txt = 'palindrome'
txt == txt[::-1]

print(f"'{txt} is a palindrome")


# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.

email = str(input('Email address:'))

e = email.split('@')[1]

print('Email: ', e)


# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.


import secrets
import string
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8)) 

print(password)
