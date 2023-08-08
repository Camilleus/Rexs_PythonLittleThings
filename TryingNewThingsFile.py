import re


def find_all_emails(text):
    email_pattern = re.compile(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Za-z]{2,}\b')
    result = email_pattern.findall(text)
    return result
