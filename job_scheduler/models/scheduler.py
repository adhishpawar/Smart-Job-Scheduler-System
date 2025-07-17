from storage.job_store import JobStore
from utils.logger import log_action

class Schedular:
    def __init__(self):
        self.store = JobStore()
    
    def add_job(self, job):
        self.store.add_job(job)
        log_action(f"Added job: {job.name} (Priority: {job.priority})")
    
    def run_one(self):
        job  = self.store.get_next_job()
        if job:
            job.run()
            self.store.update_job_status(job.id, "completed")
            log_action(f"Executed Job: {job.name}")
        else:
            print("No Jobs to run.  ")

    def run_all(self):
        while True:
            job = self.store.get_next_job()
            if not job:
                break
            job.run()
            self.store.update_job_status(job.id, "completed")
            log_action(f"Executed job: {job.name}" )

    def list_jobs(self):
        print("\n --- current Jobs ---")
        jobs = self.store.get_all_jobs()
        for job in jobs:
            print(f"{str(job.id)[:8]} | {job.name} | [{job.category.value}] | {job.priority} | {job.duration}s | {job.status}")



    def delete_job(self, job_id):
        self.store.delete_job(job_id)
        print(f"Job {job_id} deleted (if it existed).")

    def update_priority(self, job_id, new_priority):
        success, job_name, old_priority = self.store.update_priority(job_id, new_priority)
        if success:
            log_action(f"Updated priority of {job_name} from {old_priority} to {new_priority}")
            print(f"Updated priority of {job_name}")
        else:
            print("Job not found.")


    