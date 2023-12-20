#!/usr/bin/python3
from sys import stderr
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as Exc:
        stderr.write("Exception: {}\n".format(Exc))
        return None
