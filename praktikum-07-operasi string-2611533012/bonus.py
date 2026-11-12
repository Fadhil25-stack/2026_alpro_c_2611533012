# Name: Muhammad Fadhil Andavi
# NIM: 2611533012
# Question 1

kalimat = input("Masukkan kalimat: ")

clean = kalimat.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")