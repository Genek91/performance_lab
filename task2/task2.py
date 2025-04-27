import sys
from decimal import Decimal


def read_circle_data(file_name):
    with open(file_name, "r") as file:
        x, y = map(Decimal, file.readline().strip().split())
        radius = Decimal(file.readline().strip())

    return x, y, radius


def read_points_data(file_name):
    points = []

    with open(file_name, "r") as file:
        for line in file:
            x, y = map(Decimal, line.strip().split())
            points.append((x, y))

    return points


def point_position(circle_x, circle_y, circle_radius, point):
    point_x, point_y = point
    distance_squared = (point_x - circle_x) ** 2 + (point_y - circle_y) ** 2
    circle_radius_squared = circle_radius ** 2

    if distance_squared == circle_radius_squared:
        return 0
    elif distance_squared < circle_radius_squared:
        return 1
    else:
        return 2


if __name__ == "__main__":
    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    circle_x, circle_y, circle_radius = read_circle_data(circle_file)
    points_list = read_points_data(points_file)

    results = [
        point_position(circle_x, circle_y, circle_radius, point)
        for point in points_list
    ]

    for result in results:
        print(result)

#  cd task2
#  python task2.py circle.txt points.txt
