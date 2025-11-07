def unique_majors(students):
    """
    Return a set of unique majors from the student list using set comprehension.
    """
    return {student[2] for student in students}
