from storage.job_store import JobStore
from utils.logger import log_action

class Schedular:
    def __init__(self):
        self.store = JobStore()
    
    def add_job(self, job):
        self.store.add_job(job)
        log_action(f"Added job: {job.name} (Priority: {job.priority})")
    
    def run_all(self):
        while self.store.has_jobs():
            job = self.store.get_next_job()
            job.run()
            log_action(f"Executed job: {job.name}" )
    
    def run_one(self):
        job  = self.store.get_next_job()
        if job:
            job.run()
            log_action(f"Executed Job: {job.name}")
        else:
            print("No Jobs to run.  ")

    def list_jobs(self):
        print("\n --- current Jobs")
        for _,_, job in self.store.queue:
            print(f"{job.id[:8]} | {job.name}  | [{job.category.value}] | {job.priority} | {job.duration}s | {job.status}")
    