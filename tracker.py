import csv
import datetime
import os
import re
from tabulate import tabulate

class Tracker:
    fieldNames = ["type", "amount", "date"]
    matching_rows = []

    def __init__(self, file):
        self.file = file
        self.file_exists = os.path.exists(self.file)

    def add_transaction(self, type, amount, date):
        with open(self.file, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldNames)

            if not self.file_exists:
                writer.writeheader()

            writer.writerow({"type": type, "amount": amount, "date": date})


    def calculate_savings(self, startDate, endDate):
        if not self.file_exists:
            return f"This file does not exist"

        elif self.file == "":
            return f"The file is empty, so there is nothing to calculate"

        elif self.file_exists:
            income = 0
            expenses = 0

            income = float(income)
            expenses = float(expenses)

            with open(self.file, "r") as file:
                reader = csv.DictReader(file)
                self.matching_rows = []

                for row in reader:
                    row_date = row["date"]

                    if startDate <= row_date <= endDate:
                        self.matching_rows.append(row)

                for match in self.matching_rows:
                    if match["type"] == "income":
                        income += float(match["amount"])

                    elif match ["type"] == "expense":
                        expenses += float(match["amount"])

                saving = income - expenses

                if saving < 0:
                    return f"You lost ${saving * -1}"

                elif saving > 0:
                    return f"You saved ${saving}"

    def generate_summary(self):
        if not self.file_exists:
            print(f"This file does not exist")
            return False

        elif self.file == "":
            print(f"The file is empty, so there is nothing to calculate")
            return False

        elif self.file_exists:
            table = []

            with open(self.file, "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    table.append(row)

            print(tabulate(table, headers = "keys", tablefmt = "grid"))
            return True

    def clear_data(self):
        with open(self.file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows([])

def main():
    while True:
        file = input("What csv file would you like to access? ")
        if file.endswith(".csv"):
            break
        else:
            continue

    tracker = Tracker(file)

    print("What Would you like to do today?")
    print("1. Add Transaction")
    print("2. Calculate Savings")
    print("3. Generate Summary")
    print("4. Clear Data")

    while True:
        try:
            choice = int(input("Choose options 1 to 4: "))
            if choice < 1 or choice > 4:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please insert a valid option: ")

    if choice == 1:
        while True:
            try:
                type = input("Income or Expense? ").lower().strip()
                if type not in ["income", "expense"]:
                    raise ValueError
                else:
                    while True:
                        amount = input("Insert Amount: ").strip()
                        try:
                            amount = float(amount)
                            if amount < 0:
                                raise ValueError("Amount can't be negative.")
                            amount = f"{amount:2f}"
                            break
                        except ValueError:
                            print("Invalid amount. Please enter a valid number.")
                            continue

                    tracker.add_transaction(type, amount, datetime.datetime.now().date())
                    print("Transaction added successfully.")
                    break
            except ValueError:
                print("Income or Expense can only be entered, case-insensitively.")

    elif choice == 2:
        def validate(period):
            if re.match(r"^\d{4}-\d{2}-\d{2} to \d{4}-\d{2}-\d{2}$", period):
                return True

            else:
                return False

        while True:
            print("Date range must be in the format (YYYY-DD-MM to YYYY-DD-MM)")
            date_range = input("Insert date range for calculating savings: ").strip().lower()
            validated = validate(date_range)

            if validated:
                break

            elif validated == False:
                print("Invalid format, must be (YYYY-MM-DD to YYYY-MM-DD)")
                continue

        startDate, _, endDate = date_range.split()

        calculated_saving = tracker.calculate_savings(startDate, endDate)
        print(calculated_saving)

    elif choice == 3:
        generated = tracker.generate_summary()

        if generated:
            print("Summary Generated")

        elif generated == False:
            print("Summary was not generated")

    elif choice == 4:
        tracker.clear_data()
        print("Data cleared.")

if __name__ == "__main__":
    main()