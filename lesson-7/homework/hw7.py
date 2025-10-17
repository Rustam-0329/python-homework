# Lesson-7 | map | filter | lamda

# Task
# Learn about map and filter functions, and be prepared to explain them in class. 
# Provide examples using these functions with lambda expressions.

# A. The map Function. 
# The map function applies a given function to each item in an iterable and returns an iterator with the transformed results.
# Ex:
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  
# Output: [1, 4, 9, 16, 25]

# Ex: Multiple Iterables
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
sums = map(lambda x, y: x + y, numbers1, numbers2)
print(list(sums))  
# Output: [11, 22, 33]

# Ex: 
n = int(input())
squares = map(lambda x: x**2, range(n))
for square in squares:
    print(square)
# n=5, 
# Output: 
# 0
# 1
# 4
# 9
# 16


# B. The filter Function
# The filter function applies a predicate function (returning True or False) to each item 
# in an iterable and returns an iterator with only the elements for which the predicate returns True.

# Ex:
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  
# Output: [2, 4, 6]

# Ex:
values = [0, 1, "", "hello", None, False, 42]
truthy = filter(None, values)
print(list(truthy))  
# Output: [1, "hello", 42]

# Ex:
numbers = [12, 75, 150, 180, 145, 525, 50]
filtered = filter(lambda x: 70 <= x <= 150, numbers)
for num in filtered:
    print(num)


# C. Key difference betweeen map and filter
# Feature       | map                                         | filter
# ----------------------------------------------------------------------------------------------------------#
# Purpose       | Transforms each element                     | Selects elements based on a condition
# Function      | Returns any value                           | Returns True or False
# Output Size   | Same as input (one output per item)         | Subset of input (only True items)
# Example       | "map(lambda x: x*2, [1, 2, 3]) → [2, 4, 6]" | "filter(lambda x: x > 1, [1, 2, 3]) → [2, 3]"


# D. Practical Use Cases
# Map:
# Converting data types: map(int, ["1", "2", "3"]) → [1, 2, 3].
# Applying calculations: map(lambda x: x * 1.1, prices) for a 10% price increase.
# Formatting strings: map(str.upper, ["a", "b", "c"]) → ["A", "B", "C"].

# Filter:
# Removing outliers: filter(lambda x: 0 <= x <= 100, scores) to keep valid test scores.
# Selecting specific items: filter(lambda x: x.endswith(".txt"), files) for text files.
# Cleaning data: filter(lambda x: x is not None, data) to remove None values.

# -------------------------------------------------------------------------------------- #
# Problems
# 1. is_prime(n) funksiyasi
# is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.

# Misollar:
# Kiritish:
# 4
# Natija:
# False
# (Izoh: 4 soni tub emas, chunki u 2 ga bo'linadi.)

# Kiritish:
# 7
# Natija:
# True
# (Izoh: 7 soni faqat 1 va o'ziga bo'linadi, ya'ni tub son.)

def is_prime(n):
    if n > 0:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
            return True
    return False


n = int(input("Enter a number: "))
is_prime(n)

# -------------------------------------------------------------------------------------- #
# 2. digit_sum(k) funksiyasi
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

# Misollar:
# Kiritish:
# 24
# Natija:
# 6
# (Izoh: 24 sonining raqamlari yig'indisi: 2 + 4 = 6.)

# Kiritish:
# 502
# Natija:
# 7
# (Izoh: 502 sonining raqamlari yig'indisi: 5 + 0 + 2 = 7.)

def digit_sum(k):
    sum = 0
    while k > 0:
        sum += k % 10
        k //= 10
    return sum

digit_sum(502)

# -------------------------------------------------------------------------------------- #
# 3. Ikki sonning darajalari
# Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

# Misol:
# Kiritish:
# 10
# Natija:
# 2 4 8
# (Izoh: 10 dan kichik yoki teng bo'lgan 2 ning darajalari: 2, 4, 8.)

def is_sqr(N):
    k = 1
    while True:
        pwr = 2 ** k
        if pwr <= N:
            print(pwr, end=" ")
            k += 1
        else:
            break
    print()

is_sqr(10)

