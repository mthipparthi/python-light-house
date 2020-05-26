def main(numbers):

    for i, num in enumerate(numbers):
        # if num % 3 == 0 and num % 5 == 0:
        if num % 15 == 0:
            numbers[i] = "FizzBuzz"
        elif num % 3 == 0:
            numbers[i] = "Fizz"
        elif num % 5 == 0:
            numbers[i] = "Buzz"
        else:
            pass

    return numbers


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
    main(numbers)
