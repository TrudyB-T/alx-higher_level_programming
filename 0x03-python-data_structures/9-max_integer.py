#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        for i in range(len(my_list)):
            my_list.sort()
        return (my_list[len(my_list) - 1])
