#!/usr/bin/python3
def fizzbuzz():
    for figure in range(1, 101):
        if figure % 3 == 0 and figure % 5 == 0:
            print("FizzBuzz ", end="")
        elif figure % 3 == 0:
            print("Fizz ", end="")
        elif figure % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(figure), end="")
