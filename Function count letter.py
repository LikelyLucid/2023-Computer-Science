def count_letter(find, sentence):
    return sum(find in sentence[i] for i in range(len(sentence)))

sentence = input("Sentance: ")
find = input("letter to find: ")

print(count_letter(find, sentence))
