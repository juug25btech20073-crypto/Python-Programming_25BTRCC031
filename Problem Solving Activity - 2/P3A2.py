names = ["Anu", "Bharath", "Chitra", "Deepak", "Farah"]
attendance = [92, 68, 85, 45, 78]
marks = [88, 55, 76, 32, 91]

eligible_count = 0

for i, (name, att, mark) in enumerate(zip(names, attendance, marks), start=1):
    if att < 0 or att > 100 or mark < 0 or mark > 100:
        continue

    if att >= 75:
        if mark >= 80 and mark <= 100:
            grade = "Distinction"
        elif mark >= 60 and mark <= 79:
            grade = "First Class"
        elif mark >= 40 and mark <= 59:
            grade = "Pass"
        else:
            grade = "Fail"

        print(f"{i}. {name} - Attendance: {att}% - Marks: {mark} - {grade}")
        eligible_count += 1
    else:
        print(f"{i}. {name} - Attendance: {att}% - Not Eligible")

print(f"Total Eligible Students: {eligible_count}")