from student_data import students
from filter import filter_students_by_major
from data_processing import display_students
from set_operations import unique_majors
from data_generator import student_generator

# --- Demonstrate filtering ---
print("📘 Students in Computer Science:")
cs_students = filter_students_by_major(students, "Computer Science")
display_students(cs_students)

# --- Display unique majors ---
print("\n🎓 Unique Majors:")
print(unique_majors(students))

# --- Demonstrate generator expression ---
print("\n⚡ Students (via generator) in Mathematics:")
math_gen = student_generator(students, "Mathematics")

for student in math_gen:
    print(student)
