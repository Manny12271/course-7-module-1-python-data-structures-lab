def student_generator(students, major):
    """
    Return a generator expression that yields students by a given major.
    """
    return (student for student in students if student[2].lower() == major.lower())
