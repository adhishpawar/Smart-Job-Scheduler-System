from storage.job_store import JobStore
from utils.logger import log_action

class Schedular:
    def __init__(self):
        self.store = JobStore()
        self.all_jobs = []
    
    def add_job(self, job):
        self.store.add_job(job)
        self.all_jobs.append(job)
        log_action(f"Added job: {job.name} (Priority: {job.priority})")
    
    def run_one(self):
        job  = self.store.get_next_job()
        if job:
            job.run()
            log_action(f"Executed Job: {job.name}")
        else:
            print("No Jobs to run.  ")

    def run_all(self):
        while self.store.has_jobs():
            job = self.store.get_next_job()
            job.run()
            log_action(f"Executed job: {job.name}" )

    def list_jobs(self):
        print("\n --- current Jobs")
        for _,_, job in self.store.queue:
            print(f"{job.id[:8]} | {job.name}  | [{job.category.value}] | {job.priority} | {job.duration}s | {job.status}")

    def delete_job(self, job_id):
        for job in self.all_jobs:
            if job.id.startswith(job_id):
                self.all_jobs.remove(job)
                log_action(f"Deleted job: {job.name}")
                print(f"Job '{job.name}' deleted.")
                return
        print("Job Not found")

    def update_priority(self, job_id, new_priority):
        for job in self.all_jobs:
            if job.id.startswith(job_id):
                old = job.priority
                job.priority = new_priority
                log_action(f"Updated priority of {job.name} from {old} to {new_priority}")
                print(f"updated priority of {job.name}")
                return
            print("Job not found")


    