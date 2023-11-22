import sqlite3
import datetime

# Function to create the expense table if it doesn't exist
def create_tables():
    conn = sqlite3.connect("financial_tracker.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            description TEXT,
            date TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS income (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            description TEXT,
            date TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Function to record an expense
def record_expense(amount, description):
    conn = sqlite3.connect("financial_tracker.db")
    cursor = conn.cursor()
    
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''
        INSERT INTO expenses (amount, description, date)
        VALUES (?, ?, ?)
    ''', (amount, description, date))
    
    conn.commit()
    conn.close()
    print("Expense recorded successfully.")

# Function to record income
def record_income(amount, description):
    conn = sqlite3.connect("financial_tracker.db")
    cursor = conn.cursor()
    
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''
        INSERT INTO income (amount, description, date)
        VALUES (?, ?, ?)
    ''', (amount, description, date))
    
    conn.commit()
    conn.close()
    print("Income recorded successfully.")

# Function to view monthly totals for expenses
def view_expenses():
    conn = sqlite3.connect("financial_tracker.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT strftime('%Y-%m', date) AS month, 
               description,
               amount
        FROM expenses
        ORDER BY month, date
    ''')
    
    expenses = cursor.fetchall()

    print("Month | Description | Amount")
    print("--------------------------------------")
    for expense in expenses:
        print(f"{expense[0]} | {expense[1]} | {expense[2]}")
    
    print("\nMonthly Totals:")
    cursor.execute('''
        SELECT strftime('%Y-%m', date) AS month,
               SUM(amount) AS total_expenses
        FROM expenses
        GROUP BY month
    ''')

    monthly_expenses = cursor.fetchall()

    print("Month | Total Expenses")
    print("-----------------------")
    for month in monthly_expenses:
        print(f"{month[0]} | {month[1]}")

    conn.close()

# Function to view monthly totals for income
def view_income():
    conn = sqlite3.connect("financial_tracker.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT strftime('%Y-%m', date) AS month, 
               description,
               amount
        FROM income
        ORDER BY month, date
    ''')
    
    income = cursor.fetchall()

    print("Month | Description | Amount")
    print("--------------------------------------")
    for entry in income:
        print(f"{entry[0]} | {entry[1]} | {entry[2]}")

    print("\nMonthly Totals:")
    cursor.execute('''
        SELECT strftime('%Y-%m', date) AS month,
               SUM(amount) AS total_income
        FROM income
        GROUP BY month
    ''')

    monthly_income = cursor.fetchall()

    print("Month | Total Income")
    print("--------------------")
    for month in monthly_income:
        print(f"{month[0]} | {month[1]}")

    conn.close()

# Function to view net gain or loss for a specific month
def view_net_gain_loss():
    conn = sqlite3.connect("financial_tracker.db")
    cursor = conn.cursor()

    month = input("Enter the month (YYYY-MM) to view net gain or loss: ")

    # Calculate total income for the month
    cursor.execute('''
        SELECT COALESCE(SUM(amount), 0) AS total_income
        FROM income
        WHERE strftime('%Y-%m', date) = ?
    ''', (month,))

    total_income_result = cursor.fetchone()
    total_income = total_income_result[0] if total_income_result is not None else 0

    # Calculate total expenses for the month
    cursor.execute('''
        SELECT COALESCE(SUM(amount), 0) AS total_expenses
        FROM expenses
        WHERE strftime('%Y-%m', date) = ?
    ''', (month,))

    total_expenses_result = cursor.fetchone()
    total_expenses = total_expenses_result[0] if total_expenses_result is not None else 0

    # Calculate net gain or loss
    net_total = total_income - total_expenses

    print(f"\nNet Total {month}: {net_total}")

    conn.close()

# Main program loop
while True:
    print("\nFinancial Tracker Menu:")
    print("1. Record an Expense")
    print("2. Record Income")
    print("3. View Monthly Expenses")
    print("4. View Monthly Income")
    print("5. View Net Total for Specified Month")
    print("6. Exit")
    
    choice = input("Enter your choice (1, 2, 3, 4, 5, or 6): ")
    
    if choice == '1':
        amount = float(input("Enter the expense amount: "))
        description = input("Enter a brief description: ")
        record_expense(amount, description)
    elif choice == '2':
        amount = float(input("Enter the income amount: "))
        description = input("Enter a brief description: ")
        record_income(amount, description)
    elif choice == '3':
        view_expenses()
    elif choice == '4':
        view_income()
    elif choice == '5':
        view_net_gain_loss()
    elif choice == '6':
        print("Exiting the Financial Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
