def decode(encoded_list):
    if not encoded_list:
        return []

    first = encoded_list[0]
    rest = encoded_list[1:]

    if isinstance(first, int):
        if rest[0]:
            value = rest[0]
        count = first

        return [value] * count + decode(rest[1:])
    else:
        return [first] + decode(rest)

# Przykład użycia
encoded_list = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
decoded_list = decode(encoded_list)
print(decoded_list)  # Powinno wypisać: ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']
