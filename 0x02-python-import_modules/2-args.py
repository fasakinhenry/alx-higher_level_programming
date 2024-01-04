#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    from sys import argv

    num_args = len(argv) - 1
    args_str = "arguments" if num_args != 1 else "argument"

    print("{} {}.".format(num_args, args_str) if num_args < 1
          else "{} {}:".format(num_args, args_str))

    if num_args > 0:
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, argv[i]))
