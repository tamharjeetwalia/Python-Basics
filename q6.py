import csv


def read_csv(file_path):

    data = []

    with open(file_path, "r") as file:

        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    return data


def get_column_widths(data):

    col_widths = []

    num_cols = len(data[0])

    for col in range(num_cols):

        max_width = 0

        for row in data:

            max_width = max(max_width, len(row[col]))

        col_widths.append(max_width)

    return col_widths


def print_border(widths):

    print("+", end="")

    for w in widths:

        print("-" * (w + 2) + "+", end="")

    print()


def print_row(row, widths):

    print("|", end="")

    for i, cell in enumerate(row):

        print(" " + cell.ljust(widths[i]) + " |", end="")

    print()


def display_table(data):

    widths = get_column_widths(data)

    print_border(widths)

    for row in data:

        print_row(row, widths)

        print_border(widths)


def main():

    file_path = input("Enter CSV file path: ")

    data = read_csv(file_path)

    display_table(data)


if __name__ == "__main__":

    main()