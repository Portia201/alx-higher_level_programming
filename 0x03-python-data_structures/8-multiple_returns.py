#!/usr/bin/python3
def multiple_returns(sentence):
"""
Args:
    sentence: a string argument

Returns:
    a tuple with the length of a string and its first character
"""

str_len, first_char = len(sentence), sentence[0]
return (str_len, first_char)
