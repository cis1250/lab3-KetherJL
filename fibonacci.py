#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

a = 0
b = 1
temp = 0
while True:
    num = input("Please enter a positive integer: ")

    if num.isdigit():
        num = int(num)
        if num > 0:
            break
        
        else:
            print("Enter a valid integer")
    else:
        print("Enter a number")

for i in range(num):
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b
