# Expense Tracker

#### Description:
The Expense Tracker is a simple Python-based application that allows users to manage and track their financial transactions. It allows users to add income or expense transactions, calculate savings over a specified period, generate a summary of all transactions, and clear all stored data. The application stores the transactions in a CSV file, making it easy to maintain and analyze financial data over time.

The tracker has the following features:
- Add income or expense transactions with the amount and date.
- Calculate savings by subtracting expenses from income over a user-defined date range.
- Generate a summary of all transactions stored in the CSV file.
- Clear all stored data in the CSV file.

This project is useful for anyone looking for a simple way to track their finances without requiring complex software. It is easy to extend and adapt for other use cases as well.

#### Features:
- Add transactions (income/expense)
- Calculate savings for a specified period
- Generate a transaction summary
- Clear data from the file

#### Technologies Used:
- Python
- CSV module
- os Module
- datetime module
- re module
- tabulate module
- Pytest for unit testing

#### How to Run:
1. Clone or download this repository to your local machine.
2. Ensure that you have Python 3.x installed.
3. Run the script using the command `python project.py`.
4. Interact with the tracker via the terminal to add transactions, calculate savings, generate summaries, or clear data.

#### Testing:
Unit tests are written using Pytest and can be run using the following command:
```bash
pytest test_project.py