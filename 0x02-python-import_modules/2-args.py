#!/usr/bin/python3
def main():
    import sys
    length = len(sys.argv) - 1
    print("{} argument".format(length), end="")
    if length == 1:
        print(":")
    elif length > 1:
        print("s:")
    else:
        print("s.")
    for i, arg in enumerate(sys.argv):
        if i > 0:
            print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
