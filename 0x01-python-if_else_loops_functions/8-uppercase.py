#!/usr/bin/python3
# 8-uppercase.py
# Portia Aphane <portia201@github.com>

def uppercase(str):
    """Print a string in uppercase."""
    for s in str:
        tmp = ord(s)
        if tmp >= 97 and tmp <= 122:
            pr = chr(tmp - 32)
        else:
            pr = s
        print('{}'.format(pr), end="")
    print()
