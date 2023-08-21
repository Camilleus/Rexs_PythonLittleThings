grades_points = {
    "1": 0,
    "2": 35,
    "3": 60,
    "4": 75,
    "5": 90,
    "6": 100
}

grades_ects = {
    "1": "F",
    "2": "FX",
    "3": "E",
    "4": "D",
    "5": "C",
    "6": "B",
    "7": "A"
}

grades_descriptions = {
    "1": "Unsatisfactorily",
    "2": "Unsatisfactorily",
    "3": "Enough",
    "4": "Satisfactorily",
    "5": "Good",
    "6": "Very good",
    "7": "Perfectly"
}
def get_grade(ects_grade):
    for grade, points in grades_points.items():
        if ects_grade == grades_ects[grade]:
            return int(grade)
    return None
def get_description(ects_grade):
    for grade, description in grades_descriptions.items():
        if ects_grade == grades_ects[grade]:
            return description
    return None

ects_grade = "C"
grade = get_grade(ects_grade)
description = get_description(ects_grade)
print(f"Grade: {grade}")
print(f"Grade Description: {description}")