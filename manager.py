import mysql.connector
import matplotlib.pyplot as plt
from datetime import date

# ---------------------- Database Setup ----------------------
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"  # 🔹 change to your MySQL root password
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS expense_db")
    cursor.execute("USE expense_db")

    # Create Tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS category (
        category_id INT AUTO_INCREMENT PRIMARY KEY,
        category_name VARCHAR(50) UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expense (
        expense_id INT AUTO_INCREMENT PRIMARY KEY,
        category_id INT,
        amount DECIMAL(10,2),
        date DATE,
        description VARCHAR(100),
        FOREIGN KEY (category_id) REFERENCES category(category_id)
    )
    """)

    # Default categories
    categories = ['Food', 'Travel', 'Bills', 'Entertainment', 'Shopping']
    for cat in categories:
        cursor.execute("INSERT IGNORE INTO category (category_name) VALUES (%s)", (cat,))
    conn.commit()

except mysql.connector.Error as e:
    print("Database connection error:", e)
    exit()

# ---------------------- Algorithm (DAA) ----------------------
def total_expense(amounts):
    """Divide & Conquer algorithm to calculate total"""
    if len(amounts) == 0:
        return 0
    if len(amounts) == 1:
        return amounts[0]
    mid = len(amounts) // 2
    left = total_expense(amounts[:mid])
    right = total_expense(amounts[mid:])
    return left + right

# ---------------------- Add New Expense ----------------------
def add_expense():
    print("\nAdd a new expense:")
    cursor.execute("SELECT category_id, category_name FROM category")
    cats = cursor.fetchall()
    for cid, cname in cats:
        print(f"{cid}. {cname}")
    
    try:
        cat_id = int(input("Enter Category ID: "))
        amount = float(input("Enter Amount (₹): "))
        desc = input("Enter Description: ")
        today = date.today()
        cursor.execute("""
            INSERT INTO expense (category_id, amount, date, description)
            VALUES (%s, %s, %s, %s)
        """, (cat_id, amount, today, desc))
        conn.commit()
        print("✅ Expense added successfully!\n")
    except Exception as e:
        print("❌ Error adding expense:", e)

# ---------------------- Fetch and Analyze ----------------------
def analyze_expenses():
    cursor.execute("""
    SELECT c.category_name, e.amount 
    FROM expense e 
    JOIN category c ON e.category_id = c.category_id
    """)
    rows = cursor.fetchall()

    if not rows:
        print("\n⚠ No expense data found. Add some entries first!")
        return

    category_data = {}
    for category, amount in rows:
        category_data[category] = category_data.get(category, 0) + float(amount)

    total = total_expense(list(category_data.values()))

    print("\n=== Expense Report ===")
    for cat, amt in category_data.items():
        print(f"{cat}: ₹{amt}")
    print(f"\nTotal Expense (DAA Calculation): ₹{total}")

    # ---------------------- Visualization ----------------------
    plt.figure(figsize=(6, 6))
    plt.pie(category_data.values(), labels=category_data.keys(), autopct='%1.1f%%', startangle=140)
    plt.title("Expense Distribution by Category")
    plt.show()

    plt.bar(category_data.keys(), category_data.values())
    plt.title("Expenses per Category")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.show()

# ---------------------- Main Menu ----------------------
while True:
    print("\n=== Expense Analyzer Menu ===")
    print("1. Add New Expense")
    print("2. Show Expense Report")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        analyze_expenses()
    elif choice == '3':
        print("👋 Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# Close connection
cursor.close()
conn.close()