#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = dict(sorted(a_dictionary.items(), key=lambda x: x[0]))
    for key, value in new_dict.items():
        print("{}: {}".format(key, value))
