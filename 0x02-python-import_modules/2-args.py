#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arc = len(argv)
    if arc > 2:
        print("{:d} {:s}:".format(arc-1, "arguments"))
        for i, s in enumerate(argv[1:]):
            print("{:d}: {:s}".format(i+1, s))
    if arc == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    if arc == 1:
        print("0 arguments.")
