def count_letter(find, sentance):
    count = 0
    for find in sentance:
        count += 1
    return count

sentance = input("Sentance: ")
find = input("letter to find: ")

print(count_letter(find, sentance))
