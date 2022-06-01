#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = int(str(number)[-1])

if 6 > last_digit > 0:
    print(str(last_digit) + " is less than 6 and not 0\n")
elif last_digit > 5:
    print(str(last_digit) + " is greater than 5")
elif last_digit % 10 == 0:
    print(str(last_digit) + "is 0")
