"""
lOGICAL VARIABLES



is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")

access = False
is_admin = False
is_active = False
is_permission = False

if access is 1:
    is_permission = True
else:
    is_permission = False

if is_admin is True:
    is_permission = True
    is_active = True
else:
    is_admin = False

if access is True and is_active is True:
    is_permission = True
    is_active = True
else:
    is_permission = False
    is_active = False

if is_permission is True:
    acces = True
else:
    acces = False

"""
"""
SQUARE EQUATION


import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
elif D == 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
else:
    D < 0
"""
"""
GREATEST COMMON DIVISOR



first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = int( first if first < second else second)
smaller = int( first if first < second else second)
bigger = int( first if first > second else second)

while bigger % gcd != 0 :
    gcd -= 1
    print(gcd)
    if bigger % int(gcd) == 0:
        if smaller % int(gcd) != 0:
            gcd -= 1
            print(gcd)
        else:
            print(gcd)

    
"""
"""
CAESAR'S CODE



message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    letter = ""
    if not ch.isalpha():
        encoded_message += ch
        continue
    if 65 <= ord(ch) <= 90:
        letter = "A"
    else:
        letter = "a"
    pos = ord(ch) - ord(letter)
    pos = (pos + offset) % 26
    new_char = chr(pos + ord(letter))
    encoded_message += new_char     
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
"""
"""
Factorial / Silnia


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

factorial(5)# 120
"""
