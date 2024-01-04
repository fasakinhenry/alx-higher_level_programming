#!/usr/bin/python3

if __name__ == "__main__":
    """prints the result of the addition of all arguments (argv)"""
    from sys import argv

    if len(argv) > 1:
        run_sum = 0
        for i in range(1, len(argv)):
            run_sum += int(argv[i])
        print("{}".format(run_sum))
    else:
        print("0")
