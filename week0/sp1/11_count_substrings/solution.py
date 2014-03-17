def count_substrings(haystack, needle):
    count = 0
    x = haystack.split()
    #print x
    for i in x:
        if needle in i:
            count += i.count(needle)
    return count
