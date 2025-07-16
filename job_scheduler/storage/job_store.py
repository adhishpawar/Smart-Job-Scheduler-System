import heapq

class JobStore:
    def __init__(self):
        self.queue = []
    
    def add_job(self, job):
        heapq.heappush(self.queue, (job.priority, job.created_at, job))

    def get_next_job(self):
        return heapq.heappop(self.queue)[2] if self.queue else None

    def has_jobs(self):
        return len(self.queue) > 0