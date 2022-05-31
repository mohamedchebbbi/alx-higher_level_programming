#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i+1, 10):
        if (i + j != 17):
            print("{:d}{:d}".format(i, j), end=', ')
        else:
            print("{:d}{:d}".format(i, j))
