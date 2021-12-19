import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "**Please fold your clothes",
            message = "Time to fold clothes",
            timeout = 15
        )
        time.sleep(60*60)