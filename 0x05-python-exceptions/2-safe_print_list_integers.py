#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                y += 1
    except (TypeError, ValueError):
        pass
    print()
    return y
