from models.job import Job
from models.job_type import JobType

def get_job_from_user():
    print("\n --Create new Job--")
    name = input("Enter Job Name: ").strip()

    print("Select job catgory: ")
    for index, category in enumerate(JobType):
        print(f"{index + 1}.{category.value}")
    
    cat_index = int(input("Enter Choice [1-5]: "))
    category = list(JobType)[cat_index - 1]

    duration = int(input("Estimated duration in Seconds: "))

    priority = int(input("Priority (lower = higher propority): "))

    logic = lambda: print(f"Executing Job: {name} Time required is {duration}")

    return Job(name, logic,category, duration,priority)


