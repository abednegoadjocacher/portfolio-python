#My task is building a task manager
#User must prompted to select an action to perform
#Base on the user input the right operation must be performed.
#Operations thatt user can perfom
# 1.  Add new task
# 2. View tasks
# 3. remove task
# 4. update task
# 5. Exit

def addTask():
    tasks.append(task_name)

def viewTask():
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("You have not added any task yet!!")

def removeTask():
    if tasks:
        tasks.pop()
    else:
        print("There is no task to remove!!")
    

tasks = []
print("""What do you want to do?
    1. Add new task
    2. View tasks
    3. remove task
    4. Exit    """)

while True:
    try:
        operation = int(input("Select from (1-4): "))
        
        if operation == 1:
            task_name = input("Enter you new task: ")
            addTask()
            #tasks.append(task_name)
        elif operation == 2:
            viewTask()
        elif operation == 3:
            removeTask()
        elif operation == 4:
            print("closing task")
            break
        else:
            print("Please read the instructions well")

    except ValueError:
        print("Invalid input")
