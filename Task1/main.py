from core.manager import FinanceManager

def main():
    app = FinanceManager()
    app.load_data()

    while True:
        print("\n" + "="*50)
        print("     Personal Finance Tracker System")
        print("="*50)
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        choice = input("\nEnter choice (1-4): ")

        if choice == "1":
            amount = float(input("Amount: "))
            cat = input("Category (e.g. Salary, Investment): ")
            app.add_transaction("Cash Wallet", amount, cat, True)
            print("✅ Income recorded!")
        elif choice == "2":
            amount = float(input("Amount: "))
            cat = input("Category (e.g. Food, Transport): ")
            app.add_transaction("Cash Wallet", amount, cat, False)
            print("✅ Expense recorded!")
        elif choice == "3":
            app.show_summary()
        elif choice == "4":
            print("👋 Thanks for using! Data saved.")
            break
        else:
            print("❌ Invalid input, please try again")

if __name__ == "__main__":
    main()
