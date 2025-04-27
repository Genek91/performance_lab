import sys


def read_numbers_data(file_name):
    numbers = []

    with open(file_name, "r") as file:
        for line in file:
            numbers.append(int(line))

    return numbers


def min_number_steps(numbers):
    numbers.sort()
    i1 = 0
    i2 = len(numbers) - 1
    im = len(numbers) // 2
    steps = 1

    while i1 != im and i2 != im:
        if numbers[i1] < numbers[im]:
            numbers[i1] += 1
            if numbers[i1] == numbers[im]:
                i1 += 1
        elif numbers[i2] > numbers[im]:
            numbers[i2] -= 1
            if numbers[i2] == numbers[im]:
                i2 -= 1
        steps += 1

    return steps


if __name__ == "__main__":
    numbers_file = sys.argv[1]

    numbers = read_numbers_data(numbers_file)
    result = min_number_steps(numbers)

    print(result)
