import uuid
import datetime
from models.job_type import JobType

class Job:
    def __init__(self, name, execute_fn, category: JobType, duration: int,   priority: int=1):
        self.id = str(uuid.uuid4())
        self.name = name
        self.execute_fn = execute_fn
        self.priority = priority
        self.category = category
        self.duration = duration  # Duration in seconds
        self.status = "Pending"
        self.created_at = datetime.datetime.now()
    
    def run(self):
        print(f"Running Job: {self.name} [{self.id}]")
        self.execute_fn()
        self.status = "completed"
