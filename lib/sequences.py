#!/usr/bin/env python3

def print_fibonacci(length):
    if(length == 0):
        print([])
    elif(length == 1):
        print([0])
    elif(length == 2):
        print([0, 1])
    else:
        fibonacci_list = [0, 1]
        for num in range(length - 2):
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
        print(fibonacci_list)