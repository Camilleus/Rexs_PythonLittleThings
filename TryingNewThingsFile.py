import re


def find_all_emails(text):
    all_emails = re.compile(r"[a-zA-Z][a-zA-Z0-9_.]+@[a-z]+\.[a-z]{2,}")
    result = all_emails.findall(text)
    return result
