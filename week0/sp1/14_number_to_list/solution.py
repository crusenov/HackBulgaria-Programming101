def number_to_list(n):
    x = []
    while  n != 0:
        x.append(n % 10)
        n =  n // 10
    x.reverse()
    return x
