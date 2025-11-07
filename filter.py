def filter_students_by_major(students, major):
    """
    Return a filtered list of students by major using list comprehension.
    """
    return [student for student in students if student[2].lower() == major.lower()]
