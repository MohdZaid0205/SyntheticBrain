
from datetime import datetime

def getCurrentTime() -> str:
    return f"{datetime.now().strftime("%H:%M:%S")}".center(12)

