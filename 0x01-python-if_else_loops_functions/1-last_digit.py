#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = -(-number % 10)
else:
    last_digit = number % 10
if last_digit > 5:
    result = 'and is greater than 5'
elif last_digit == 0:
    result = 'and is 0'
else:
    result = 'and is less than 6 and not 0'
print('Last digit of', '{:d}'.format(number), 'is ', end="")
print('{:d}'.format(last_digit), result)
