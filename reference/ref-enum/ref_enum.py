import enum


class BusinessFlowsEnum(enum.Enum):
    FEEDS = "feeds"
    FOLDERS = "personal_folders"
    ALERTS = "peak_alerts"


def main():
    for v in BusinessFlowsEnum:
        print(f"{v}")

    if "feeds" in BusinessFlowsEnum:
        print(f"Found it")


if __name__ == "__main__:"
    main()
