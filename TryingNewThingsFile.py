def get_employees_by_profession(path, profession):
    matchings = []
    with open(path, 'r') as file:
        verses = file.readlines()
        for verse in verses:
            if profession in verse:
                matchings.append(verse)

    result = '\n'.join(matchings)
    result = result.replace(profession, "")

    return result

