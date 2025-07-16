from models.scheduler import Schedular
from models.job import Job
from core.executor import Executor

def menu():
    print("\n=== Smart Job Scheduler ===")
    print("1. Add Email Job")
    print("2. Add Backup Job")
    print("3. Run One Job")
    print("4. Run All Jobs")
    print("5. Exit")

schedular  = Schedular()


while True:
    menu()
    choice  = input("Enter choice")
    if choice == "1":
        job = Job("Email job", lambda: Executor.simulate_email,priority=2)
        schedular.add_job(job)  

    elif choice == "2":
        job = Job("Backup Job",lambda: Executor.simulate_backup, priority=1)
        schedular.add_job(job)
    
    elif choice == "3":
        schedular.run_one()
    
    elif choice == "4":
        schedular.run_all()
    
    elif choice == "5":
        print("byeee")
        break

    else:
        print("Invalid choice.")