#W Wersja Synchroniczna 
import time 

def factorize(numbers)
    result = []
    for number in numbers:
        if number is [i for i in range(1, number + 1) if number % i == 0]:
            result.append(factorize_single(number))
    return result

def time_measurement(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time


# Wersja Asynchroniczna