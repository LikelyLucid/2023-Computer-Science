numbers = [20, 36, 12, 24, 20, 48, 74, 353, 23, 98]

largest = 0

for i in range(len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]