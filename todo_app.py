todo = []

def show_menu( ):
    print("\nTodo App Menu:")
    print("1. Add Todo")
    print("2. View Todos")
    print("3. Delete Todo")
    print("4. Exit")

def view_todos():
    if not todo:
        print("No todos yet.")
    else:
        print("\nYour Todos:")
        for index, item in enumerate(todo, start=1):
            print(f"{index}. {item}")
        
def add_todo():
    task = input("Enter the task: ")
    todo.append(task)
    print(f"Todo '{task}' added.")

def remove_todo():
    view_todos()
    if todo:
        try:
            index = int(input("Enter the number of the todo to delete: ")) - 1
            removed = todo.pop(index)
            print(f"Todo '{removed}' deleted.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_todo()
        elif choice == '2':
            view_todos()
        elif choice == '3':
            remove_todo()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# This is a simple command-line Todo application.