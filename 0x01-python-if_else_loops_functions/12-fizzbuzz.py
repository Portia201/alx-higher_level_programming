#!/usr/bin/python3
# 12-fizzbuzz.py

def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz ', end="")
        elif i % 3 == 0:
            print('Fizz ', end="")
        else:
            print('{} '.format(i), end="")
