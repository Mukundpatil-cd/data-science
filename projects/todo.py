tasks = []

def menu():
    print("\nOptions:")
    print("1. Add task")
    print("2. View task")
    print("3. Remove task")
    print("4. Exit")


def add_task():
    new_task = input("Add a task: ")
    tasks.append(new_task)
    print(f"✅ Task '{new_task}' added!")

def view_task():
    if not tasks:
        print("📭 No tasks in the list.")
    else:
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

def remove_task():
    view_task()
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"🗑 Task '{removed}' removed!")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

while True:
    menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("👋 Thank you for using the To-Do List!")
        break
    else:
        print("❌ Invalid choice, please try again.")
