import csv
import os

FILENAME = "expenses.csv"
if not os.path.exists(FILENAME):
    with open(FILENAME, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Amount", "Category"])

def add_expense():
    amount = input("Amount spent: ₹")
    category = input("Category: ")
    with open(FILENAME, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([amount, category])
    print("Expense saved!\n")

def view_expenses():
    print("\n--- Expenses ---")
    with open(FILENAME, mode='r') as f:
        reader = csv.reader(f)
        next(reader)  
        for row in reader:
            print(f"₹{row[0]} on {row[1]}")
    print()

def total_spent():
    total = 0
    with open(FILENAME, mode='r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            total += float(row[0])
    print(f"\nTotal spent: ₹{total}\n")

while True:
    print("1. Add Expense\n2. View Expenses\n3. Total Spent\n4. Exit")
    choice = input("Choose: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_spent()
    elif choice == '4':
        print("Bye! 🧾")
        break
    else:
        print("Invalid option!\n")


