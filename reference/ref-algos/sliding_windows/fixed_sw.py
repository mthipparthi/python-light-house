def main(arr, window=4):
    max_sum = sum(arr[0:window])
    for i in range(1, len(arr) - window + 1):
        window_end = i + window
        total = sum(arr[i:window_end])
        if total > max_sum:
            max_sum = total

    return max_sum


if __name__ == "__main__":
    arr = [
        1,
        2,
        3,
        -5,
        5,
        -2,
        5,
        -6,
    ]
    print(main(arr))
