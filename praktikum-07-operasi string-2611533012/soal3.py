# Name: Muhammad Fadhil Andavi
# NIM: 2611533012
# Question 1

text = "informatika"
print(text[-1])
print(text.upper())
print(text[0:20])

text = "Muhammad Fadhil Andavi"
count = 0

for char in text:
    if char.lower() in "aiueo":
        count += 1

print("Vowels:", count)
