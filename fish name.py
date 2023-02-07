fish = ["flounder", "sole", "blue cod", "snapper", "terakihi", "john dory", "red cod"]
# a
for item in fish:
    print(item[0])

print()
# b
for item in fish:
    print(item[0:3])

print()
# c
largest = ""
for item in fish:
    if len(item) >  len(largest):
        largest = item
print(largest)
# d

print()
for item in fish:
    if " " in item:
        print(item)