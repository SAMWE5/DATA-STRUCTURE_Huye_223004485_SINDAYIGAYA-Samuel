from collections import deque

class TaskPlanner:
    def __init__(self):
        self.task_stack = []      
        self.task_queue = deque() 
        self.completed_tasks = []  

    
    def add_task(self, task):
        self.task_queue.append(task)
        print(f"Task '{task}' added to the queue.")

    
    def process_task(self):
        if self.task_queue:
            task = self.task_queue.popleft()
            self.task_stack.append(task)
            print(f"Processing task '{task}'...")
        else:
            print("No tasks to process.")

    
    def complete_task(self):
        if self.task_stack:
            task = self.task_stack.pop()
            self.completed_tasks.append(task)
            print(f"Task '{task}' completed.")
        else:
            print("No tasks to complete.")

    
    def undo_last_completed_task(self):
        if self.completed_tasks:
            task = self.completed_tasks.pop()
            self.task_queue.appendleft(task)
            print(f"Task '{task}' undone and added back to the queue.")
        else:
            print("No completed tasks to undo.")

    def show_status(self):
        print("\nTask Queue:", list(self.task_queue))
        print("Task Stack (Undo):", self.task_stack)
        print("Completed Tasks:", self.completed_tasks, "\n")



planner = TaskPlanner()

planner.add_task("Task 1")
planner.add_task("Task 2")
planner.add_task("Task 3")


planner.process_task()
planner.process_task()


planner.complete_task()


planner.show_status()

planner.undo_last_completed_task()


planner.show_status()
