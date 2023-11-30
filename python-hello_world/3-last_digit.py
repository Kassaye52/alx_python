#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

last_digit = number % 10 if number > 0 else -(-number % 10)  # Get the last digit with the same sign as the number

if last_digit > 5:
    message = "and is greater than 5"
elif last_digit == 0:
    message = "and is 0"
else:
    message = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} {message}")


