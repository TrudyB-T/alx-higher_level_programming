#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_keys = sorted(a_dictionary)

    for key in new_keys:
        print(f"{key}: {a_dictionary[key]}")
