#!/usr/bin/python3
def fizzbuzz():
    num = 1
    while (num <= 100):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end="")
            num += 1
        elif num % 3 == 0:
            print("Fizz ", end="")
            num += 1
        elif num % 5 == 0:
            print("Buzz ", end="")
            num += 1
        else:
            print(f"{num} ", end="")
            num += 1
