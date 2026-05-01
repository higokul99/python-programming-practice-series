def read_int(prompt):
    """Read an integer from input until the user enters a valid value."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def sum_list(numbers):
    return sum(numbers)


def main():
    numbers = []
    count = read_int("Enter the number of elements needed: ")
    while count < 0:
        print("Please enter a non-negative number of elements.")
        count = read_int("Enter the number of elements needed: ")

    for i in range(count):
        numbers.append(read_int(f"Enter element No {i + 1}: "))

    print(sum_list(numbers))


if __name__ == '__main__':
    main()
