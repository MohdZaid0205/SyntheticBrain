
from datetime import datetime

def getCurrentTime() -> str:
    return f"{datetime.now().strftime("%H:%M:%S")}".center(12)

def getCurrentDate() -> str:
    return f"{datetime.now().strftime("%d:%b:%y")}".center(13)
