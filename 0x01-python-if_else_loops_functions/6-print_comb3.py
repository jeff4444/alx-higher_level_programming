#!/usr/bin/python3
for i in range(1, 100):
    if i < 10:
        print("{:02d}".format(i), end=", ")
    else:
        if i == 89:
            print("{}".format(i))
        elif (i - ((i // 10) * 10)) not in range((i // 10) + 1):
            print("{:02d}".format(i), end=", ")
