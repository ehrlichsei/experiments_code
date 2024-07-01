import logging
from .my_task import ExampleTask

class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self.logger = logging.getLogger('TaskScheduler')
    
    def add_task(self, task):
        self.tasks.append(task)
        self.logger.info(f"Task {task.name} added to the scheduler.")
    
    def run_tasks(self):
        self.logger.info("Task scheduler started.")
        for task in self.tasks:
            task.run()
        self.logger.info("Task scheduler completed.")


