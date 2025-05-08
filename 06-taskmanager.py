#My task is building a task manager
#User must prompted to select an action to perform
#Base on the user input the right operation must be performed.
#Operations thatt user can perfom
# 1.  Add new task
# 2. View tasks
# 3. remove task
# 4. update task
# 5. Exit

tasks = []
print("""What do you want to do?
    1. Add new task
    2. View tasks
    3. remove task
    4. update task
    5. Exit    """)

while True:
    try:
        operation = int(input("Select from (1-5): "))
        
        if operation == 1:
            task_name = input("Enter you new task: ")
            tasks.append(task_name)
        elif operation == 2:
            for task in tasks:
                print(task)
        elif operation == 3:
            tasks.remove()
            print(task)
        elif operation == 5:
            print("closing task")
            break

    except:
        pass
