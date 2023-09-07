import time


cached = {}


def cache(fn):
    def wrapper(n):
        if n not in cached:
            cached[n] == fn[n]
            return cached[n]
    return wrapper


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
