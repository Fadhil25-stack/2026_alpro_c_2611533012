all_students = input().split()
submitted = input().split()
submitted_set = set(submitted)
submitted_count = len(submitted_set)
not_submitted = set(all_students) - submitted_set

print("Submitted:", submitted_count, "students")
print("Not submitted:", len(not_submitted), "students")
for student in all_students:
    if student not in submitted_set:
        print(student)