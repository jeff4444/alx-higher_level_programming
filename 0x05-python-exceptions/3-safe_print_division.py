#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        avg = a / b
    except ZeroDivisionError:
        avg = None
    finally:
        print(f'Inside result: {avg}')
    return avg
