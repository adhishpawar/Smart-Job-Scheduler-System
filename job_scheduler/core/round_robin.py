from collections import deque
import time

def run_jobs_round_robin(jobs, quantum=2):
    print("\n--- Round Robin Schedulaer ---")
    queue = deque([job for job in jobs if job.status != "Completed"])

    while queue:
        job = queue.popleft()
        print(f"Running {job.name} for {quantum} seconds")
        job.status = "Running"
        time.sleep(1)

        job.duration -= quantum
        if job.duration > 0:
            job.status = "Pending"
            queue.append(job)
        else:
            job.status = "Completed"
            print(f"Job {job.name} completed.")