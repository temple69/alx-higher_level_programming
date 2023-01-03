#!/usr/bin/python3
for int in range(0, 110):
    if int != 99:
        print("{:02},".format(int), end=" ")
    else:
        print("{:02}".format(int))