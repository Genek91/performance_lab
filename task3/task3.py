import json
import sys


def read_json_data(file_file):
    with open(file_file, "r", encoding="utf-8") as file:
        return json.load(file)


def fill_values(tests_data, values_dict):
    tests = list(tests_data)

    while tests:
        current_test = tests.pop()

        if "id" in current_test:
            value = values_dict.get(current_test["id"], None)
            if value is not None:
                current_test["value"] = value

        if "values" in current_test:
            tests.extend(current_test["values"])


def main(values_file, tests_file, report_file):
    values_data = read_json_data(values_file)
    tests_data = read_json_data(tests_file)

    values_dict = {item["id"]: item["value"] for item in values_data["values"]}

    fill_values(tests_data["tests"], values_dict)

    with open(report_file, "w", encoding="utf-8") as report_file:
        json.dump(tests_data, report_file, indent=4)


if __name__ == "__main__":
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    main(values_file, tests_file, report_file)
