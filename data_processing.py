def format_student_data(student):
    """
    Format one student's info as a string.
    Example: "ID: 101 | Name: Alice Johnson | Major: Computer Science"
    """
    return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"


def display_students(students):
    """
    Loop through all students and print formatted details.
    """
    for student in students:
        print(format_student_data(student))
