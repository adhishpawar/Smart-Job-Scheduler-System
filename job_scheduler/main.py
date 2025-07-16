from models.scheduler import Schedular
from models.job import Job
from core.executor import Executor
from utils.job_input import get_job_from_user

def menu():
    print("\n=== Smart Job Scheduler ===")
    print("1. Create New Job")
    print("2. Run One Job")
    print("3. Run All Jobs")
    print("4. List All Jobs")
    print("5. Exit")

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
        print("byeee")
        break


    else:
        print("Invalid choice.")