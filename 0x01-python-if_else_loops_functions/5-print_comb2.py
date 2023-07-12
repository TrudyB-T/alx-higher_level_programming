#!/usr/bin/python3
for figure in range(0, 100):
    if figure == 99:
        print(f"{figure}")
    else:
        print("{:02}".format(figure), end=", ")
