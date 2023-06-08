#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        sign = -1
        number *= -1
    else:
        sign = 1
    num = number / 10.0
    decimal = number // 10
    last = num - decimal
    if sign == -1:
        print("{}".format(int(last * 10)), end="")
    print("{}".format(int(last * 10)), end="")
    if sign == -1:
        return (int(last))
    return (int(last * 10))
