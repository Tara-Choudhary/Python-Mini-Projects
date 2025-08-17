print("📝 Welcome to the To-Do List App!")

# empty list to store tasks
tasks = []

while True:
    print("\n--- Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"✅ Task '{task}' added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("📭 No tasks available.")
        else:
            print("\n📋 Your Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("⚠️ No tasks to delete.")
        else:
            print("\n📋 Your Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num-1)
                print(f"🗑️ Task '{removed}' deleted!")
            else:
                print("❌ Invalid task number.")

    elif choice == "4":
        print("👋 Exiting the app. Goodbye!")
        break

    else:
        print("❌ Invalid choice, please enter a number between 1-4.")
