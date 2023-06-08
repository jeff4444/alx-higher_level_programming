#!/usr/bin/python3
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
