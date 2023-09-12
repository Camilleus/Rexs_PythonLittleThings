import time
from functools import lru_cache


@lru_cache()
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


start = time.time()
n = int(input("Which number of Fibonacci sequence do you want to see? (If it is bigger than 20, this can take a little bit more time)"))
for i in range(n+1):
    print(f"{i}. Fibonacci sequence number is {fibonacci(i)}")

end = time.time()
print(f"This operation took {end - start} seconds")


""""
import time


def fibonacci(n):
    if n <= 1:
        return n

    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence[n]


while True:
    try:
        n = int(input("Which number of the Fibonacci sequence do you want to see? (If it is bigger than 20, this can take a little bit more time): "))
        if n < 0:
            print("Please enter a non-negative integer.")
            continue

        start = time.time()
        result = fibonacci(n)
        end = time.time()

        print(f"{n}. Fibonacci sequence number is {result}")
        print(f"This operation took {end - start:.6f} seconds")

    except ValueError:
        print("Please enter a valid integer.")
"""
"""
FIBONACCI SEQUENCE


def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

nterms = int(input)
for i in range(nterms):
    print(f"Fibonacci sequence:{fibonacci(i)}")



#Other Version of it : 

import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


start = time.time()
n = int(input("Which number of Fibonacci sequence do you want to see? (If it is bigger than 20, this can take a little bit more time)"))
for i in range(n):
    print(f"{i}. Fibonacci sequence number is {fibonacci(i)}")

end = time.time()
print(f"This operation took {end - start} seconds")
"""
