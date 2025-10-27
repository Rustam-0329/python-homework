# Lesson-9 | Homework

# Object-Oriented Programming (OOP) Exercises
# =============================================================================================================== #
# 1. Circle Class
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

# Cicle area = pi*r**2
# perimeter aka circumference = 2*pi*r
import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive!")
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius

c = Circle(6)
print(f"Area: {c.area(): .2f}")
print(f"Circumference: {c.circumference(): .2f}")

# =============================================================================================================== #
# 2. Person Class
# Write a Python program to create a Person class. Include attributes like name, country, and date of birth. 
# Implement a method to determine the person's age.
from datetime import datetime

class Person:
    def __init__(self, birth_date):
        self.birth_date = birth_date
    
    def calculate_age(self):
        current_date = datetime.now()
        age = current_date.year - self.birth_date.year
        if (current_date.month, current_date.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

birth_date = datetime(1988, 9, 29)
person = Person(birth_date)
print(f"Age: {person.calculate_age()} years")       

# =============================================================================================================== #
# 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
    
calc = Calculator()
print(calc.add(2, 3))
print(calc.multiply(4, 4))

# =============================================================================================================== #
# 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. 
# Include methods to calculate its area and perimeter. 
# Implement subclasses for different shapes like Circle, Triangle, and Square.

# cicle area = pi*r**2, circumference = 2*pi*r
# triangle area = (h * b)/2, perimeter = a + b + c
# square area = a**2, perimeter = 4*a

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Triangle(Shape):
    def __init__(self, a_side, b_side, c_side, height):
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side
        self.height = height

    def area(self):
        return (self.b_side * self.height) / 2
    
    def perimeter(self):
        return self.a_side + self.b_side + self.c_side
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

circle = Circle(2)
triangle = Triangle(3, 4, 5, 2.4)
square = Square(3)

print(f"Circle - Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")
print(f"Triangle - Area: {triangle.area():.2f}, Perimeter: {triangle.perimeter():.2f}")
print(f"Square - Area: {square.area():.2f}, Perimeter: {square.perimeter():.2f}")

# =============================================================================================================== #
# 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree. 
# Include methods for inserting and searching for elements in the binary tree.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node is not None and node.value == value
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
bst = BinaryST()
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    bst.insert(value)

print(f"Inserted values: {values}")
print(f"Search 40: {bst.search(40)}")
print(f"Search 90: {bst.search(90)}") 

# =============================================================================================================== #
# 6. Stack Data Structure
# Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Stack: {stack.items}")  # Output: [1, 2, 3]
print(f"Popped: {stack.pop()}")  # Output: Popped: 3
print(f"Stack after pop: {stack.items}")  # Output: [1, 2]

# =============================================================================================================== #
# 7. Linked List Data Structure
# Write a Python program to create a class representing a linked list data structure. 
# Include methods for displaying linked list data, inserting, and deleting nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if not current.next:
            raise ValueError(f"Value {data} not found in list")
        current.next = current.next.next

    def display(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
        
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
print(f"Linked List: {ll.display()}")  # Output: [1, 2, 3]
ll.delete(2)
print(f"After deleting 2: {ll.display()}")  # Output: [1, 3]
ll.insert(4)
print(f"After inserting 4: {ll.display()}")  # Output: [1, 3, 4]
try:
    ll.delete(5)  # Raises error
except ValueError as e:
    print(f"Error: {e}")

# =============================================================================================================== #
# 8. Shopping Cart Class
# Write a Python program to create a class representing a shopping cart. 
# Include methods for adding and removing items, and calculating the total price.

class Shopping:
    def __init__(self):
        self.items = []

    def add(self, name, price):
        self.items.append({"name": name.strip(), "price": price})

    def remove(self, name):
        for i, item in enumerate(self.items):
            if item["name"] == name:
                return self.items.pop(i)
    
    def calc(self):
        return sum(item["price"] for item in self.items)
    

cart = Shopping()
cart.add("Apple", 10)
cart.add("Banana", 8)
cart.add("Kiwi", 11)

print(f"Cart: {[item['name'] for item in cart.items]}")
print(f"Total price: ${cart.calc():.2f}")
cart.remove("Banana")
print(f"After removing Banana: {[item['name'] for item in cart.items]}")
print(f"New total price: ${cart.calc():.2f}")

# =============================================================================================================== #
# 9. Stack with Display
# Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing, popping, and displaying elements.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Stack: {stack.items}")  
print(f"Popped: {stack.pop()}") 
print(f"Stack after pop: {stack.items}") 

# =============================================================================================================== #
# 10. Queue Data Structure
# Write a Python program to create a class representing a queue data structure. 
# Include methods for enqueueing and dequeueing elements.
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f"Queue: {queue.items}") 
print(f"Dequeued: {queue.dequeue()}") 
    
# =============================================================================================================== #
# 11. Bank Class
# Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, customer_name, initial_balance=0):
        self.accounts[account_number] = {"name": customer_name.strip(), "balance": initial_balance}

    def deposit(self, account_number, amount):
        self.accounts[account_number]["balance"] += amount

    def withdraw(self, account_number, amount):
        self.accounts[account_number]["balance"] -= amount

    def transfer(self, from_account, to_account, amount):
        self.accounts[from_account]["balance"] -= amount
        self.accounts[to_account]["balance"] += amount

    def get_balance(self, account_number):
        return self.accounts[account_number]["balance"]

    def get_account_info(self, account_number):
        account = self.accounts[account_number]
        return {"account_number": account_number, "name": account["name"], "balance": account["balance"]}       

bank = Bank()
bank.create_account("1001", "Alice", 500)
bank.create_account("1002", "Bob", 300)
print(f"Account 1001: {bank.get_account_info('1001')}")
bank.deposit("1001", 200)
print(f"After deposit: {bank.get_balance('1001'):.2f}")  # Output: 700.00
bank.withdraw("1002", 100)
print(f"After withdrawal: {bank.get_balance('1002'):.2f}")  # Output: 200.00
bank.transfer("1001", "1002", 150)
print(f"After transfer: Alice {bank.get_balance('1001'):.2f}, Bob {bank.get_balance('1002'):.2f}")
bank.create_account("1001", "Charlie")

