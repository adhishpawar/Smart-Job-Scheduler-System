from db import get_connection
from models.job import Job
from datetime import datetime

def add_job(job: Job):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO jobs (id, name, category, priority, duration, status, created_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (job.id, job.name, job.category, job.priority, job.duration, job.status, job.created_at))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_jobs():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    cursor.close()
    conn.close()
    return jobs

def delete_job(job_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jobs WHERE id = %s", (job_id,))
    conn.commit()
    cursor.close()
    conn.close()

def update_priority(job_id, new_priority):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE jobs SET priority = %s WHERE id = %s", (new_priority, job_id))
    conn.commit()
    cursor.close()
    conn.close()

def update_status(job_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE jobs SET status = %s WHERE id = %s", (new_status, job_id))
    conn.commit()
    cursor.close()
    conn.close()
