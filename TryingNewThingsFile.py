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


# Test the find_word function
text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
word = "Python"
print(find_word(text, word))
