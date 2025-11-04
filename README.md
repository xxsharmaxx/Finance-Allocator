# Finance-Allocator
The Finance Allocator System is a software application designed to manage, track, and optimize the allocation of financial resources within an organization or for personal budgeting. It ensures that available funds are distributed efficiently among different expense categories, departments, or investment options.
# 💰 Expense Analyzer System

A **Python + MySQL-based mini project** that helps users manage and analyze their daily expenses efficiently.  
It demonstrates **Design and Analysis of Algorithms (DAA)** concepts, particularly the **Divide and Conquer** paradigm, along with **Database Management** and **Data Visualization**.

---

## 🧠 Overview

The **Expense Analyzer System** allows users to:
- Record expenses under different categories (Food, Travel, Bills, etc.)
- Store data securely in a **MySQL database**
- Automatically calculate total expenses using the **Divide & Conquer algorithm**
- Visualize expenses with **Pie Charts** and **Bar Graphs** using **Matplotlib**

This project integrates **DAA concepts**, **Python programming**, and **DBMS** — making it perfect for academic or portfolio use.

---

## ⚙️ Features

✅ Add and categorize expenses  
✅ Automatically compute total expenses  
✅ Store all data in MySQL tables  
✅ Display category-wise summaries  
✅ Generate **Pie** and **Bar** charts  
✅ Implements **Divide and Conquer** algorithm for computation  
✅ Console-based interface (simple and clean)  

---

## 🧩 Technologies Used

| Component | Technology |
|------------|-------------|
| Programming Language | Python 3.13 |
| Database | MySQL |
| Libraries | `mysql.connector`, `matplotlib` |
| IDE / Editor | VS Code |
| Algorithmic Paradigm | Divide and Conquer (DAA) |

---

## 🛠️ Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/Expense-Analyzer-System.git
cd Expense-Analyzer-System
Step 2: Install Dependencies
pip install mysql-connector-python matplotlib

Step 3: Set Up MySQL

Open MySQL command line or MySQL Workbench.

Create a user (if not already):

CREATE USER 'root'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';
FLUSH PRIVILEGES;


The program will automatically create the database expense_db and required tables.

```bash
▶️ Run the Program

Run this command in your terminal:

python expense_analyzer.py


If everything is set up correctly, you’ll see the Expense Report and visualizations.
```
🧮 Algorithm (DAA Concept)

This project uses the Divide and Conquer paradigm for calculating total expenses recursively.
####
def total_expense(amounts):
    if len(amounts) == 0:
        return 0
    if len(amounts) == 1:
        return amounts[0]
    mid = len(amounts) // 2
    left = total_expense(amounts[:mid])
    right = total_expense(amounts[mid:])
    return left + right


Time Complexity: O(n)
Paradigm: Divide and Conquer


