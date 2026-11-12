# Name: Muhammad Fadhil Andavi
# NIM: 2611533012
# Question 1


name = "muhammad fadhil andavi"
nim = "2611533012"

username = "muhammad012"
intake = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)