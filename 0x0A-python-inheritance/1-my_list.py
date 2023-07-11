#!/usr/bin/python3
""" MyList class """


class MyList(list):
    """ MyList class """
    def print_sorted(self):
        """ Prints the list in ascending order"""
        print(sorted(self))
