#!/bin/python3
def main():
    import add_0 as add_func
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b,  add_func.add(a, b)))


if __name__ == "__main__":
    main()
