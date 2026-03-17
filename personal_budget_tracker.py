#  A python personal budget tracker
import json

income_list = []
expense_list = []
file_path = "budget_data.json"

def add_income():
    while True:
        amount = float(input("Enter the income amount: "))
        description = input("Enter the income description: ")
        income_list.append({"amount": amount, "description": description})

        again = input("Do you want to add another income? (Y/N): ").upper()

        if again != "Y":
            break

def add_expense():
    while True:
        amount = float(input("Enter the expense amount: "))
        description = input("Enter the income description: ")
        expense_list.append({"amount": amount, "description": description})

        again = input("Do you want to add another expense? (Y/N): ").upper()

        if again != "Y":
            break

def view_summary():
    total_income = sum(item["amount"] for item in income_list)
    total_expense = sum(item["amount"] for item in expense_list)

    balance = total_income - total_expense

    print("\n Summary")
    print("Total income", total_income)
    print("Total expenses", total_expense)
    print("Balance", balance)

def save_data():
    with open(file_path, "w") as file:
        json.dump({"income": income_list, "expense": expense_list}, file, indent=4)
        

def main():
    
    is_running = True

    while is_running:
    
        print("Personal Budget Tracker")
        print("1.Add_income")
        print("2.Add_expense")
        print("3.View_summary")
        print("4.Quit")

        choice = input("Enter a choice (1-4): ")

        if choice == "1":
            add_income()
            save_data()
        elif choice == "2":
            add_expense()
            save_data
        elif choice == "3":
            view_summary()
        elif choice == "4":
            is_running = False
            print("Goodbye!")
        else:
            print("Invalid choice")


if __name__ == '__main__':
     main()