#!/usr/bin/env python3

def print_fibonacci(length):
    if (length <= 0):
        print([])
    elif (length == 1):
        print([0])
    else:
        fib_list = [0, 1]
        while (len(fib_list) < length):
            new_num = fib_list[-1] + fib_list[-2]
            fib_list.append(new_num)
        print(fib_list)
        

