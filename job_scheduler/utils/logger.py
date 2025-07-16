from datetime import datetime

def log_action(message):
    with open("data/logs.txt", "a") as log_file:
        log_file.write(f"[datetime.now()] {message} \n")
        