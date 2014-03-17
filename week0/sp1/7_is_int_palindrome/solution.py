def is_int_palindrom(n):
    x = str(n)
    flag = 0
    if len(x) % 2 == 0:
        length = len(x) // 2
    else:
        length = len(x) // 2 + 1
    for i in range(0,length-1):
        if x[i] == x[len(x)-1 - i]:
            flag = 1
        else:
            flag = 0
    if flag == 1 or len(x) == 1:
        return True
    else:
        return False

def main():
    print(is_int_palindrom(1))
    print(is_int_palindrom(999))

if __name__ == '__main__':
    main()