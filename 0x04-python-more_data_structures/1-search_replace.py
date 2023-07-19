#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nu_list = my_list[:]
    for i in range(len(nu_list)):
        if nu_list[i] == search:
            nu_list[i] = replace
    return nu_list
