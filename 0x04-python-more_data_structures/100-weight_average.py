#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    new_score = 0
    w8 = 0

    for score, weigght in my_lisr:
        new_score += score * weight
        w8 += weight

    return new_score / w8
