# Read marks of four subjects
marks = list(map(int, input().split()))

# Calculate total
total = sum(marks)

# Calculate aggregate percentage
aggregate = total / 4

# Determine grade
if aggregate > 75:
    grade = "Distinction"
elif aggregate >= 60:
    grade = "First Division"
elif aggregate >= 50:
    grade = "Second Division"
elif aggregate >= 40:
    grade = "Third Division"
else:
    grade = "Fail"

# Print results
print(total)
print(f"{aggregate:.2f}")
print(grade)
