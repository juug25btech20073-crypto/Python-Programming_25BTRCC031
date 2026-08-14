names = ["Arun", "Bala", "Charan", "Divya", "Esha"]
marks = [85, 72, 38, 105, 91]

valid_count = 0

for i, (name, mark) in enumerate(zip(names, marks), start=1):
    if mark < 0 or mark > 100:
        print(f"Invalid marks for {name} - Skipped")
        continue

    if mark >= 80 and mark <= 100:
        result = "Excellent"
    elif mark >= 60 and mark <= 79:
        result = "Good"
    elif mark >= 40 and mark <= 59:
        result = "Average"
    else:
        result = "Fail"

    print(f"{i}. {name} - {mark} - {result}")
    valid_count += 1

print(f"Total Valid Students: {valid_count}")