from plyer import notification
import time


def main():
    while True:
        # notification.notify(
        #     title="Break time",
        #     message="Break time",
        #     app_icon="./clock.jpg",
        #     timeout=10,
        # )

        notification.notify(title="test tiltle", message="scanning started")

        time.sleep(60 * 60)


if __name__ == "__main__":
    main()

