from tabulate import tabulate

class TodoItem:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

    def __str__(self):
        return f"{self.id}: {self.title} - {self.description}"

todo_list = []
next_id = 1
tasks_created = 0
tasks_completed = 0

def add_todo_item(title, description):
    global next_id, tasks_created
    todo = TodoItem(next_id, title, description)
    todo_list.append(todo)
    next_id += 1
    tasks_created += 1
    print(f"Added: {todo}")

def view_todo_items():
    if not todo_list:
        print("No to-do items.")
        return

    table = []
    for todo in todo_list:
        table.append([todo.id, todo.title, todo.description])

    headers = ["ID", "Title", "Description"]
    print(tabulate(table, headers, tablefmt="pretty"))

def update_todo_item(id, title, description):
    for todo in todo_list:
        if todo.id == id:
            todo.title = title
            todo.description = description
            print(f"Updated: {todo}")
            return
    print("To-Do item not found.")

def delete_todo_item(id):
    global todo_list, tasks_completed
    if any(todo.id == id for todo in todo_list):
        todo_list = [todo for todo in todo_list if todo.id != id]
        tasks_completed += 1
        print(f"Deleted to-do item with id {id}")
    else:
        print("To-Do item not found.")

def productivity_measure():
    if tasks_created == 0:
        productivity_score = 0
    else:
        productivity_score = (tasks_completed / tasks_created) * 100
    print(f"Tasks Created: {tasks_created}")
    print(f"Tasks Completed: {tasks_completed}")
    print(f"Productivity Score: {productivity_score:.2f}%")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a new to-do item(got another task yet?)")
        print("2. View all to-do items(no time to procrastinate)")
        print("3. Update a to-do item(fine lets update)")
        print("4. Delete a to-do item(wohooo task done)")
        print("5. View productivity measure")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter title: ")
            description = input("Enter description: ")
            add_todo_item(title, description)
        elif choice == '2':
            view_todo_items()
        elif choice == '3':
            id = int(input("Enter the ID of the item to update: "))
            title = input("Enter new title: ")
            description = input("Enter new description: ")
            update_todo_item(id, title, description)
        elif choice == '4':
            id = int(input("Enter the ID of the item to delete: "))
            delete_todo_item(id)
        elif choice == '5':
            productivity_measure()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
