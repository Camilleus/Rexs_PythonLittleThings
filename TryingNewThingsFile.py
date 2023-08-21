def is_integer(s):
    s = s.strip()
    if len(s) == 0:
        return False
    if s[0] in ['+', '-']:
        s = s[1:]
    if s.isdigit():
        return True
    else:
        return False
