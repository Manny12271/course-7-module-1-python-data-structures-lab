from lib.data_processing import display_students, format_student_data


def test_format_student_data():
    student = (101, "Alice Johnson", "Computer Science")
    expected_output = "ID: 101 | Name: Alice Johnson | Major: Computer Science"
    assert format_student_data(student) == expected_output


def test_display_students(capsys):
    students = [
        (101, "Alice Johnson", "Computer Science"),
        (102, "Bob Smith", "Mathematics"),
    ]
    display_students(students)
    captured = capsys.readouterr()
    assert "Alice Johnson" in captured.out
    assert "Bob Smith" in captured.out
