#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator, denominator = 0, 0
    for i, v in my_list:
        numerator += (i * v)
        denominator += v
    return (numerator / denominator)
