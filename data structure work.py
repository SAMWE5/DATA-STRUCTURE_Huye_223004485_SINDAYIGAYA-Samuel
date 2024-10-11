from collections import deque


undo_stack = []

task_queue = deque()


completed_tasks = []


def add_task(task):
    task_queue.append(task)
    print(f"Task '{task}' added to the queue.")

def process_task():
    if task_queue:
        task = task_queue.popleft()  # Remove from front of queue (FIFO)
        completed_tasks.append(task)  # Add to completed list
        print(f"Task '{task}' completed.")
    else:
        print("No tasks in the queue to process.")

def undo_last_task():
    if completed_tasks:
        last_task = completed_tasks.pop()  
        undo_stack.append(last_task)  
        print(f"Task '{last_task}' undone.")
    else:
        print("No completed tasks to undo.")

def redo_task():
    if undo_stack:
        task = undo_stack.pop() 
        completed_tasks.append(task) 
        print(f"Task '{task}' redone.")
    else:
        print("No tasks to redo.")


add_task("Task A")
add_task("Task B")
add_task("Task C")

process_task() 
process_task()  
process_task() 

undo_last_task() 
undo_last_task() 

redo_task() 
print("\nTask Queue:", list(task_queue))
print("Completed Tasks:", completed_tasks)
print("Undo Stack:", undo_stack)
