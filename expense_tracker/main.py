def main():
    print("Welcome to Expense Tracker")
    print("1. Use CLI")
    print("2. Use GUI")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        from expense_tracker.ui.cli import run_cli
        run_cli()
    elif choice == '2':
        from expense_tracker.ui.gui import run_gui
        run_gui()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
