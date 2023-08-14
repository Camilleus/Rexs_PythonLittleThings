def is_equal_string(utf8_string, utf16_string):
    utf8_normalized = utf8_string.decode('utf-8').casefold().encode('utf-8')
    utf16_normalized = utf16_string.decode('utf-16').casefold().encode('utf-8')
    return utf8_normalized == utf16_normalized
