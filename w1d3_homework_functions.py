


tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# MVP
# As a user, to manage my task list I would like a program that allows me to:
# Print a list of uncompleted tasks
def find_uncompeted_task(task_list):
 completed_task= []

 for task in task_list:
  if task["completed"]!=True==True:
     completed_task.append(task["description"])
 return(completed_task)

print(find_uncompeted_task(tasks))


# Print a list of completed tasks
def find_completed_task(task_list):
 completed_task= []

 for task in task_list:
  if task["completed"]==True==True:
     completed_task.append(task["description"])
 return(completed_task)

print(find_completed_task(tasks))

# Print a list of all task descriptions

def find_description(task_list):
    descriptions=[]
    for task in task_list:
        descriptions.append(task["description"])
    return(descriptions)

print(find_description(tasks))

# Print a list of tasks where time_taken is at least a given time

def find_long_tasks(task_list):
    time_taken_at_least_10=[]
    for task in task_list:
        if task ["time_taken"] > 10:
            time_taken_at_least_10.append(task["description"])
    return f" The tasks taking longer than ten minutes are: {time_taken_at_least_10}"

print(find_long_tasks(tasks))

# Print any task with a given description 
def find_by_given_description(task_list, named_task):
    
    for task in task_list:
        if task["description"] == named_task:
            return task
    return "Not found"

print(find_by_given_description(tasks, "Clean Windows"))
print(find_by_given_description(tasks, "Dance"))
# sample code from class:
# def find_( list, chicken_name ):
#   for chicken in list:
#     if chicken["name"] == chicken_name:
#       return chicken

#   return "Not found"

# Extension
# Given a description update that task to mark it as complete.

def update_task(task_list, description):
    for task in task_list:
        if task["description"]==description:
            return task_list["completed"],True

print(update_task(tasks,"Wash Dishes"))

    



    


# Add a task to the list
tasks.append({ "description": "Hoover Room", "completed": False, "time_taken": 20 })
# print(tasks)