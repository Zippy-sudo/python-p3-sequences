#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []

    if length < 1 :
        pass
    elif length == 1 :
        fib.append(0)
    elif length == 2 :
        fib.append(0)
        fib.append(1)
    else :
        fib.append(0)
        fib.append(1)

        while len(fib) < length:
            fib.append(fib[-2] + fib[-1])

    return print(fib)
