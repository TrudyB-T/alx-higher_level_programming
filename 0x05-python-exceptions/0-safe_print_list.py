#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
    except IndexError:
        x = 0
        for element in my_list:
            print(end="")
            x += 1
    finally:
        print()
    return x
