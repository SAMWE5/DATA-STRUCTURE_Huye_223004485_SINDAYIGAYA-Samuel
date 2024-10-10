from collections import deque

# Stack for undoing tasks (LIFO)
undo_stack = []

# Queue for processing task assignments (FIFO)
task_queue = deque()

# List for tracking completed tasks
completed_tasks = []

# Function to add a task to the queue
def add_task(task):
    task_queue.append(task)
    print(f"Task '{task}' added to the queue.")

# Function to process tasks from the queue
def process_task():
    if task_queue:
        task = task_queue.popleft()  # Remove from front of queue (FIFO)
        completed_tasks.append(task)  # Add to completed list
        print(f"Task '{task}' completed.")
    else:
        print("No tasks in the queue to process.")

# Function to undo the last completed task
def undo_last_task():
    if completed_tasks:
        last_task = completed_tasks.pop()  # Remove from completed list
        undo_stack.append(last_task)  # Add to undo stack
        print(f"Task '{last_task}' undone.")
    else:
        print("No completed tasks to undo.")

# Function to redo the last undone task
def redo_task():
    if undo_stack:
        task = undo_stack.pop()  # Remove from undo stack (LIFO)
        completed_tasks.append(task)  # Add back to completed list
        print(f"Task '{task}' redone.")
    else:
        print("No tasks to redo.")

# Example of usage
add_task("Task A")
add_task("Task B")
add_task("Task C")

process_task()  # Completes Task A
process_task()  # Completes Task B
process_task()  # Completes Task C

undo_last_task()  # Undo Task C
undo_last_task()  # Undo Task B

redo_task()  # Redo Task B

print("\nTask Queue:", list(task_queue))
print("Completed Tasks:", completed_tasks)
print("Undo Stack:", undo_stack)
