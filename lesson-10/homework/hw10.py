# Lesson-10 | Homework

# =============================================================================================================== #
# Homework 1. ToDo List Application
# =============================================================================================================== #
#1 Define Task Class:
# Create a Task class with attributes such as task title, description, due date, and status.
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        try:
            datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Due date must be in YYYY-MM-DD format")
        if status not in ["Pending", "Completed"]:
            raise ValueError("Status must be 'Pending' or 'Completed'")
        
        self.title = title.strip()
        self.description = description.strip()
        self.due_date = due_date
        self.status = status
    
    def mark_completed(self):
        self.status = "Completed"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        
    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                return
        
    def list_all_tasks(self):
        return [{"title": task.title, "description": task.description, 
                 "due_date": task.due_date, "status": task.status} for task in self.tasks]

    def list_incomplete_tasks(self):
        return [{"title": task.title, "description": task.description, 
                 "due_date": task.due_date, "status": task.status} 
                for task in self.tasks if task.status == "Pending"]
    
todo = ToDoList()
todo.add_task("Buy groceries", "Get milk and eggs", "2025-11-01")
todo.add_task("Finish homework", "Complete Python assignment", "2025-10-30")
todo.add_task("Call mom", "Check in about weekend plans", "2025-10-29")
print(f"All tasks: {todo.list_all_tasks()}")
todo.mark_task_completed("Finish homework")
print(f"After marking 'Finish homework' as completed: {todo.list_all_tasks()}")
print(f"Incomplete tasks: {todo.list_incomplete_tasks()}")
todo.add_task("", "Invalid task", "2025-10-31")

# =============================================================================================================== #
# Homework 2. Simple Blog System
# =============================================================================================================== #
#5 Define Post Class:
# Create a Post class with attributes like title, content, and author.
from typing import List, Optional

class Post:
    def __init__(self, title, content, author):
        self.title = title.strip()
        self.content = content.strip()
        self.author = author.strip()

class Blog:
    def __init__(self):
        self.posts: List[Post] = []

    def add_post(self, title, content, author) -> None:
        self.posts.append(Post(title, content, author))

    def list_all_posts(self) -> List[str]:
        return [str(p) for p in self.posts]
    
    def list_post_by_author(self, author) -> List[str]:
        author = author.strip().lower()
        return [str(p) for p in self.posts if p.author.lower() == author]
    
    def delete_post(self, title) -> None:
        for i, p in enumerate(self.post):
            if p.title == title:
                self.posts.pop(i)
                return
    
    def edit_post(self, old_title, new_title, new_content) -> None:
        for p in self.posts:
            if p.title == old_title:
                if new_title and new_title.strip():
                    p.title = new_title.strip()
                if new_content and new_content.strip():
                    p.content == new_content.strip()
                return
            
    def cli() -> None:
        blog = Blog()
        while True:
            print("\n=== Simple Blog System ===")
            print("1. Add post")
            print("2. List all posts")
            print("3. List posts by author")
            print("4. Delete post")
            print("5. Edit post")
            print("6. Exit")
            choice = input("Choose (1-6): ").strip()
        try:
            if choice == "1":
                title = input("Title: ").strip()
                content = input("Content: ").strip()
                author = input("Author: ").strip()
                blog.add_post(title, content, author)
                print("Post added!")

            elif choice == "2":
                posts = blog.list_all_posts()
                if posts:
                    for p in posts:
                        print(p)
                else:
                    print("No posts yet.")

            elif choice == "3":
                author = input("Author name: ").strip()
                posts = blog.list_posts_by_author(author)
                if posts:
                    for p in posts:
                        print(p)
                else:
                    print(f"No posts by '{author}'.")

            elif choice == "4":
                title = input("Title of post to delete: ").strip()
                blog.delete_post(title)
                print("Deleted.")

            elif choice == "5":
                old = input("Title of post to edit: ").strip()
                new_t = input("New title (Enter to keep): ").strip()
                new_c = input("New content (Enter to keep): ").strip()
                blog.edit_post(old,
                               new_title=new_t or None,
                               new_content=new_c or None)
                print("Edited.")

            elif choice == "8":
                blog.save_to_file()
                print("Goodbye!")

            else:
                print("Invalid option.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    print("\n=== Running automated tests ===")
    b = Blog()

    b.add_post("First Post", "Hello world!", "Alice")
    b.add_post("Python Tips", "Use list comprehensions.", "Bob")
    b.add_post("AI News", "New model released.", "Alice")

    print("\nAll posts:")
    for p in b.list_all_posts():
        print(p)

    print("\nPosts by Alice:")
    for p in b.list_posts_by_author("alice"):
        print(p)

    b.edit_post("First Post", new_title="My First Blog", new_content="Updated content.")
    print("\nAfter edit:")
    print(b.list_all_posts()[0])

    print("\nLatest 2 posts:")
    for p in b.latest_posts(2):
        print(p)

    b.delete_post("Python Tips")
    print("\nAfter deleting 'Python Tips':")
    for p in b.list_all_posts():
        print(p)

# =============================================================================================================== #
# Homework 3. Simple Banking System
# =============================================================================================================== #
import random

# --- 10. Define Account Class ---
class Account:
    def __init__(self, account_holder_name: str, initial_deposit: float = 0.0):
        self.account_number = str(random.randint(10000000, 99999999))
        self.account_holder_name = account_holder_name
        self.balance = max(0.0, initial_deposit)

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
# --- 13. Enhance Banking System: Handle Overdrafts ---
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print(f"Error: Insufficient funds. Current balance: ${self.balance:.2f}")
            return False

        self.balance -= amount
        return True

# --- 13. Enhance Banking System: Display Account Details ---
    def display_details(self):
        print("--- Account Details ---")
        print(f"  Account Number: **{self.account_number}**")
        print(f"  Holder Name:    **{self.account_holder_name}**")
        print(f"  Current Balance: **${self.balance:.2f}**")
        print("-" * 25)

    def __str__(self):
        return (f"Account({self.account_number}, {self.account_holder_name}, "
                f"Balance: ${self.balance:.2f})")
# --- 11. Define Bank Class ---
class Bank:
    """Manages a collection of accounts and provides core banking services."""
    def __init__(self):
        self.accounts: dict[str, Account] = {}

    def add_account(self, name: str, initial_deposit: float = 0.0) -> str:
        new_account = Account(name, initial_deposit)
        self.accounts[new_account.account_number] = new_account
        return new_account.account_number

    def get_account(self, account_num: str) -> Account | None:
        return self.accounts.get(account_num)

    def check_balance(self, account_num: str):
        account = self.get_account(account_num)
        if account:
            print(f"Balance for account **{account_num}**: **${account.balance:.2f}**")
        else:
            print(f"Account **{account_num}** not found.")

    def deposit_money(self, account_num: str, amount: float):
        account = self.get_account(account_num)
        if account:
            if account.deposit(amount):
                print(f"Deposited **${amount:.2f}** into account **{account_num}**.")
                print(f"New Balance: **${account.balance:.2f}**")
            else:
                print("Deposit amount must be greater than zero.")
        else:
            print(f"Account **{account_num}** not found.")

    def withdraw_money(self, account_num: str, amount: float):
        account = self.get_account(account_num)
        if account:
            if account.withdraw(amount):
                print(f"Withdrew **${amount:.2f}** from account **{account_num}**.")
                print(f"New Balance: **${account.balance:.2f}**")
        else:
            print(f"Account **{account_num}** not found.")

# --- 13. Enhance Banking System: Transfer Money ---
    def transfer_money(self, from_num: str, to_num: str, amount: float):
        if from_num == to_num:
            print("Cannot transfer money to the same account.")
            return

        from_account = self.get_account(from_num)
        to_account = self.get_account(to_num)

        if not from_account:
            print(f"Source account **{from_num}** not found.")
            return
        if not to_account:
            print(f"Destination account **{to_num}** not found.")
            return

        if amount <= 0:
            print("Transfer amount must be positive.")
            return

# Attempt to withdraw from the source account (handles overdraft check)
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            print(f"🎉 Successfully transferred **${amount:.2f}** from **{from_num}** to **{to_num}**.")
            print(f"   **{from_num}** new balance: **${from_account.balance:.2f}**")
            print(f"   **{to_num}** new balance: **${to_account.balance:.2f}**")


# --- Utility Functions for CLI ---
def get_positive_float_input(prompt: str) -> float | None:
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Input must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        return None

def get_account_number_input(bank: Bank, prompt: str) -> str | None:
    while True:
        acc_num = input(prompt).strip()
        if not acc_num:
            return None
        return acc_num


# --- 12. Create Main Program (CLI) ---
def main():
    bank = Bank()
    print("Welcome to the Simple Banking System")

# --- 14. Test the Application: Create Initial Instances ---
    acc1_num = bank.add_account("Alice Johnson", 1500.00)
    acc2_num = bank.add_account("Bob Smith", 500.00)
    print(f"Test Account 1 created: Alice Johnson (**{acc1_num}**)")
    print(f"Test Account 2 created: Bob Smith (**{acc2_num}**)")
    print("-" * 30)

    while True:
        print("\n--- Main Menu ---")
        print("1. **Add** New Account")
        print("2. **Check** Balance")
        print("3. **Deposit** Money")
        print("4. **Withdraw** Money")
        print("5. **Transfer** Money (Enhanced)")
        print("6. **Display** Account Details (Enhanced)")
        print("7. **Exit**")
        print("-" * 17)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            print("\n**--- Add New Account ---**")
            name = input("Enter Account Holder Name: ").strip()
            initial_deposit = get_positive_float_input("Enter Initial Deposit (or 0 for none): ")
            if name and initial_deposit is not None:
                if initial_deposit == 0:
                    new_num = bank.add_account(name)
                else:
                    new_num = bank.add_account(name, initial_deposit)
                print(f"\n Account created successfully! Number: **{new_num}**")
            else:
                print("Invalid input for account creation.")

        elif choice == '2':
            print("\n**--- Check Balance ---**")
            acc_num = get_account_number_input(bank, "Enter Account Number: ")
            if acc_num:
                bank.check_balance(acc_num)

        elif choice == '3':
            print("\n**--- Deposit Money ---**")
            acc_num = get_account_number_input(bank, "Enter Account Number to Deposit into: ")
            amount = get_positive_float_input("Enter Deposit Amount: ")
            if acc_num and amount is not None:
                bank.deposit_money(acc_num, amount)

        elif choice == '4':
            print("\n**--- Withdraw Money ---**")
            acc_num = get_account_number_input(bank, "Enter Account Number to Withdraw from: ")
            amount = get_positive_float_input("Enter Withdrawal Amount: ")
            if acc_num and amount is not None:
                bank.withdraw_money(acc_num, amount)

# --- Enhanced Functionality (Transfer) ---
        elif choice == '5':
            print("\n**--- Transfer Money ---**")
            from_acc = get_account_number_input(bank, "Enter **Source** Account Number: ")
            to_acc = get_account_number_input(bank, "Enter **Destination** Account Number: ")
            amount = get_positive_float_input("Enter Transfer Amount: ")

            if from_acc and to_acc and amount is not None:
                bank.transfer_money(from_acc, to_acc, amount)

# --- Enhanced Functionality (Display Details) ---
        elif choice == '6':
            print("\n**--- Display Account Details ---**")
            acc_num = get_account_number_input(bank, "Enter Account Number: ")
            account = bank.get_account(acc_num)
            if account:
                account.display_details()
            else:
                print(f"Account **{acc_num}** not found.")

        elif choice == '7':
            print("\n Thank you for using the Simple Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()
