#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

num = int(input("Please enter a positive integer: "))
a = 0
b = 1
temp = 0
if num <= 0:
  print("Invalid input")

else:
  for i in range(num):
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b
