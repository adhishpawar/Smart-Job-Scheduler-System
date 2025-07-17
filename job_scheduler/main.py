from models.scheduler import Schedular
from models.job import Job
from core.executor import Executor
from utils.job_input import get_job_from_user
from core.round_robin import run_jobs_round_robin
from db.db_helper import insert_job

def menu():
    print("\n=== Smart Job Scheduler ===")
    print("1. Create New Job")
    print("2. Run One Job")
    print("3. Run All Jobs")
    print("4. List All Jobs")
    print("5. Delete a Job")
    print("6. Update Job Priority")
    print("7. Run Round-Robin Scheduler")
    print("8. Exit")

schedular  = Schedular()


while True:
    menu()
    choice  = input("Enter choice: ")

    if choice == "1":
        job = get_job_from_user()
        schedular.add_job(job) 

    elif choice == "2":
        schedular.run_one()
    
    elif choice == "3":
        schedular.run_all()

    elif choice == "4":
        schedular.list_jobs()
    
    elif choice == "5":
        job_id = input("Enter job id: ").strip()
        schedular.delete_job(job_id)
    
    elif choice == "6":
        job_id = input("Enter job id: ").strip()
        new_priority = int(input("Enter new priority: "))
        schedular.update_priority(job_id, new_priority) 
    
    elif choice == "7":
        quantum = int(input("Enter time qunatum in seconds: "))
        jobs = schedular.store.get_all_jobs()
        run_jobs_round_robin(jobs, quantum)


    elif choice == "8":
        print("byeee")
        break

    else:
        print("Invalid choice.")