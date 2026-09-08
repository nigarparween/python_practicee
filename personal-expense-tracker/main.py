import json
from datetime import date

expenses = []


def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Please enter a valid amount!")
        return

    if amount <= 0:
        print("Amount must be greater than zero!")
        return

    category = input("Enter expense category: ").strip().title()

    if not category:
        print("Category cannot be empty!")
        return

    expense = {
        "amount": amount,
        "category": category,
        "date": str(date.today())
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found!")
        return
    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['category']} - "
            f"${expense['amount']:.2f} - "
            f"{expense['date']}"
     )


def view_total_expenses(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print(f"Total: ${total:.2f}")


def search_by_category(expenses):
    category = input("Enter category to search: ").strip().title()

    found = False
    total = 0

    for expense in expenses:
        if expense["category"] == category:
            print(
                f"{expense['category']} - "
                f"${expense['amount']:.2f} - "
                f"{expense['date']}"
            )

            found = True
            total = total + expense["amount"]

    if not found:
        print("Category not found!")
    else:
        print(f"Total for {category}: ${total:.2f}")


def delete_expense(expenses):
    try:
        expense_number = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    if expense_number < 1 or expense_number > len(expenses):
        print("Invalid expense number!")
        return

    expense = expenses[expense_number - 1]

    print(
        f"Deleting: {expense['category']} - "
        f"${expense['amount']:.2f} - "
        f"{expense['date']}"
    )

    expenses.remove(expense)
    print("Expense deleted successfully!")


def edit_expense(expenses):
    try:
        expense_number = int(input("Enter expense number to edit: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    if expense_number < 1 or expense_number > len(expenses):
        print("Invalid expense number!")
        return

    expense = expenses[expense_number - 1]

    try:
        new_amount = float(input("Enter new amount: "))
    except ValueError:
        print("Please enter a valid amount!")
        return

    if new_amount <= 0:
        print("Amount must be greater than zero!")
        return

    new_category = input("Enter new category: ").strip().title()

    if not new_category:
        print("Category cannot be empty!")
        return

    expense["amount"] = new_amount
    expense["category"] = new_category

    print("Expense updated successfully!")

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expenses saved successfully!")


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

        print("Expenses loaded successfully!")
        return expenses

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("No valid expense data found!")
        return []


def main():
    expenses = []

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Search by category")
        print("5. Delete Expense")
        print("6. Save Expenses")
        print("7. Load Expenses")
        print("8. Edit Expenses")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            view_total_expenses(expenses)

        elif choice == "4":
            search_by_category(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            save_expenses(expenses)

        elif choice == "7":
            expenses = load_expenses()

        elif choice == "8":
            edit_expense(expenses)

        elif choice =="9":
            save_expenses(expenses)
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
