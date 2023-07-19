#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        key_val = list(a_dictionary.items())
        best_scr_ky, best_scr = max(key_val, key=lambda x: x[1])

    return best_scr_ky
