#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        ldigit = number % 10
    else:
        ldigit = number % -10
        ldigit *= -1

    print("{:d}".format(ldigit), end='')
    return ldigit
