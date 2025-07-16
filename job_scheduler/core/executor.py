import time 


class Executor:
    @staticmethod
    def simulate_backup():
        print("performing Backup...")
        time.sleep(1)
        print("BackUp complete")
    
    @staticmethod
    def simulate_email():
        print("Sending email...")
        time.sleep(1)
        print("Email sent..")