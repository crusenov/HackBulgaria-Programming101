def count_vowels(str):
    x = str.lower()
    count = 0
    for i in x:
        if i in "aeiouy":
            count += 1
    return count



