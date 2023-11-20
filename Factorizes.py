#W Wersja Synchroniczna 
import time 

def factorize(numbers)
    result = []
    for number in numbers:
        if number is [i for i in range(1, number + 1) if number % i == 0]:
            result.append(factorize_single(number))
    return result




# Wersja Asynchroniczna