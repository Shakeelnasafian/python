TODO_FILE = "todos.txt"

def load_todos():
    try:
        with open(TODO_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        for todo in todos:
            file.write(todo + "\n")

def show_menu():
    print("\nTodo App Menu:")
    print("1. Add Todo")
    print("2. View Todos")
    print("3. Delete Todo")
    print("4. Exit")

def view_todos(todos):
    if not todos:
        print("No todos yet.")
    else:
        print("\nYour Todos:")
        for index, item in enumerate(todos, start=1):
            print(f"{index}. {item}")

def add_todo(todos):
    task = input("Enter the task: ")
    todos.append(task)
    save_todos(todos)
    print(f"Todo '{task}' added.")

def remove_todo(todos):
    view_todos(todos)
    if todos:
        try:
            index = int(input("Enter the number of the todo to delete: ")) - 1
            removed = todos.pop(index)
            save_todos(todos)
            print(f"Todo '{removed}' deleted.")
        except (ValueError, IndexError):
            print("Please enter a valid number.")

def main():
    todos = load_todos()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_todo(todos)
        elif choice == '2':
            view_todos(todos)
        elif choice == '3':
            remove_todo(todos)
        elif choice == '4':
            print("Exiting... Good Bye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()