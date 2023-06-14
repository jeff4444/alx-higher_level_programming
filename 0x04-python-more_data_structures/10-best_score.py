#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    maximum, maxi = list(a_dictionary.items())[0]
    for key, value in a_dictionary.items():
        if value > maxi:
            maxi = value
            maximum = key
    return maximum
