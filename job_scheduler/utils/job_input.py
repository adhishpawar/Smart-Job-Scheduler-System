from models.job import Job
from models.jobtype import JobType

def get_job_from_user():
    print("\n --Create new Job--")
    name = input("Enter Job Name: ").strip()

    category = select_category()

    duration = int(input("Estimated duration in Seconds: "))

    priority = int(input("Priority (lower = higher priority): "))

    return Job(
        name=name,
        category=category,
        duration=duration,
        priority=priority,
        execute_fn=lambda: print(f"Simulating: {name}")
    )


def select_category():
    print("Select job category:")
    for i, cat in enumerate(JobType, start=1):
        print(f"{i}. {cat.name} - {cat.value}")
    choice = int(input("Enter choice (1-5): "))
    return list(JobType)[choice - 1]