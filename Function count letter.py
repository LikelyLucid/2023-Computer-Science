def count_letter(find, sentance):
    return sum(find in sentance[i] for i in range(len(sentance)))

sentance = input("Sentance: ")
find = input("letter to find: ")

print(count_letter(find, sentance))
