#!/usr/bin/python3

if __name__ == "__main__":
    """add all the arguments together."""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
