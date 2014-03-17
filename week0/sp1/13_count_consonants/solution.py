def count_consonants(str):
    x = str.lower()
    count = 0
    for i in x:
        if i in "bcdfghjklmnpqrstvwxz":
            count += 1
    return count
