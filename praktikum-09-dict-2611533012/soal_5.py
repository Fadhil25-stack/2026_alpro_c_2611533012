n = int(input())

cash = {}

for i in range(n):
    data = input().split()
    name = data[0]
    amount = int(data[1])

    if name in cash:
        cash[name] += amount
    else:
        cash[name] = amount

total_cash = sum(cash.values())

top_name = ""
top_amount = 0

for name, amount in cash.items():
    if amount > top_amount:
        top_name = name
        top_amount = amount

for name, amount in cash.items():
    print(name + ":", amount)

print("Total cash:", total_cash)
print("Top contributor:", top_name, "(" + str(top_amount) + ")")