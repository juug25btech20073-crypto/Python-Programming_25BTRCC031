NUMBER_OF_SUBJECTS = 5
MAX_MARKS_PER_SUBJECT = 100


def analyze_performance():
    student_name = input("Enter Student Name: ")
    usn = input("Enter USN: ")

    subject_marks = []
    total_marks = 0.0

    for i in range(1, NUMBER_OF_SUBJECTS + 1):
        while True:
            try:
                marks = float(input(f"Enter marks in Subject {i} (out of 100): "))
                if 0 <= marks <= MAX_MARKS_PER_SUBJECT:
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input.")

        subject_marks.append(marks)
        total_marks += marks

    percentage = (total_marks / (NUMBER_OF_SUBJECTS * MAX_MARKS_PER_SUBJECT)) * 100
    average = total_marks / NUMBER_OF_SUBJECTS

    if percentage >= 90:
        grade = "O"
    elif percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "RA"

    print("\n" + "=" * 42)
    print("        STUDENT ACADEMIC REPORT CARD")
    print("=" * 42)
    print(f"Student Name : {student_name}")
    print(f"USN          : {usn}")
    print("-" * 42)

    for i, marks in enumerate(subject_marks, start=1):
        print(f"Subject {i} Marks : {marks:.2f} / {MAX_MARKS_PER_SUBJECT}")

    print("-" * 42)
    print(f"Total Marks : {total_marks:.2f} / {NUMBER_OF_SUBJECTS * MAX_MARKS_PER_SUBJECT}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Average     : {average:.2f}")
    print(f"Grade       : {grade}")
    print("=" * 42)


if __name__ == "__main__":
    analyze_performance()