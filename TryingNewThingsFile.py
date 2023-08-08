import re


def replace_spam_words(text, spam_words):
    for word in spam_words:
        escaped_word = word.replace('+', r'\+')
        word_pattern = re.compile(rf'\b{escaped_word}\b', re.IGNORECASE)
        text = word_pattern.sub('*' * len(word), text)
    return text

text = "Python is an amazing programming language, but beware of spam words like JAVA, c++, and javascript."
spam_words = ["java", "c++", "javascript"]
result = replace_spam_words(text, spam_words)
print(result)
