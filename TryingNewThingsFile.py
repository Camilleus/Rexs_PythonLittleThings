def decode(data):
    if len(data)==2:
        return [data[0]]*data[1]
    elif len(data)<2:
        return data
    return decode(data[:2])+decode(data[2:])

# Przykład użycia
encoded_list = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
decoded_list = decode(encoded_list)
print(decoded_list)  # Powinno wypisać: ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']
