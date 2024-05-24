#!/usr/bin/env python3

def print_fibonacci(length):
    fib = [0, 1]
    
    if length == 1:
        fib.pop()
    
    elif length == 0:
        fib.clear()
   
    while len(fib) < length:
       fib.append(fib[-1] + fib[-2])
    print(fib)
    return fib
   
(print_fibonacci(0))