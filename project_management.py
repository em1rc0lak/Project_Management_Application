import init


### HELPER FUNCTIONS ###
#returns the users choice 
def choose_operation():
    return int(input("""
Operations:
    1. Add a new task
    2. Assign task to a team member
    3. Complete a task
    4. Generate report
    5. Exit
Please select an operation: """))

#Corrects the id's of the tasks
def handle_id(tasks,task_id):
    for task in tasks:
        task['id'] = task_id
        task_id+=1    
        if "subtasks" in task:
            task_id = handle_id(task["subtasks"],task_id)
    return task_id   

#Prints the tasks to choose id from -> eg. id. description (assigned_to)
def prompt_task_choices(tasks,indent = 0):
    for task in tasks:
        print("-"*indent,end='')
        print(f"{task['id']}. {task['description']} ({task['assigned_to']})")
    
        if "subtasks" in task:
            prompt_task_choices(task["subtasks"],indent+2)

### HOMEWORK RELATED FUNCTIONS ###
total_time = 0
remaining_time = 0
def calculate_time_recusive(tasks,remaining_time):
    sum = 0
    for task in tasks:
        if task.get('completed') == None:
            task['completed'] = False
        if "subtasks" in task:
            task["time_estimate"],remaining_time = calculate_time_recusive(task["subtasks"],remaining_time)
            sum += task["time_estimate"]
        else:
            remaining_time += task["time_estimate"] if task['completed'] == False else 0
            sum += task["time_estimate"]
    return sum,remaining_time

def generate_report_recursive(tasks,indent = 0):
    
    for task in tasks:
        completed = "Completed" if task['completed'] else "Pending"
        time = calculate_time_recusive([task],0)[1]
        print("-"*indent,end='')
        print(f"{task['id']}. {task['description']} ({task['assigned_to']}) -- Estimated Time to Finish: {time} out of {task['time_estimate']} hours, {completed}\n")
    
        if "subtasks" in task:
            generate_report_recursive(task["subtasks"],indent+2)

def assign_task(tasks,id,assigned_to):
    for task in tasks:
        if task['id'] == id:
            task['assigned_to'] = assigned_to
            print(f"Task, {task['description']} assigned to {assigned_to}.")
        if "subtasks" in task:
            assign_task(task["subtasks"],id,assigned_to)

def add_task_recursive(tasks,id,description, assigned_to, time_estimate):
    new_task = {'id': 0, 'description': description, 'assigned_to': assigned_to, 'time_estimate': time_estimate}
    if id == 0:
        tasks.append(new_task)
        tasks[-1]["completed"] = False
    else:
        for task in tasks:
            if task['id'] == id:
                if "subtasks" in task:
                    task['subtasks'].append(new_task)
                    task["completed"] = False
                else:
                    task['subtasks'] = [new_task]
                    task["completed"] = False
            elif "subtasks" in task:
                add_task_recursive(task["subtasks"],id,description, assigned_to, time_estimate)
    
def complete_task_recursive(tasks,id):
    for task in tasks:
        if id == 0:
            task['completed'] = True
            if "subtasks" in task:
                complete_task_recursive(task["subtasks"],0)
        elif task['id'] == id:
            task['completed'] = True
            print(f"Task, {task['description']} marked as completed.")
            if "subtasks" in task:
                complete_task_recursive(task["subtasks"],0)
        elif "subtasks" in task:
            complete_task_recursive(task["subtasks"],id)

def main():
    tasks = init.init_tasks()
    
    is_contionue = True
    while is_contionue:
        choice = choose_operation()
        print()
        handle_id(tasks,1)

        if choice == 1:
            # Add Task
            prompt_task_choices(tasks)
            print()

            add_id = int(input("To add a new task, enter 0. To add a subtask, select the task ID: "))
            description = input("Please enter the task description: ")
            assigned_to = input("Please enter the task responsible: ")
            time_estimate = int(input("Please enter the estimated time for the task: "))

            add_task_recursive(tasks,add_id,description, assigned_to, time_estimate)
            print("New task is added .")
            input("Press Enter to continue...")
        elif choice == 2:
            # Assign Task
            prompt_task_choices(tasks)
            print()

            assign_id = int(input("Please select a task: "))
            assigned_to_new = input("Please enter the new team members name: ")
            assign_task(tasks,assign_id,assigned_to_new)
            input("Press Enter to continue...")
        elif choice == 3:
            # Complete Task
            prompt_task_choices(tasks)

            complete_id = int(input("Please select a task: "))
            complete_task_recursive(tasks,complete_id)
            input("Press Enter to continue...")
        elif choice == 4:
            # Generate Report
            total_time,remaining_time =calculate_time_recusive(tasks,0)
            generate_report_recursive(tasks)
            print(f"Total time to finish the project: {total_time} hours")
            print(f"Remaining time to finish the project: {remaining_time} hours")
            input("Press Enter to continue...")
        elif choice == 5:
            # Exit
            is_contionue = False

if __name__ == "__main__":
    main()