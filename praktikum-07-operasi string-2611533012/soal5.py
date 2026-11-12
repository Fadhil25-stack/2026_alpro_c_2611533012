# Name: Muhammad Fadhil Andavi
# NIM: 2611533012
# Question 1


username = input("Username: andi@123 ")

if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")