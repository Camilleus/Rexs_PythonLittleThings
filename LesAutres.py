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


"""
articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

def find_articles(key, letter_case=False):
    founded_articles = []
    for article in articles_dict:
        title = article['title']
        author = article['author']
        year = article['year']

        if not letter_case:
            key = key.lower()
            title_lower = title.lower()
            author_lower = author.lower()
        else:
            title_lower = title
            author_lower = author

        if key in title_lower or key in author_lower:
            founded_articles.append({
                'author': author,
                'title': title,
                'year': year
            })

    if not founded_articles:
        print("Not found")

    return founded_articles

"""
"""
import re


def find_word(text, word):
    search_result = re.search(rf'\b{re.escape(word)}\b', text, re.IGNORECASE)

    if search_result:
        result_dict = {
            'result': True,
            'first_index': search_result.start(),
            'last_index': search_result.end() - 1,
            'search_string': search_result.group(),
            'string': text
        }
    else:
        result_dict = {
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text
        }

    return result_dict
"""