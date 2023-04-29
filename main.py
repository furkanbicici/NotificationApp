import time
from plyer import notification

icon = "battery.jpg"

if __name__ == "__main__":

    notification.notify(
        title = "Notification System",
        message = "Your Notification System is Working",
        app_name = "1 New Notice",


        # displaying time
        timeout = 10
    )

