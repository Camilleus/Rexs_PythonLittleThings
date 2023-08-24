import re

def get_employees_by_profession (path, profession): 
    with open(path, 'r') as file:
        verses = file.readlines()
        matchings = []
        for verse in verses:
            if verse.find(profession) > 0:
                vers = verse.replace(profession, "") 
                matchings.append(re.sub (r'\s+', '', vers))
        return ' '.join(matchings)