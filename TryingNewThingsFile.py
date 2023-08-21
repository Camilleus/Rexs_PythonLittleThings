import re


def capital_text(text):
    text = text.capitalize()
    text = re.sub(r'([.!?]\s*)([a-z])',
                  lambda m: m.group(1) + m.group(2).upper(), text)

    return text


text = "lubie jest przykład. co dalej? okej! tak to jest."
capitalized_text = capital_text(text)
print(capitalized_text)
