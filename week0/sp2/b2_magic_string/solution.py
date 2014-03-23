def magic_string(s):
    count = 0
    for i, char in enumerate(s):
        if i < len(s)//2 and char == '<' or i >= len(s)//2 and char == '>':
            count += 1
    return count

