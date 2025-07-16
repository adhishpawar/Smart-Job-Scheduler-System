from enum import Enum

class JobType(Enum):
    DEV = "Development"
    TEST = "Testing"
    DATA = "Data Processing"
    SYSTEM = "System Maintenance"
    AI = "AI/ML Task"