#!/usr/bin/python3
"""A script that reads STDIN line by line and computes metrics."""


def show_stats(size, status_codes):
    """Prints the metrics.
    Arguments:
        size (integer): The read file size.
        status_codes (dict): An arry of status codes.
    """
    print("File size: {}".format(size))
    for array_key in sorted(status_codes):
        print("{}: {}".format(array_key, status_codes[array_key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    counter = 0

    try:
        for current_line in sys.stdin:
            if (counter == 10):
                show_stats(size, status_codes)
                counter = 1
            else:
                counter += 1
            current_line = current_line.split()

            try:
                size += int(current_line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if (current_line[-2] in codes):
                    if (status_codes.get(current_line[-2], -1) == -1):
                        status_codes[current_line[-2]] = 1
                    else:
                        status_codes[current_line[-2]] += 1
            except IndexError:
                pass
            show_stats(size, status_codes)

    except KeyboardInterrupt:
        show_stats(size, status_codes)
        raise
