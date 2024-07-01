import logging

class Task:
    def __init__(self, name):
        self.name = name
        self.status = 'pending'
        self.logger = logging.getLogger(self.name)
    
    def run(self):
        self.logger.info(f"Task {self.name} started.")
        try:
            # 具体任务的执行逻辑
            self.execute()
            self.status = 'completed'
            self.logger.info(f"Task {self.name} completed successfully.")
        except Exception as e:
            self.status = 'failed'
            self.logger.error(f"Task {self.name} failed with error: {e}")
    
    def execute(self):
        raise NotImplementedError("Subclasses must implement this method.")

class ExampleTask(Task):
    def __init__(self, name, param):
        super().__init__(name)
        self.param = param
    
    def execute(self):
        # 示例任务的具体逻辑
        print(f"Executing task with parameter: {self.param}")
