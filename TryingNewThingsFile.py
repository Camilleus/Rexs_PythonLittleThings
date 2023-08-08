import re


def find_all_phones(text):
    all_phones = re.compile(r'\+380\(\d{2}\)777-\d{1,2}-\d{2,3}')
    result = all_phones.findall(text)
    return result


text = "Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787"
phones = find_all_phones(text)
print(phones)
