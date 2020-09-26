from typing import List


def missing_number(n: int, numbers: List(int)) -> int:
    total = sum(numbers)
    return int(n * (n + 1) / 2) - total


def main():
    n = int(input())
    numbers = list(map(int, str(input()).split()))
    print(missing_number(n, numbers))


if __name__ == "__main__":
    main()
