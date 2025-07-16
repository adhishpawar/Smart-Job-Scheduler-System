import uuid
import datetime

class Job:
    def __init__(self, name, execute_fn, priority=1):
        self.id = str(uuid.uuid4())
        self.name = name
        self.execute_fn = execute_fn
        self.priority = priority
        self.created_at = datetime.datetime.now()
    
    def run(self):
        print(f"Running Job: {self.name} [{self.id}]")
        self.execute_fn()
