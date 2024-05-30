class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print("Task not found in the to-do list.")

    def view_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Your to-do list is empty.")

    def start(self):
        print("Welcome to the To-Do List Manager!")
        while True:
            print("\nPlease choose an option:")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. View Tasks")
            print("4. Exit")
            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                task = input("Enter task to add: ")
                self.add_task(task)
            elif choice == '2':
                task = input("Enter task to remove: ")
                self.remove_task(task)
            elif choice == '3':
                self.view_tasks()
            elif choice == '4':
                print("Thank you for using the To-Do List Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.start()
