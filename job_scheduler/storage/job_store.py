import mysql.connector
from config.db import get_connection
from datetime import datetime
from db.db_helper import (
    insert_job,
    fetch_next_job,
    fetch_all_jobs,
    update_job_status,
    update_job_priority,
    delete_job,
    has_pending_jobs
)

class JobStore:
    def add_job(self, job):
        insert_job(job)

    def get_next_job(self):
        return fetch_next_job()

    def has_jobs(self):
        return has_pending_jobs()

    def update_job_status(self, job_id, status):
        update_job_status(job_id, status)

    def delete_job(self, job_id):
        delete_job(job_id)

    def update_priority(self, job_id, new_priority):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT name, priority FROM jobs WHERE id = %s", (job_id,))
        row = cursor.fetchone()

        if row is None:
            print("Job not found.")
            return False, None, None  # Return a tuple even in failure

        job_name, old_priority = row

        cursor.execute("UPDATE jobs SET priority = %s WHERE id = %s", (new_priority, job_id))
        connection.commit()

        cursor.close()
        connection.close()

        return True, job_name, old_priority  # This must be a 3-item tuple

    def get_all_jobs(self):
        return fetch_all_jobs()