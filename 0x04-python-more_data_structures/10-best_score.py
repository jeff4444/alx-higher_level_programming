#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if a_dictionary == {}:
        return None
    maximum, maxi = list(a_dictionary.items())[0]
    for key, value in a_dictionary.items():
        if value > maxi:
            maxi = value
            maximum = key
    return maximum
