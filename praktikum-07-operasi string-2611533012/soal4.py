# Name: Muhammad Fadhil Andavi
# NIM: 2611533012
# Question 1


phone = "082611533012"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)
