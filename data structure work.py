class DailyTaskPlanner:
    def __init__(self):
        self.task_queue = deque()          
        self.completed_tasks = []          
        self.undo_stack = []               
     def add_task(self, task):
        self.task_queue.append(task)
        print(f"Task '{task}' added to the queue.")
     def process_task(self):
        if not self.task_queue:
            print("No tasks to process.")
            return
         current_task = self.task_queue.popleft()  
        print(f"Processing task: {current_task}")
        
        self.completed_tasks.append(current_task) 
        self.undo_stack.append(current_task)       
     def undo_last_task(self):
        if not self.undo_stack:
            print("No tasks to undo.")
            return
         last_task = self.undo_stack.pop()  
        print(f"Undoing task: {last_task}")
         self.completed_tasks.remove(last_task)    
        self.task_queue.appendleft(last_task)      
    def show_completed_tasks(self):
        if not self.completed_tasks:
            print("No tasks have been completed yet.")
            return
        print("Completed tasks:", self.completed_tasks)
    def show_pending_tasks(self):
        if not self.task_queue:
            print("No pending tasks in the queue.")
            return
        print("Pending tasks in the queue:", list(self.task_queue))
planner = DailyTaskPlanner()
planner.add_task("Task A")
planner.add_task("Task B")
planner.add_task("Task C")
planner.process_task()  
planner.process_task()  
planner.show_completed_tasks()  
planner.show_pending_tasks()   
planner.undo_last_task()       
planner.show_completed_tasks() 
planner.show_pending_tasks()   
planner.process_task()         
