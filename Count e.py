sentance = input("Sentance: ")
count = 0
for e in range(len(sentance)):
    if "e" in sentance[e]:
        count +=1
print(count)