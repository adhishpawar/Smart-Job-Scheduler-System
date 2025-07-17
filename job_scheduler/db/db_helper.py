import mysql.connector
from mysql.connector import Error
from models.job import Job
from models.jobtype import JobType
from config.db import get_connection



def insert_job(job: Job):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO jobs (name, category, duration, priority, status, created_at)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        job.name, job.category.name, job.duration,
        job.priority, job.status, job.created_at
    )

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def fetch_all_jobs():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()

    jobs = []
    for row in rows:
        job = Job(
            id=row["id"],
            name=row["name"],
            category=JobType[row["category"]], 
            duration=row["duration"],
            priority=row["priority"],
            status=row["status"],
            created_at=row["created_at"],
            execute_fn=lambda: print(f"Simulating: {row['name']}")
        )
        jobs.append(job)
    cursor.close()
    conn.close()
    return jobs


def fetch_next_job():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT * FROM jobs
        WHERE status = 'Pending'
        ORDER BY priority ASC, created_at ASC
        LIMIT 1
    """)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        return Job(
            id=row["id"],
            name=row["name"],
            category= JobType[row["category"]],
            duration=row["duration"],
            priority=row["priority"],
            status=row["status"],
            created_at=row["created_at"],
            execute_fn=lambda: print(f"Simulating: {row['name']}")
        )
    return None


def update_job_status(job_id, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE jobs SET status = %s WHERE id = %s", (status, job_id))
    conn.commit()
    cursor.close()
    conn.close()


def update_job_priority(job_id, priority):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE jobs SET priority = %s WHERE id = %s", (priority, job_id))
    conn.commit()
    cursor.close()
    conn.close()


def delete_job(job_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jobs WHERE id = %s", (job_id,))
    conn.commit()
    cursor.close()
    conn.close()


def has_pending_jobs():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) AS count FROM jobs WHERE status = 'Pending'")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result["count"] > 0
