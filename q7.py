def get_recommendation(instance, cpu):

    sizes = [
        "nano","micro","small","medium","large",
        "xlarge","2xlarge","4xlarge","8xlarge",
        "16xlarge","32xlarge"
    ]

    instance_type, size = instance.split(".")

    index = sizes.index(size)

    if cpu < 20:

        status = "Underutilized"

        if index > 0:
            recommended = instance_type + "." + sizes[index - 1]
        else:
            recommended = instance

    elif cpu > 80:

        status = "Overutilized"

        if index < len(sizes) - 1:
            recommended = instance_type + "." + sizes[index + 1]
        else:
            recommended = instance

    else:

        status = "Optimized"

        latest_map = {
            "t2":"t3",
            "t3":"t4g",
            "m4":"m5",
            "m5":"m6i"
        }

        new_type = latest_map.get(instance_type, instance_type)

        recommended = new_type + "." + size

    return status, recommended


# TABLE FUNCTION FROM Q6
def print_table(headers, rows):

    widths = [len(h) for h in headers]

    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    def border():
        print("+", end="")
        for w in widths:
            print("-"*(w+2) + "+", end="")
        print()

    def print_row(row):
        print("|", end="")
        for i, cell in enumerate(row):
            print(" " + str(cell).ljust(widths[i]) + " |", end="")
        print()

    border()
    print_row(headers)
    border()

    for row in rows:
        print_row(row)
        border()


def main():

    instance = input("Current EC2 instance: ")

    cpu = int(input("CPU utilization (%): ").replace("%",""))

    status, recommendation = get_recommendation(instance, cpu)

    headers = [
        "Serial No.",
        "Current EC2",
        "Current CPU",
        "Status",
        "Recommended EC2"
    ]

    rows = [
        [1, instance, f"{cpu}%", status, recommendation]
    ]

    print_table(headers, rows)


if __name__ == "__main__":
    main()