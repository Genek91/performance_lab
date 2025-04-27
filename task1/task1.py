import sys


def find_path(n, m):
    numbers = list(range(1, n + 1))
    result = []
    pos = 0

    while True:
        result.append(numbers[pos])

        last_pos = (pos + m - 1) % n

        if last_pos == 0:
            break

        pos = last_pos

    return "".join(map(str, result))


if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    result = find_path(n, m)

    print(result)

#  cd task1
#  python task1.py 5 4
