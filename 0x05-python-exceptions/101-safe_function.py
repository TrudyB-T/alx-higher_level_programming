#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        product = fct(*args)
        return product
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
