#!/usr/bin/python3

#RAYANE - MAD

if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    sum = 0
    for i in range(n):
        sum = sum + int(sys.argv[i + 1])
    print("{}".format(sum))
