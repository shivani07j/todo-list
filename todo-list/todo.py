tasks = []

def show_menu():
    print("\n🌸 --- My To-Do List --- 🌸")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Quit")

def view_tasks():
    if len(tasks) == 0:
        print("\n✨ No tasks yet! Add something.")
    else:
        print("\n📝 Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")

def add_task():
    task = input("\nWhat do you want to add? → ")
    tasks.append(task)
    print(f"✅ '{task}' added!")

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        num = int(input("\nEnter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"🗑️ '{removed}' deleted!")
    except (ValueError, IndexError):
        print("❌ Invalid number, try again.")

# Main loop
while True:
    show_menu()
    choice = input("\nChoose an option (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("\n🌷 Bye! Stay productive ✨")
        break
    else:
        print("❌ Please enter 1, 2, 3 or 4")