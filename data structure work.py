from collections import deque

class DailyTaskPlanner:
    def __init__(self):
        self.task_queue = deque()          # Queue for task assignments
        self.completed_tasks = []          # List for tracking completed tasks
        self.undo_stack = []               # Stack for undoing tasks
    
    # Add task to the queue
    def add_task(self, task):
        self.task_queue.append(task)
        print(f"Task '{task}' added to the queue.")
    
    # Process the next task in the queue
    def process_task(self):
        if not self.task_queue:
            print("No tasks to process.")
            return
        
        current_task = self.task_queue.popleft()  # Get the first task (FIFO)
        print(f"Processing task: {current_task}")
        
        self.completed_tasks.append(current_task)  # Add to completed tasks list
        self.undo_stack.append(current_task)       # Push to undo stack
    
    # Undo the last completed task
    def undo_last_task(self):
        if not self.undo_stack:
            print("No tasks to undo.")
            return
        
        last_task = self.undo_stack.pop()  # Pop from undo stack (LIFO)
        print(f"Undoing task: {last_task}")
        
        self.completed_tasks.remove(last_task)     # Remove from completed list
        self.task_queue.appendleft(last_task)      # Re-add to the front of the queue
    
    # Show the completed tasks
    def show_completed_tasks(self):
        if not self.completed_tasks:
            print("No tasks have been completed yet.")
            return
        print("Completed tasks:", self.completed_tasks)
    
    # Show the tasks waiting in the queue
    def show_pending_tasks(self):
        if not self.task_queue:
            print("No pending tasks in the queue.")
            return
        print("Pending tasks in the queue:", list(self.task_queue))


# Example usage:
planner = DailyTaskPlanner()

# Add tasks to the queue
planner.add_task("Task A")
planner.add_task("Task B")
planner.add_task("Task C")

# Process some tasks
planner.process_task()  # Processes Task A
planner.process_task()  # Processes Task B

# Show the state of completed tasks and pending tasks
planner.show_completed_tasks()  # Shows completed tasks
planner.show_pending_tasks()    # Shows tasks left in the queue

# Undo the last completed task
planner.undo_last_task()        # Undoes Task B

# Show the updated state after undo
planner.show_completed_tasks()  # Shows completed tasks after undo
planner.show_pending_tasks()    # Shows tasks in queue after undo

# Process another task
planner.process_task()          # Processes Task C
